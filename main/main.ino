#include <Wire.h>
#include <SPI.h>
#include <TinyScreen.h>

// Include all frame headers
#include "frame_00.h"
#include "frame_01.h"
#include "frame_02.h"
#include "frame_03.h"
// Continue including all frame headers

TinyScreen display = TinyScreen(0);

// Create a list of frame pointers
const uint8_t* frames[] = {
  frame_00, frame_01, frame_02, frame_03,
  // Continue adding all frame pointers
};

const int frame_count = sizeof(frames) / sizeof(frames[0]);

void setup() {
  Wire.begin();
  display.begin();
  display.setBrightness(10);
}

void loop() {
  for (int i = 0; i < frame_count; i++) {
    display.setX(0, 95);
    display.setY(0, 63);
    display.startData();
    display.writeBuffer((uint8_t*)frames[i], 96 * 64);
    display.endTransfer();
    delay(100); // Adjust delay for speed control
  }
}
