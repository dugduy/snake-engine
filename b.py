from snake import Snake
from random import randint
from time import sleep

mysnake=Snake()
mysnake.print_out()
for i in range(100):
    sleep(1)
    mysnake.move(randint(0,3))
    mysnake.print_out()
    if mysnake.isgameovered:break