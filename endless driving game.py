import microbit
import random

pos = 2

def start_game():
    show_player()

    if microbit.button_a.was_pressed():
        move_left()

    if microbit.button_b.was_pressed():
        move_right()

def move_left():
    pos = pos - 1
    if pos < 0:
        pos = 5

def move_right():
    pos = pos + 1
    if pos > 5:
        pos = 0

def show_player():
    
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

