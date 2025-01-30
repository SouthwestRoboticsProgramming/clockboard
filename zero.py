import multiprocessing as mp
import queue
import time

# Real sheet
#sheet_id = "1u2M_qIo_XLVv5HPKYmyX_ehruxVFECf8vmXNKnErk4U"
#sheets_key_file = "/creds/service_account.json"

# Test sheet
sheet_id = "1H6hMCbpaxb5Ts8yTO4nVpE3nqBfmG2kIDezKE0Cf5QQ"
sheets_key_file = "service_account.json"

rows = 6
cols = 5
button_row_pins = [2, 3, 4, 17, 27, 22]
button_col_pins = [26, 19, 13, 6, 5]

button_scan_interval_ms = 10

# Seconds between refreshing data from Sheets API
# Rate limit is 60 read requests/min, so 10 seconds/request -> 6 requests/min
# should be safe
refresh_interval = 10

pico_port_name = "/dev/serial0"
pico_port_baud = 115200
pico_start_bit = 0b10000000

# Order of these should match order of buttons (down, then to right),
# and match the order of the people in the sheet
student_names = [
    "Mason", "Cameron", "Jonah", "Jerry", "Henri K", "Liam",
    "Ki Bae", "Oliver", "Clark", "Rain", "Malcom", "Henry N",
    "Auggie", "Anders G", "Victor", "Finn", "Sam", "Neah",
    "Sophia", "Eddie", "Sadie", "Alena", "Anders T", "Owen",
    "Anna", "Kaelan", "Drew"
]

def scan_buttons(press_queue, stop_event):
    try:
        import RPi.GPIO as GPIO
    except RuntimeError:
        print("This script must be run as superuser")

    # FIXME: I don't know whether this should be BOARD or BCM
    GPIO.setmode(GPIO.BOARD)

    for pin in button_row_pins:
        GPIO.setup(pin, GPIO.IN)
    for pin in button_col_pins:
        GPIO.setup(pin, GPIO.OUT)

    print("Button scanning started")
    prev_pressed_buttons = []
    while not stop_event.is_set():
        pressed_buttons = []
        for col in range(cols):
            for i in range(cols):
                GPIO.output(button_col_pins[i], i == col)
                
            time.sleep(button_scan_interval_ms / 1000.0)
            for row in range(rows):
                if GPIO.input(button_row_pins[row]):
                    index = row + col * rows
                    pressed_buttons.append(index)

        # Only handle presses if exactly one button is down
        # Prevents matrix ghosting by ignoring the problem
        if len(pressed_buttons) == 1:
            button = pressed_buttons[0]
            if button not in prev_pressed_buttons:
                # Button was just pressed, enqueue event
                press_queue.put(button)

        prev_pressed_buttons = pressed_buttons

    print("Button scanning stopped")

def get_clocked_in_from_sheet(sheet):
    min_column = 2
    max_column = min_column + len(student_names) - 1

    values = sheet.range(f"J{min_column}:J{max_column}")
    return [(cell.value == "Clocked In") for cell in values]

def send_leds_to_pico(port, led_states):
    led_data = [pico_start_bit, 0, 0, 0, 0]
    for i in range(len(led_states)):
        row = i % 5
        col = i // 5
        led_data[col] |= (1 << row)

    led_bytes = bytes(led_data)
    port.write(led_bytes)

should_stop = False

def signal_handler(signal_recv, frame):
    global should_stop
    should_stop = True
    
def main():
    print("Starting")

    from datetime import datetime
    from google.oauth2.service_account import Credentials
    from google.auth.transport.requests import AuthorizedSession
    import gspread
    import serial

    credential_scopes = ["https://spreadsheets.google.com/feeds",
                         "https://www.googleapis.com/auth/drive"]
    credentials = Credentials.from_service_account_file(sheets_key_file, scopes=credential_scopes)
    sheets_client = gspread.authorize(credentials)
    sheet = sheets_client.open_by_key(sheet_id).sheet1
    print("Opened sheet")

    try:
        clocked_in = get_clocked_in_from_sheet(sheet)
        print("Initial clocked in state:")
        for name, is_clocked_in in zip(student_names, clocked_in):
            print(f"  {name}: {is_clocked_in}")
    except Exception as e:
        print("API Error! Assuming all are clocked out")
        print("Error is:", e)
        clocked_in = [False] * len(student_names)
    
    press_queue = mp.Queue()
    button_stop_event = mp.Event()
    button_proc = mp.Process(target=scan_buttons, args=(press_queue, button_stop_event))

    pico_serial = serial.Serial(pico_port_name, pico_port_baud)
        
    # We need to handle signals ourselves since we're using multiprocessing
    import signal
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    
    button_proc.start()

    next_cache_refresh = time.time() + refresh_interval
    
    print("Running...");
    while not should_stop:
        send_leds_to_pico(pico_serial, clocked_in)

        #try:
        #    press_queue.put(int(input()))
        #except:
        #    print("Not pressed this time")
        
        # Poll button events
        while True:
            try:
                pressed_button = press_queue.get_nowait()
                if pressed_button >= len(clocked_in):
                    # No person for this button
                    continue

                student_name = student_names[pressed_button]
                is_clocked_in = clocked_in[pressed_button]

                if is_clocked_in:
                    action = "Clock Out"
                else:
                    action = "Clock In"
                print(action + ": " + student_name)

                date_str = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                sheet.append_row([date_str, action, student_name], value_input_option="USER_ENTERED")

                # Update cache
                clocked_in[pressed_button] = not clocked_in
            except queue.Empty:
                # Queue is empty
                break
            
        time.sleep(0.1)
        if time.time() > next_cache_refresh:
            try:
                clocked_in = get_clocked_in_from_sheet(sheet)
                print("Cache refreshed from sheet:", clocked_in)
            except Exception as e:
                print("API Error:", e)

            next_cache_refresh = time.time() + refresh_interval

    print("Stopping...")
    button_stop_event.set()
    button_proc.join()
    
    print("Goodbye :3")

if __name__ == "__main__":
    main()
