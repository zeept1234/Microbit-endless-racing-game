import microbit, random, music

pos = 2
exit_loop = False
started = False
obstacle_kill = -1
obstacle_y = [-1,-1,-1,-1,-1]
obstacle_x = [-1,-1,-1,-1,-1]
obstacle_timer = 0
previous_pixel = 0
obstacle_count = 0

def start_game(): #Starts other functions
    show_player()
    spawn_obstacle0()
    kill_check()

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

def start_menu(): #Displays start menu, touch sensor triggers while loop
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

def spawn_obstacle0(): #Spawns obstacles which move closer every 750ms
    global obstacle_x, obstacle_y, obstacle_timer, obstacle_kill, kill_timer
    if obstacle_y[0] == -1:
        obstacle_x[0] = random.randint(0,4)
        obstacle_y[0] = 0
        microbit.display.set_pixel(obstacle_x[0], obstacle_y[0], 9)
        obstacle_timer = microbit.running_time()
        kill_timer = microbit.running_time()
        
    elif microbit.running_time() >= obstacle_timer + 750:
        microbit.display.set_pixel(obstacle_x[0], obstacle_y[0], 0)
        obstacle_y[0] = obstacle_y[0] + 1
        obstacle_timer = microbit.running_time()

    if obstacle_y[0] > 4:
        obstacle_y[0] = -1
    else:
        microbit.display.set_pixel(obstacle_x[0], obstacle_y[0], 9)
        if obstacle_y[0] == 4:
            obstacle_kill = obstacle_x[0]

def spawn_obstacle1(): #Spawns obstacles which move closer every 750ms
    global obstacle_x, obstacle_y, obstacle_timer, obstacle_kill
    if obstacle_y[1] == -1:
        obstacle_x[1] = random.randint(0,4)
        obstacle_y[1] = 0
        microbit.display.set_pixel(obstacle_x[1], obstacle_y[1], 9)
        obstacle_timer = microbit.running_time()
        kill_timer = microbit.running_time()
        
    elif microbit.running_time() >= obstacle_timer + 750:
        microbit.display.set_pixel(obstacle_x[1], obstacle_y[1], 0)
        obstacle_y[1] = obstacle_y[1] + 1
        obstacle_timer = microbit.running_time()

    if obstacle_y[1] > 4:
        obstacle_y[1] = -1
    else:
        microbit.display.set_pixel(obstacle_x[1], obstacle_y[1], 9)
        if obstacle_y[1] == 4:
            obstacle_kill = obstacle_x[1]

def spawn_obstacle2(): #Spawns obstacles which move closer every 750ms
    global obstacle_spwan, obstacle_y, obstacle_timer, obstacle_x, obstacle_kill
    if obstacle_y[2] == -1:
        obstacle_x[2] = random.randint(0,4)
        obstacle_y[2] = 0
        microbit.display.set_pixel(obstacle_x[2], obstacle_y[2], 9)
        obstacle_timer = microbit.running_time()
        kill_timer = microbit.running_time()
        
    elif microbit.running_time() >= obstacle_timer + 750:
        microbit.display.set_pixel(obstacle_x[2], obstacle_y[2], 0)
        obstacle_y[2] = obstacle_y[2] + 1
        obstacle_timer = microbit.running_time()

    if obstacle_y[2] > 4:
        obstacle_y[2] = -1
    else:
        microbit.display.set_pixel(obstacle_x[2], obstacle_y[2], 9)
        if obstacle_y[2] == 4:
            obstacle_kill = obstacle_x[2]

def spawn_obstacle3(): #Spawns obstacles which move closer every 750ms
    global obstacle_spwan, obstacle_y, obstacle_timer, obstacle_x, obstacle_kill
    if obstacle_y[3] == -1:
        obstacle_x[3] = random.randint(0,4)
        obstacle_y[3] = 0
        microbit.display.set_pixel(obstacle_x[3], obstacle_y[3], 9)
        obstacle_timer = microbit.running_time()
        kill_timer = microbit.running_time()
        
    elif microbit.running_time() >= obstacle_timer + 750:
        microbit.display.set_pixel(obstacle_x[3], obstacle_y[3], 0)
        obstacle_y[3] = obstacle_y[3] + 1
        obstacle_timer = microbit.running_time()

    if obstacle_y[3] > 4:
        obstacle_y[3] = -1
    else:
        microbit.display.set_pixel(obstacle_x[3], obstacle_y[3], 9)
        if obstacle_y[3] == 4:
            obstacle_kill = obstacle_x[3]

def spawn_obstacle4(): #Spawns obstacles which move closer every 750ms
    global obstacle_spwan, obstacle_y, obstacle_timer, obstacle_x, obstacle_kill
    if obstacle_y[4] == -1:
        obstacle_x[4] = random.randint(0,4)
        obstacle_y[4] = 0
        microbit.display.set_pixel(obstacle_x[4], obstacle_y[4], 9)
        obstacle_timer = microbit.running_time()
        kill_timer = microbit.running_time()
        
    elif microbit.running_time() >= obstacle_timer + 750:
        microbit.display.set_pixel(obstacle_x[4], obstacle_y[4], 0)
        obstacle_y[4] = obstacle_y[4] + 1
        obstacle_timer = microbit.running_time()

    if obstacle_y[4] > 4:
        obstacle_y[4] = -1
    else:
        microbit.display.set_pixel(obstacle_x[4], obstacle_y[4], 9)
        if obstacle_y[4] == 4:
            obstacle_kill = obstacle_x[4]
  
obstacle_functions = [spawn_obstacle0, spawn_obstacle1, spawn_obstacle2, spawn_obstacle3, spawn_obstacle4]

def kill_check(): #Checks if the obstacle kills the player
    global obstacle_kill
    if pos == obstacle_kill:
        kill()

def kill(): #Displays death screen
    microbit.display.show(microbit.Image.SKULL)
    music.play(music.POWER_DOWN)
    microbit.sleep(3000)
    reset()

def continuous_spawn(): #Spawns up to 5 objects using a counter
    global obstacle_count, obstacle_functions
    if obstacle_count > 4:
        obstacle_count = 0
    
    obstacle_functions[obstacle_count]()
    obstacle_count = obstacle_count + 1

    if microbit.running_time() >= obstacle_timer + 750:
        obstacle_functions[obstacle_count]()
        obstacle_count = obstacle_count + 1


    


start_menu()

while started == True:
    start_game()

    if exit_loop == True:
        break
        

