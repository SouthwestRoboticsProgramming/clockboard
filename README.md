uses a pi pico w for controlling leds and a pi zero 2 w for interfacing.

leds are now connected to pico in a matrix.
buttons are connected to pi zero in a matrix (uses pull ups on the inputs because the pull downs werent behaving)

Button pressed -> check clock in/out state of person -> change cached clock in/out state of person -> send updated clock in/out state to pico -> push changed state to google sheet

for leds:
Columns are negative, rows are positive
GPIO:
row 1: 16
row 2: 17
row 3: 2
row 4: 3
row 5: 4
row 6: 5

column 1: 6
column 2: 7
column 3: 8
column 4: 9
column 5: 10



for buttons:

GPIO:
row 1: 2
row 2: 3
row 3: 4
row 4: 17
row 5: 27
row 6: 22

column 1: 26
column 2: 19
column 3: 13
column 4: 6
column 5: 5

pico connected to pi zero over UART (pins 1 and 2 on the pico, pins 8 and 10 on the pi zero)