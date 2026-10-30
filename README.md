# Endless racing game for microbit
A game for the BBC micro:bit. You control the car on the bottom row, and dodge the incomming obstacles from the top. The longer you survive the faster the obstacles fall. All displayed on the microbits LED display.

### Requirements
    - BBC micro:bit v2 (requires v2 for built in speaker and touch sensor).
    - An alternative to a micro:bit v2 is a microbit emulator (https://python.microbit.org/v/3).

### How to play
|Input                              |Action                             |
|Touch the logo to start the game   |Starts or resets the game          |
|Button A                           |Move player left                   |
|Button B                           |Move player right                  |

    - The car wraps around the edges, going past far left column puts you at far right and vice versa.
    - Obstacles are lit pixels which approach the player from the top of the screen.
    - When you die, a skull lit up and a noise played, indicated that you have collided with an obstacle.

### Difficulty
    - The game starts at one tick (obstacle spawns every tick, obstacle moves towards you every tick) is 750ms.
    - Tick speed increases by 50ms every 10 seconds, capping at a max tick speed of 400ms/tick (taking 70 seconds to reach max difficulty, weird number I know).
    - Tick speed resets at the start of every game.

### How it works
    - count_tick() fires once every {speed} milliseconds, the result is stored in {count_tick_store}. This creates the global tick timing, so obstacles move and spawn in sync
    - The obstacles are spawned by 5 functions (spawn_obstacle0() - spawn_obstacle4()), one for each of the max 5 obstacles on the screen at a time. These functions handle spawning, moving and clearing the obstacle pixels.
    - When an obstacle reaches row 4 (bottom row), it sets a variable called obstacle_kill to the x value of the obstacle which reached the bottom. Obstacle_kill only stays active on one pixel at a time, as each of the 5 spawn_obstacleX() functions uses the same obstacle_kill value.
    - The start_menu() function is run at the start of the game, and after reset(). The function start_game(), contains and runs the other functions, and is responsible for handling movement input. Start_game() is run in the game loop, which was kept as clean as possible, containing only the start_game() function.

### For the future
    - In the future, I intend to make a changes and improvements which I didn't have time to add to this version.
    - A single note of the music for each game tick, the music speeding up with the game.
    - Better sound queues, like on button presses, speed ups and movement. 
    - Multiple game modes such as easy mode, hard mode, full row with a gap or timed rather than endless
    - Score counter, displaying score after death

### Last words
Hi anyone reading this! Thanks for taking the time to look at my project. This game was made by ZeepT.

Credit to BBC and the Micro:bit Educational Foundation for the micro:bit v2, music sourced from the microbit "music" import module.