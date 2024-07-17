# SPDX-FileCopyrightText: 2022 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from rainbowio import colorwheel
import neopixel

NUMPIXELS = 25  # Update this to match the number of LEDs.
SPEED = 0.01  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 0.1  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.A3  # This is the default pin on the 5x5 NeoPixel Grid BFF.

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)


def rainbow_cycle(wait):
    for color in range(255):
        for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
            pixel_index = (pixel * 256 // len(pixels)) + color * 5
            pixels[pixel] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def apple():
    # pixels go in order down from first column by gold plates
    for i in range(len(pixels)):
        pixels[i] = (255, 0, 0)

    pixels[0] = (0, 0, 0)
    pixels[1] = (0, 0, 0)
    pixels[5] = (0, 0, 0)

    pixels[10] = (125, 50, 0)
    pixels[11] = (125, 50, 0)
    pixels[15] = (125, 50, 0)
    
    pixels[20] = (0, 0, 0)
    pixels[21] = (0, 0, 0)
    pixels[4] = (0, 0, 0)
    pixels[24] = (0, 0, 0)
    pixels.show()
        
while True:
    # rainbow_cycle(SPEED)
    # print(pixels[0], pixels[24])
    apple()
