import microbit
import random

pos = 2
exit_loop = 0

def start_game(): #Shows player, enables movement
    microbit.display.scroll("", wait = False)
    show_player()

    if microbit.button_a.was_pressed():
        move_left()

    if microbit.button_b.was_pressed():
        move_right()

    if pin_logo.is_touched():
        reset()

def move_left(): #Moves left
    pos = pos - 1
    if pos < 0:
        pos = 5

def move_right(): #Moves right
    pos = pos + 1
    if pos > 5:
        pos = 0

def show_player(): #Displays player location according to {pos}
    
    if pos == 0:
        microbit.display.set_pixel(0,4,9)
        microbit.display.set_pixel(1,4,0)
        microbit.display.set_pixel(2,4,0)
        microbit.display.set_pixel(3,4,0)
        microbit.display.set_pixel(4,4,0)
        
    if pos == 1:
        microbit.display.set_pixel(1,4,9)
        microbit.display.set_pixel(0,4,0)
        microbit.display.set_pixel(2,4,0)
        microbit.display.set_pixel(3,4,0)
        microbit.display.set_pixel(4,4,0)
        
    if pos == 2:
        microbit.display.set_pixel(2,4,9)
        microbit.display.set_pixel(1,4,0)
        microbit.microbit.display.set_pixel(0,4,0)
        microbit.display.set_pixel(3,4,0)
        microbit.display.set_pixel(4,4,0)
        
    if pos == 3:
        microbit.display.set_pixel(3,4,9)
        microbit.display.set_pixel(1,4,0)
        microbit.display.set_pixel(2,4,0)
        microbit.display.set_pixel(0,4,0)
        microbit.display.set_pixel(4,4,0)
        
    if pos == 4:
        microbit.display.set_pixel(4,4,9)
        microbit.display.set_pixel(1,4,0)
        microbit.display.set_pixel(2,4,0)
        microbit.display.set_pixel(3,4,0)
        microbit.display.set_pixel(0,4,0)

def reset(): #Exits loop and displays start screen
    global exit_loop
    exit_loop = 1
    start()

def start():
    microbit.display.scroll("Car game: Press touch sensor to start!", wait = False)

while True:
    if pin_logo.is_touched():
        reset()

    if exit_loop == 1:
        break

start_game()