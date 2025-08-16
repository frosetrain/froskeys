# Froskeys

![Render of Froskeys macropad](froskeys.png)

A 9-key macropad that I created for my own use-cases. I wanted some more keys next to my keyboard to do things like push-to-talk and other macros. Since my mouse is on the right of my laptop, my macropad shall sit on the left of my laptop.

There is a column of keys on the right of the macropad, to easily press with my pinky while my left hand is on WASD.

There is a diagonal cutout on the bottom left, where I can rest my hand more easily.

## Keys

-   Control+Z (undo) and Control+Y (redo)
-   Control+C (copy) and Control+V (paste), the only two keys I need
-   Control+D (duplicate)
-   F2 (rename)
-   Play/pause
-   Push-to-talk
-   `sudo pacman -Syu` (average arch user)

## Schematic

![Schematic](schematic.png)

## PCB

![PCB](pcb.png)

## Case

| Top                         | Bottom                            |
| --------------------------- | --------------------------------- |
| ![Top of case](casetop.png) | ![Bottom of case](casebottom.png) |

Section analysis was a very useful feature

![Section analysis](section.png)

## BOM

### From inventory

-   1 × XIAO-RP2040
-   9 × diode
-   1 × encoder
-   1 × small-screen
-   9 × keycap-white

### Custom components

-   9 × SK6812 MINI-E LED
-   4 × M3×16mm screw
-   4 × M3×5mm×4mm heatset insert
-   9 × Gateron Baby Kangaroo 2.0
