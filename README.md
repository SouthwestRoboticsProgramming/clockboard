uses a pi pico w for controlling leds and a pi zero 2 w for interfacing.

leds are now connected to pico in a matrix.

for leds:
Columns are negative, rows are positive
GPIO:
row 1: 0
row 2: 1
row 3: 2
row 4: 3
row 5: 4
row 6: 5

column 1: 6
column 2: 7
column 3: 8
column 4: 9
column 5: 10



for buttons:

GPIO:
row 1: 2
row 2: 3
row 3: 4
row 4: 17
row 5: 27
row 6: 22

column 1: 26
column 2: 19
column 3: 13
column 4: 6
column 5: 5



## !! DOES NOT CURRENTLY WORK !! ##

Will also have to rewire buttons into a matrix and rewrite main.py for that (hopefully can stay in python because c++ as a debian service sounds terrible)

Also Also have to implement led logic on pi zero 2 w (could probably roll all of this into main.py)