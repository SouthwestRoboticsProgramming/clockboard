// Board install at https://arduino-pico.readthedocs.io/en/latest/install.html
#include "pico/stdlib.h"

// 6 rows x 5 columns
// Want to cycle on columns to maximize lit time -> maximize brightness

// GPIO 0-5 are rows top to bottom
// GPIO 6-10 are columns left to right

// Columns are negative side of LED -> drive LOW to light
// Rows are positive side -> drive HIGH to light

const uint8_t ROWS = 6;
const uint8_t COLS = 5;

// These bits correspond to the GPIO pins
const uint32_t ROWS_MASK = 0b00000111111;
const uint32_t COLS_MASK = 0b11111000000;

// All pins are outputs
const uint32_t OUTPUTS_MASK = ROWS_MASK | COLS_MASK;

const uint32_t COL_OUTPUTS[5] = {
  0b11110000000,
  0b11101000000,
  0b11011000000,
  0b10111000000,
  0b01111000000
};

// About 500 columns/sec = 100 Hz refresh rate
const uint16_t PERSIST_MICROS = 2000;

// Used to synchronize with Pi Zero transmission
// This bit does not correspond to LEDs so will only be set on first byte
const uint8_t START_BIT = 0b10000000;

// Bits 0-5 of each byte are LED states, each byte is a row
uint8_t led_state[COLS];

// Buffer for in-progress data read
uint8_t read_buf[COLS];
// Current index within read_buf, -1 means waiting for start byte
int8_t read_idx;

void setup() {
  gpio_init_mask(OUTPUTS_MASK);
  gpio_set_dir_out_masked(OUTPUTS_MASK);
  read_idx = -1;
}

void loop() {
  // Read at most one byte per loop to minimize LEDs dimming while receiving
  // This code must be as fast as possible since it's outside the matrix loop
  if (Serial.available()) {
    uint8_t in = Serial.read();

    // Check for start byte
    if (read_idx < 0 && (in & START_BIT) != 0) {
      read_idx = 0;
    }

    if (read_idx >= 0) {
      read_buf[read_idx++] = in;

      // Update LEDs once we've received all data
      if (read_idx >= COLS) {
        memcpy(led_state, read_buf, COLS);

        // Wait for next start byte
        read_idx = -1;
      }
    }
  }

  // Display LEDs
  for (uint8_t column = 0; column < COLS; column++) {
    uint32_t outputs = COL_OUTPUTS[column] | (led_state[column] & 0b111111);
    gpio_put_masked(OUTPUTS_MASK, outputs);

    // LED on time
    busy_wait_us_32(PERSIST_MICROS);
  }

  // All LEDs off so last column isn't slightly brighter
  gpio_put_masked(OUTPUTS_MASK, 0);
}
