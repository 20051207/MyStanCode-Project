"""
File: Steeplechase.py
Name: Ziv Liu
---------------------------------
Ziv Liu
"""

from karel.stanfordkarel import *

def jump():
    up()
    down()

def up():
    """
    Pre condition:east
    Post condition:north
    make sure it face the same direction,
    so that the while loop will function well
    """
    while not front_is_clear():
        #east
        turn_left()
        move()
        #north
        turn_right()
    move()
    turn_right()
def down():
    """
    Pre condition:Up
    Post condition:Down
    """
    while front_is_clear():
        move()
    turn_left()
def turn_right():
    for i in range(3):
        turn_left()

def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        #east
        if front_is_clear():
            move()
        else:
            jump()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
