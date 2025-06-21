#include <Wire.h>
#include <SPI.h>
#include <TinyScreen.h>

// Include all frame headers
#include "frame_00.h"
#include "frame_01.h"
#include "frame_02.h"
#include "frame_03.h"
#include "frame_04.h"
#include "frame_05.h"
#include "frame_06.h"
#include "frame_07.h"
#include "frame_08.h"
#include "frame_09.h"
#include "frame_10.h"
#include "frame_11.h"
#include "frame_12.h"
#include "frame_13.h"
#include "frame_14.h"
#include "frame_15.h"
#include "frame_16.h"
#include "frame_17.h"
#include "frame_18.h"
#include "frame_19.h"
#include "frame_20.h"
#include "frame_21.h"
#include "frame_22.h"
#include "frame_23.h"
#include "frame_24.h"
// Continue including all frame headers

TinyScreen display = TinyScreen(0);

// Create a list of frame pointers
const uint8_t* frames[] = {
  frame_00, frame_01, frame_02, frame_03,
  frame_04, frame_05, frame_06, frame_07,
  frame_08, frame_09, frame_10, frame_11,
  frame_12, frame_13, frame_14, frame_15,
  frame_16, frame_17, frame_18, frame_19,
  frame_20, frame_21, frame_22, frame_23,
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
