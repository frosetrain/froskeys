import storage
import board
import digitalio

col_0 = digitalio.DigitalInOut(board.D0)
row_0 = digitalio.DigitalInOut(board.D10)

col_0.direction = digitalio.Direction.OUTPUT
col_0.value = True

row_0.direction = digitalio.Direction.INPUT
row_0.pull = digitalio.Pull.DOWN

if not row_0.value:
    storage.disable_usb_drive()
