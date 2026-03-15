import board
import neopixel
import time
from rainbowio import colorwheel

NUM_PIXELS = 9

pixels = neopixel.NeoPixel(board.D6, NUM_PIXELS, brightness=0.1)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(NUM_PIXELS):
            rc_index = (i * 64 // NUM_PIXELS) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    rainbow_cycle(0)
    # pixels.fill((100, 0, 0))
    # pixels.show()
    # time.sleep(0.2)
    # pixels.fill((0, 100, 0))
    # pixels.show()
    # time.sleep(0.2)
    # pixels.fill((0, 0, 100))
    # pixels.show()
    # time.sleep(0.2)
