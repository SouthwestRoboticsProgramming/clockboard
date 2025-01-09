uses a pi pico w for controlling leds and a pi zero 2 w for interfacing.

leds are now connected to pico in a matrix.

for leds:

GPIO 0-5 are the rows top to bottom
GPIO6-10 are the columns left to right
Columns are negative, rows are positive

for buttons:

tbd


## !! DOES NOT CURRENTLY WORK !! ##

Will also have to rewire buttons into a matrix and rewrite main.py for that (hopefully can stay in python because c++ as a debian service sounds terrible)

Also Also have to implement led logic on pi zero 2 w (could probably roll all of this into main.py)