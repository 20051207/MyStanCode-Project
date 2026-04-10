"""
File: StepUp.py
Name: Ziv Liu
------------------------
This program demonstrates how Karel picks up a beeper
at Street 1 Avenue 2 and moves it to Street 2 Avenue 4.

By guiding Karel step by step, we will practice writing
clear and well-structured commands. At the end of the
program, Karel will be facing East at Street 2 Avenue 5.
"""

from karel.stanfordkarel import *


def main():
    pass
    move()
    pick_beeper()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    put_99()
    move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def put_99():
    for i in range(99):
        put_beeper()
# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
