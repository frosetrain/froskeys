import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP6, 1)

while True:
    pixels[0] = (100, 0, 0)
    pixels.show()
    time.sleep(0.2)
    pixels[0] = (0, 100, 0)
    pixels.show()
    time.sleep(0.2)
    pixels[0] = (0, 0, 100)
    pixels.show()
    time.sleep(0.2)
