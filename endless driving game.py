import microbit
import random

pos = 2
exit_loop = False
started = False

def start_game(): #Shows player, enables movement
    show_player()

    if microbit.button_a.was_pressed():
        move_left()

    if microbit.button_b.was_pressed():
        move_right()

    if microbit.pin_logo.is_touched():
        reset()

def move_left(): #Moves left
    global pos
    pos = pos - 1
    if pos < 0:
        pos = 4

def move_right(): #Moves right
    global pos
    pos = pos + 1
    if pos > 4:
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
        microbit.display.set_pixel(0,4,0)
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
    microbit.sleep(200)
    global exit_loop
    global started
    global pos
    pos = 2
    exit_loop = True
    started = False
    start_menu()
    exit_loop = False

def start_menu():
    global started
    microbit.display.scroll("Car game: Press touch sensor to start!", wait = False) #40 seconds to finish scrolling
    start_time = microbit.running_time()

    while not started:
        if microbit.pin_logo.is_touched():
            microbit.sleep(200)
            started = True
            microbit.display.scroll("", wait = False)
        if microbit.running_time() >= start_time + 40000:
            microbit.sleep(200)
            started = True
            microbit.display.scroll("", wait = False)

start_menu()

while started == True:
    start_game()

    if exit_loop == True:
        break
        

