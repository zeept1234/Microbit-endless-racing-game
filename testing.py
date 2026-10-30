import microbit, random, music

pos = 2
started = False
obstacle_kill = -1
obstacle_y = [-1,-1,-1,-1,-1]
obstacle_x = [-1,-1,-1,-1,-1]
obstacle_timer = [0,0,0,0,0]
previous_pixel = 0
obstacle_count = 0
tick = microbit.running_time()
tick_step = 750
tick_set = False
switch = [0,0,0,0,0]
first_sleep = False
count_tick_store = False

def start_game(): #Starts other functions
    set_tick_start()
    show_player()
    kill_check()
    continuous_spawn()
    obstacle_switch()
    store_count_tick()

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
    global started, pos, obstacle_kill, obstacle_y, obstacle_x, obstacle_timer, previous_pixel, obstacle_count, tick, tick_step, tick_set, first_sleep, switch, count_tick_store
    pos = 2
    started = False
    obstacle_kill = -1
    obstacle_y = [-1,-1,-1,-1,-1]
    obstacle_x = [-1,-1,-1,-1,-1]
    obstacle_timer = [0,0,0,0,0]
    previous_pixel = 0
    obstacle_count = 0
    tick = microbit.running_time()
    tick_step = 750
    tick_set = False
    first_sleep = False
    switch = [0,0,0,0,0]
    count_tick_store = False
    start_menu()

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
        kill_timer = microbit.running_time()
        
    elif count_tick_store == True:
        microbit.display.set_pixel(obstacle_x[0], obstacle_y[0], 0)
        obstacle_y[0] = obstacle_y[0] + 1

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
        
    elif count_tick_store == True:
        microbit.display.set_pixel(obstacle_x[1], obstacle_y[1], 0)
        obstacle_y[1] = obstacle_y[1] + 1

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
        
    elif count_tick_store == True:
        microbit.display.set_pixel(obstacle_x[2], obstacle_y[2], 0)
        obstacle_y[2] = obstacle_y[2] + 1
        obstacle_timer[2] = microbit.running_time()

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
        
    elif count_tick_store == True:
        microbit.display.set_pixel(obstacle_x[3], obstacle_y[3], 0)
        obstacle_y[3] = obstacle_y[3] + 1
        obstacle_timer[3] = microbit.running_time()

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
        
    elif count_tick_store == True:
        microbit.display.set_pixel(obstacle_x[4], obstacle_y[4], 0)
        obstacle_y[4] = obstacle_y[4] + 1
        obstacle_timer[4] = microbit.running_time()

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
    microbit.sleep(2000)
    reset()

def continuous_spawn(): #Spawns up to 5 objects using a counter
    global obstacle_count, obstacle_functions, first_sleep
    
    if obstacle_count > 4:
        pass

    elif count_tick_store == True:
        switch[obstacle_count] = 1
        obstacle_count = obstacle_count + 1

def obstacle_switch():
    global switch
    if switch[0] == 1:
        spawn_obstacle0()
    if switch[1] == 1:
        spawn_obstacle1()
    if switch[2] == 1:
        spawn_obstacle2()
    if switch[3] == 1:
        spawn_obstacle3()
    if switch[4] == 1:
        spawn_obstacle4()

def count_tick():
    global tick, tick_step
    if microbit.running_time() >= tick + tick_step:
        tick_step = tick_step + 750
        return True
    else:
        return False

def store_count_tick():
    global count_tick_store
    count_tick_store = count_tick()

def set_tick_start():
    global tick, tick_set
    if tick_set == False:
        tick = microbit.running_time()
        tick_set = True


start_menu()

while started == True:
    start_game()