import board
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB
from kmk.keys import KC, make_key
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.combos import Chord, Combos
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.macros import Delay, Macros, Press, Release, Tap
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
combos = Combos()
encoder = EncoderHandler()
rgb = RGB(pixel_pin=board.GP0, num_pixels=9, val_default=64, val_limit=64)
keyboard.modules = [Macros()]
keyboard.extensions = [MediaKeys(), Macros(), Layers(), combos, encoder]

make_key(
    names=("MYKEY",),
    on_press=lambda *args: print("I pressed MYKEY"),
)

combos.combos = [Chord((0, 1), KC.MYKEY, match_coord=True)]
encoder.pins = ((board.GP1, board.GP29, None),)
encoder.map = [
    ((KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.NO)),
    ((KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, KC.NO)),
]

keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP3, board.GP4, board.GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

PACMAN_SYU = KC.MACRO(
    Press(KC.LGUI),
    Tap(KC.T),
    Release(KC.LGUI),
    Delay(500),
    "sudo pacman -Syu",
    Tap(KC.ENTER),
)

keyboard.keymap = [
    [
        KC.LCTL(KC.Z),
        KC.LCTL(KC.Y),
        KC.MEDIA_PLAY_PAUSE,
        KC.F2,
        KC.LCTL(KC.D),
        PACMAN_SYU,
        KC.LCTL(KC.C),
        KC.LCTL(KC.V),
        KC.KP_EQUAL_AS400,
    ],
    [KC.TRNS] * 9,  # Transparent
]

if __name__ == "__main__":
    keyboard.go()
