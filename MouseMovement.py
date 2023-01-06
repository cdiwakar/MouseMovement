from re import X
import pyautogui
from time import sleep
from random import randint
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

w,h=pyautogui.size()
#Function to get Random position
def getNextPos():
    x=randint(0,w-1)
    y=randint(0,h-1)
    print(x,y)
    #w=x
    #h=y
    sleep(1)
    return x,y
#Function to Move mouse
def move():
    x,y=getNextPos()
    print("Moving to ({},{})".format(x, y))
    pyautogui.moveTo(x,y,duration=0.25)
    sleep(1)
print("Press CTRL-C to Stop")
while True:
    move()


