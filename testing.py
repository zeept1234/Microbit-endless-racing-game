import microbit, random, music

pos = 2
exit_loop = False
started = False
obstacle_kill = -1
obstacle_y = -1
obstacle_x = -1
obstacle_timer = 0
previous_pixel = 0

def start_game(): #Starts other functions
    show_player()
    continuos_spawn()
    kill_check()
    kill_timer_check()

    if microbit.button_a.was_pressed():
        move_left()

    if microbit.button_b.was_pressed():
        move_right()

    if microbit.pin_logo.is_touched():
        reset()

def move_left(): #Moves left
    global pos, previous_pixel
    microbit.display.set_pixel(previous_pixel,4,0)
    pos = pos - 1
    
    if pos < 0:
        pos = 4

def move_right(): #Moves right
    global pos, previous_pixel
    microbit.display.set_pixel(previous_pixel,4,0)
    pos = pos + 1
    if pos > 4:
        pos = 0

def show_player(): #Displays player location according to {pos}
    global previous_pixel
    if pos == 0:
        microbit.display.set_pixel(0,4,9)
        previous_pixel = 0
    if pos == 1:
        microbit.display.set_pixel(1,4,9)
        previous_pixel = 1
        
    if pos == 2:
        microbit.display.set_pixel(2,4,9)
        previous_pixel = 2
        
    if pos == 3:
        microbit.display.set_pixel(3,4,9)
        previous_pixel = 3
        
    if pos == 4:
        microbit.display.set_pixel(4,4,9)
        previous_pixel = 4

def reset(): #Exits loop and displays start screen
    microbit.sleep(200)
    global exit_loop, started, pos, obstacle_kill, obstacle_y, obstacle_x, obstacle_timer
    global started
    global pos
    pos = 2
    obstacle_kill = -1
    obstacle_y = -1
    obstacle_x = -1
    obstacle_timer = 0
    exit_loop = True
    started = False
    start_menu()
    exit_loop = False

def start_menu():
    global started
    microbit.display.scroll("Car game: Press touch sensor to start!", wait = False) #41 seconds to finish scrolling
    start_time = microbit.running_time()

    while not started:
        if microbit.pin_logo.is_touched():
            microbit.sleep(200)
            started = True
            microbit.display.scroll("", wait = False)
        if microbit.running_time() >= start_time + 41000:
            microbit.sleep(200)
            started = True
            microbit.display.scroll("", wait = False)

def spawn_obstacle(): #Spawns obstacles which move closer every 750ms
    global obstacle_spwan, obstacle_y, obstacle_timer, obstacle_x, obstacle_kill, kill_timer
    if obstacle_y == -1:
        obstacle_x = random.randint(0,4)
        obstacle_y = 0
        microbit.display.set_pixel(obstacle_x, obstacle_y, 9)
        obstacle_timer = microbit.running_time()
        kill_timer = microbit.running_time()
        
    elif microbit.running_time() >= obstacle_timer + 750:
        microbit.display.set_pixel(obstacle_x, obstacle_y, 0)
        obstacle_y = obstacle_y + 1
        obstacle_timer = microbit.running_time()

    if obstacle_y > 4:
        obstacle_y = -1
    else:
        microbit.display.set_pixel(obstacle_x, obstacle_y, 9)
        if obstacle_y == 4:
            obstacle_kill = obstacle_x

def kill_check(): #Checks if the obstacle kills the player
    global obstacle_kill
    if pos == obstacle_kill:
        kill()

def kill():
    microbit.display.show(microbit.Image.SKULL)
    music.play(music.POWER_DOWN)
    microbit.sleep(3000)
    reset()

def continuos_spawn():
    global continuos_spawn
    spawn_obstacle()
    continuos_spawn_timer = microbit.running_time()

    if microbit.running_time() >= continuos_spawn_timer + 750:
        spawn_obstacle()
        continuos_spawn_timer = microbit.running_time()

def kill_timer_check():  #Checks to remove obstacle (remove after multiple obstacle spawn added)
    global kill_timer, obstacle_kill
    if microbit.running_time() >= kill_timer + 1:
        obstacle_kill = -4500

start_menu()

while started == True:
    start_game()

    if exit_loop == True:
        break
        

