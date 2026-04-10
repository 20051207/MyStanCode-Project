"""
File: PotholeFilling.py
Name: Ziv Liu
--------------------------
This program demonstrates how Karel fills multiple potholes
by using decomposition.

In this program, we will guide Karel to fix three potholes
on the road. Instead of writing all the commands in one place,
we will practice breaking a big task into smaller, reusable
functions to make the program clearer and easier to manage.
"""

from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def put_99():
    for i in range(99):
        put_beeper()
def main():
    """
    pre condition :(2,1) east
    post condition:
    """
    pass
    for i in range(3):
        move()
        turn_right()
        move()
        put_99()
        turn_left()
        turn_left()
        move()
        turn_right()
        move()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
