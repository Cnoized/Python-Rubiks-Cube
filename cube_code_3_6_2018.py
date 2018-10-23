# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 02:21:47 2018

@author: Cnoized
"""

"cube2 = [[[1]*3]*3,[[2]*3]*3,[[3]*3]*3,[[4]*3]*3,[[5]*3]*3,[[6]*3]*3]"
"import numpy as np"
from tkinter import Tk, Label, Button
"""
class Face:
    def __init__(self, number):
        self.number = number
        self.values = [[number]*3]*3
    
    def __getitem__(self, key):
        return self.values[key]
        
    def RotateL(self):
        tempCube = [list(a) for a in zip(*self.values)][::-1]
        self.values = tempCube
        return self.values
    def RotateR(self):
        tempCube = [list(a) for a in zip(*self.values[::-1])]
        self.values = tempCube
        return self.values
    def NoRotate(self):
        return self.values
    __call__ = NoRotate
    __call__ = RotateR
    __call__ = RotateL
cube = [list(Face(n)) for n in range(6)]
print(cube)
"""
"Possible implementation of face manipulation."
class Cube:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        
        self.cube = [[[n]*3]*3 for n in range(1,7)]
        "Create the data for the cube as 6 faces of 9 values per face."
        self.label = Label(master, text="Rubik's Cube!")
        self.label.pack()

        self.greet_button = Button(master, text="Top CW", command=self.TopLeft)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Top CCW", command=self.TopRight)
        self.greet_button.pack()
        
        self.greet_button = Button(master, text="Bot CW", command=self.BotRight)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Bot CCW", command=self.BotLeft)
        self.greet_button.pack()  

        self.greet_button = Button(master, text="Front CW", command=self.FrontCW)
        self.greet_button.pack()  
              
        self.greet_button = Button(master, text="Front CCW", command=self.FrontCCW)
        self.greet_button.pack()
                
        self.greet_button = Button(master, text="Back CW", command=self.BackCW)
        self.greet_button.pack()  
              
        self.greet_button = Button(master, text="Back CCW", command=self.BackCCW)
        self.greet_button.pack()
        
        self.greet_button = Button(master, text="Left CW", command=self.LeftDown)
        self.greet_button.pack()
                
        self.greet_button = Button(master, text="Left CCW", command=self.LeftUp)
        self.greet_button.pack()
                
        self.greet_button = Button(master, text="Right CW", command=self.RightUp)
        self.greet_button.pack()
                
        self.greet_button = Button(master, text="Right CCW", command=self.RightDown)
        self.greet_button.pack()
        
        self.greet_button = Button(master, text="Shift CW", command=self.CW)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Shift CCW", command=self.CCW)
        self.greet_button.pack()
        
        self.greet_button = Button(master, text="Shift Up", command=self.UP)
        self.greet_button.pack()
                        
        self.greet_button = Button(master, text="Shift Down", command=self.DOWN)
        self.greet_button.pack()
                        
        self.greet_button = Button(master, text="Shift Left", command=self.LEFT)
        self.greet_button.pack()
                                
        self.greet_button = Button(master, text="Shift Right", command=self.RIGHT)
        self.greet_button.pack()
                
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    def __getitem__(self, key):
        return self.cube[key]
    
    def Turn(self):
        tempCube = [[self.cube[(n+1) % 4][0],self.cube[n][1],self.cube[n][2]] if n<4 else [list(a) for a in zip(*self.cube[n][::-1])] if n==4 else self.cube[n] for n in range(6)]
        self.cube = tempCube
    __call__ = Turn
    def Clockwise(self):
        tempCube = [[list(a) for a in zip(*self.cube[n])][::-1] if n==2 else [list(a) for a in zip(*self.cube[n][::-1])] for n in range(6)]
        self.cube = [tempCube[i] for i in [0,4,2,5,3,1]]
    __call__ = Clockwise
    def Forward(self):
        tempCube = [[list(a) for a in zip(*self.cube[n][::-1])] if n==1 else [list(a) for a in zip(*self.cube[n])][::-1] if n==3 else [a[::-1] for a in self.cube[n][::-1]] if n==4 or n==2 else self.cube[n] for n in range(6)]
        self.cube = [tempCube[i] for i in [5,1,4,3,0,2]]
    __call__ = Forward
    
    "Above are the base moves, which every other turn can be derived from."
    
#    def CounterClockwise(self):
#        tempCube = [[list(a) for a in zip(*self.cube[n])][::-1] if n!=2 else [list(a) for a in zip(*self.cube[n][::-1])] for n in range(6)]
#        self.cube = [tempCube[i] for i in [0,5,2,4,1,3]]
#    __call__ = CounterClockwise
    
    "These are extra moves which were derived, but are unnecessary."

    "Main turn method"
    """
    "Turns the top row left."
    def TopRight(self):
        tempCube = [[self.cube[(n-1) % 4][0],self.cube[n][1],self.cube[n][2]] if n<4 else [list(a) for a in zip(*self.cube[n])][::-1] if n==4 else self.cube[n] for n in range(6)]
        self.cube = tempCube
        label = Label(root, text = self.cube)
        label.pack()
        print(self.cube)
    __call__ = TopRight
    "Turns the top row right."
    def BotLeft(self):
        tempCube = [[self.cube[n][0],self.cube[n][1],self.cube[(n+1) % 4][2]] if n<4 else [list(a) for a in zip(*self.cube[n])][::-1] if n==5 else self.cube[n] for n in range(6)]
        self.cube = tempCube
        label = Label(root, text = self.cube)
        label.pack()
        print(self.cube)
    __call__ = BotLeft
    "Turns the bot row left."
    def BotRight(self):
        tempCube = [[self.cube[n][0],self.cube[n][1],self.cube[(n-1) % 4][2]] if n<4 else [list(a) for a in zip(*self.cube[n][::-1])] if n==5 else self.cube[n] for n in range(6)]
        self.cube = tempCube
        label = Label(root, text = self.cube)
        label.pack()
        print(self.cube)
    "Turns the bot row right."
    "These are functional turns, but I have a better itea for implementation."
    """
    def TopLeft(self):
        self.Turn()
        self.CallBack()
    __call__ = TopLeft
    
    def TopRight(self):
        self.Turn()
        self.Turn()
        self.Turn()
        self.CallBack()
    __call__ = TopRight
    
    def BotLeft(self):
        self.Clockwise()
        self.Clockwise()
        self.Turn()
        self.Turn()
        self.Turn()
        self.Clockwise()
        self.Clockwise()
        self.CallBack()
    __call__ = BotLeft
    
    def BotRight(self):
        self.Clockwise()
        self.Clockwise()
        self.Turn()
        self.Clockwise()
        self.Clockwise()
        self.CallBack()
    __call__ = BotRight

    def RightDown(self):
        self.Clockwise()
        self.Clockwise()
        self.Clockwise()
        self.Turn()
        self.Turn()
        self.Turn()
        self.Clockwise()
        self.CallBack()
    __call__ = RightDown
    
    def RightUp(self):
        self.Clockwise()
        self.Clockwise()
        self.Clockwise()
        self.Turn()
        self.Clockwise()
        self.CallBack()
    __call__ = RightUp
    
    def LeftUp(self):
        self.Clockwise()
        self.Turn()
        self.Turn()
        self.Turn()
        self.Clockwise()
        self.Clockwise()
        self.Clockwise()
        self.CallBack()
    __call__ = LeftUp
    
    def LeftDown(self):
        self.Clockwise()
        self.Turn()
        self.Clockwise()
        self.Clockwise()
        self.Clockwise()
        self.CallBack()
    __call__ = LeftDown

    def FrontCW(self):
        self.Forward()
        self.Turn()
        self.Forward()
        self.Forward()
        self.Forward()
        self.CallBack()
    __call__ = FrontCW
    
    def FrontCCW(self):
        self.Forward()
        self.Turn()
        self.Turn()
        self.Turn()
        self.Forward()
        self.Forward()
        self.Forward()
        self.CallBack()
    __call__ = FrontCCW    

    def BackCCW(self):
        self.Forward()
        self.Forward()
        self.Forward()
        self.Turn()
        self.Forward()
        self.CallBack()
    __call__ = BackCCW
    
    def BackCW(self):
        self.Forward()
        self.Forward()
        self.Forward()
        self.Turn()
        self.Turn()
        self.Turn()
        self.Forward()
        self.CallBack()
    __call__ = BackCW    

    def UP(self):
        self.Forward()
        self.CallBack()
    __call__ = UP
    
    def DOWN(self):
        self.Forward()
        self.Forward()
        self.Forward()
        self.CallBack()
    __call__ = DOWN
    
    def CW(self):
        self.Clockwise()
        self.CallBack()
    __call__ = CW
    
    def CCW(self):
        self.Clockwise()
        self.Clockwise()
        self.Clockwise()
        self.CallBack()
    __call__ = CCW

    def LEFT(self):
        self.Clockwise()
        self.Clockwise()
        self.Clockwise()
        self.Forward()
        self.Clockwise()
        self.CallBack()
    __call__ = LEFT  
    
    def RIGHT(self):
        self.Clockwise()
        self.Forward()
        self.Clockwise()
        self.Clockwise()
        self.Clockwise()
        self.CallBack()
    __call__ = RIGHT
    
    "The above functions give you the ability to rotate the cube as well as each of the sides. Giving 18 different ways to change the cube's composition."
    
    def CallBack(self):
        label = Label(root, text = self.cube)
        label.pack()
        print(self.cube)
    __call__ = CallBack
""" These methods currently only move rows in the arrays, and don't move individual values. Speculating something is wrong with my implmentation of the zip() function."""
"""def LeftUp(self):
        tempCube1 = [self.cube[n] if n==1 else if n==2 else if n==3 else if n==4 else if n==5 for n in range(6)]
        tempCube2 = """


root = Tk()
my_gui = Cube(root)

root.mainloop()
"Actually presents the GUI."
"print([list(a) for a in zip(cube2)])"