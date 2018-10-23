# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 02:21:47 2018

@author: Cnoized
"""

cube2 = [[[1]*3]*3,[[2]*3]*3,[[3]*3]*3,[[4]*3]*3,[[5]*3]*3,[[6]*3]*3]
import numpy as np
from tkinter import Tk, Label, Button
"""
class Face:
    def __init__(self, number):
        self.number = number
        self.values = [[number]*3]*3
    
    def __getitem__(self, key):
        return self.values[key]
        
    def RotateL(self):
        tempCube = [list(a) for sublist in zip(self.values) for a in sublist][::-1]
        self.values = tempCube
        return self.values
    def RotateR(self):
        tempCube = [list(a) for sublist in zip(self.values[::-1]) for a in sublist]
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

        self.greet_button = Button(master, text="Top Left", command=self.TopLeft)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Top Right", command=self.TopRight)
        self.greet_button.pack()
        
        self.greet_button = Button(master, text="Bot Left", command=self.BotLeft)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Bot Right", command=self.BotRight)
        self.greet_button.pack()  
        
        self.greet_button = Button(master, text="Clockwise", command=self.Clockwise)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Counterclockwise", command=self.Counter)
        self.greet_button.pack()
        
        self.greet_button = Button(master, text="Forward", command=self.Forward)
        self.greet_button.pack()
                
        self.greet_button = Button(master, text="Front Clockwise", command=self.FrontCW)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    def __getitem__(self, key):
        return self.cube[key]
    
    def TopLeft(self):
        tempCube = [[self.cube[(n+1) % 4][0],self.cube[n][1],self.cube[n][2]] if n<4 else [list(a) for sublist in zip(self.cube[n]) for a in sublist][::-1] if n==4 else self.cube[n] for n in range(6)]
        self.cube = tempCube
        print(self.cube)
    __call__ = TopLeft
    "Turns the top row left."
    def TopRight(self):
        tempCube = [[self.cube[(n-1) % 4][0],self.cube[n][1],self.cube[n][2]] if n<4 else [list(a) for sublist in zip(self.cube[n][::-1]) for a in sublist] if n==4 else self.cube[n] for n in range(6)]
        self.cube = tempCube
        print(self.cube)
    __call__ = TopRight
    "Turns the top row right."
    def BotLeft(self):
        tempCube = [[self.cube[n][0],self.cube[n][1],self.cube[(n+1) % 4][2]] if n<4 else [list(a) for sublist in zip(self.cube[n]) for a in sublist][::-1] if n==5 else self.cube[n] for n in range(6)]
        self.cube = tempCube
        print(self.cube)
    __call__ = BotLeft
    "Turns the bot row left."
    def BotRight(self):
        tempCube = [[self.cube[n][0],self.cube[n][1],self.cube[(n-1) % 4][2]] if n<4 else [list(a) for sublist in zip(self.cube[n][::-1]) for a in sublist] if n==5 else self.cube[n] for n in range(6)]
        self.cube = tempCube
        print(self.cube)
    "Turns the bot row right."
    def Clockwise(self):
        tempCube = [[list(a) for sublist in zip(self.cube[n]) for a in sublist][::-1] if n==2 else [list(a) for sublist in zip(self.cube[n][::-1]) for a in sublist] for n in range(6)]
        self.cube = [tempCube[i] for i in [0,4,2,5,3,1]]
        print(self.cube)
    __call__ = Clockwise
    def Counter(self):
        tempCube = [[list(a) for sublist in zip(self.cube[n]) for a in sublist][::-1] if n!=2 else [list(a) for sublist in zip(self.cube[n][::-1]) for a in sublist] for n in range(6)]
        self.cube = [tempCube[i] for i in [0,5,2,4,1,3]]
        print(self.cube)
    __call__ = Counter
    def Forward(self):
        tempCube = [[list(a) for sublist in zip(self.cube[n]) for a in sublist][::-1] if n==1 else [list(a) for sublist in zip(self.cube[n][::-1]) for a in sublist] if n==3 else self.cube[n][::-1][::-1] if n==4 or n==2 else self.cube[n] for n in range(6)]
        self.cube = [tempCube[i] for i in [5,1,4,3,0,2]]
        print(self.cube)
    __call__ = Forward
    def FrontCW(self):
        self.Forward()
        self.TopLeft()
        self.Forward()
        self.Forward()
        self.Forward()
        print(self.cube)
    __call__ = FrontCW
""" These methods currently only move rows in the arrays, and don't move individual values. Speculating something is wrong with my implmentation of the zip() function."""
"""def LeftUp(self):
        tempCube1 = [self.cube[n] if n==1 else if n==2 else if n==3 else if n==4 else if n==5 for n in range(6)]
        tempCube2 = """


root = Tk()
my_gui = Cube(root)

root.mainloop()
"Actually presents the GUI."
