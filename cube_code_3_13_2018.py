# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 02:21:47 2018

@author: Cnoized
"""

from tkinter import *
import random

#class Face:
#    def __init__(self, number):
#        self.number = number
#        self.values = [[number]*3]*3
#    
#    def __getitem__(self, key):
#        return self.values[key]
#        
#    def RotateL(self):
#        tempCube = [list(a) for a in zip(*self.values)][::-1]
#        self.values = tempCube
#        return self.values
#    def RotateR(self):
#        tempCube = [list(a) for a in zip(*self.values[::-1])]
#        self.values = tempCube
#        return self.values
#    def NoRotate(self):
#        return self.values
#    __call__ = NoRotate
#    __call__ = RotateR
#    __call__ = RotateL
#cube = [list(Face(n)) for n in range(6)]
#print(cube)

"Possible implementation of face manipulation."
class Cube:
    def __init__(self, master):
        self.master = master
        master.title("Rubik's Cube!")
        self.supress = True
        self.cube = [[[n]*3]*3 for n in range(1,7)]
        self.row = [4,4,4,4,1,7]
        self.column = [9,12,15,6,9,9]
        self.correct = 0
        self.cCube = [[[0]*3]*3 for n in range(6)]
        
        "Create the data for the cube as a 6 by 3 by 3 multidimentional array."
        self.label = Label(master, text="Side Rotations")
        self.label.grid(sticky=N+S+E+W, row=0,column=0,columnspan=2)

        self.label = Label(master, text="Cube Rotations")
        self.label.grid(sticky=N+S+E+W, row=0,column=2,columnspan=2)
        
        self.button = Button(master, text="Top CW", command=self.TopLeft)
        self.button.grid(sticky=N+S+E+W, row=1,column=0,ipadx=7)

        self.button = Button(master, text="Top CCW", command=self.TopRight)
        self.button.grid(sticky=N+S+E+W, row=1,column=1)
        
        self.button = Button(master, text="Bot CW", command=self.BotRight)
        self.button.grid(sticky=N+S+E+W, row=2,column=0)

        self.button = Button(master, text="Bot CCW", command=self.BotLeft)
        self.button.grid(sticky=N+S+E+W, row=2,column=1)  

        self.button = Button(master, text="Front CW", command=self.FrontCW)
        self.button.grid(sticky=N+S+E+W, row=3,column=0)  
              
        self.button = Button(master, text="Front CCW", command=self.FrontCCW)
        self.button.grid(sticky=N+S+E+W, row=3,column=1)
                
        self.button = Button(master, text="Back CW", command=self.BackCW)
        self.button.grid(sticky=N+S+E+W, row=4,column=0)  
              
        self.button = Button(master, text="Back CCW", command=self.BackCCW)
        self.button.grid(sticky=N+S+E+W, row=4,column=1)
        
        self.button = Button(master, text="Left CW", command=self.LeftDown)
        self.button.grid(sticky=N+S+E+W, row=5,column=0)
                
        self.button = Button(master, text="Left CCW", command=self.LeftUp)
        self.button.grid(sticky=N+S+E+W, row=5,column=1)
                
        self.button = Button(master, text="Right CW", command=self.RightUp)
        self.button.grid(sticky=N+S+E+W, row=6,column=0)
                
        self.button = Button(master, text="Right CCW", command=self.RightDown)
        self.button.grid(sticky=N+S+E+W, row=6,column=1)
        
        self.button = Button(master, text="Shift CW", command=self.CW)
        self.button.grid(sticky=N+S+E+W, row=1,column=2,ipadx=7)

        self.button = Button(master, text="Shift CCW", command=self.CCW)
        self.button.grid(sticky=N+S+E+W, row=1,column=3)
        
        self.button = Button(master, text="Shift Up", command=self.UP)
        self.button.grid(sticky=N+S+E+W, row=2,column=2)
                        
        self.button = Button(master, text="Shift Down", command=self.DOWN)
        self.button.grid(sticky=N+S+E+W, row=2,column=3)
                        
        self.button = Button(master, text="Shift Left", command=self.LEFT)
        self.button.grid(sticky=N+S+E+W, row=3,column=2)
                                
        self.button = Button(master, text="Shift Right", command=self.RIGHT)
        self.button.grid(sticky=N+S+E+W, row=3,column=3)

        self.button = Button(master, text="Rand Turn", command=self.Random)
        self.button.grid(sticky=N+S+E+W, row=5,column=2)
                                
        self.button = Button(master, text="20 Turns", command=self.Turn20)
        self.button.grid(sticky=N+S+E+W, row=5,column=3)
    
        self.button = Button(master, text="Supress", command=self.Supress)
        self.button.grid(sticky=N+S+E+W, row=8,column=0)

        self.button = Button(master, text="UnSup", command=self.UnSupress)
        self.button.grid(sticky=N+S+E+W, row=8,column=1)
        
        self.label = Label(master, text="Console Output")
        self.label.grid(sticky=N+S+E+W, row=7,column=0,columnspan=2)
        
        self.label = Label(master, text="www.Cnoized.com")
        self.label.grid(sticky=N+S+E+W, row=9,column=0,columnspan=2)
        
        self.close_button = Button(master, text="Close", command=root.destroy)
        self.close_button.grid(sticky=N+S+E+W, row=7,column=2,columnspan=3,padx=30)
        
        self.CallBack()
    "Setting up all the buttons and text for the Tkinter plugin."
    def __getitem__(self, key):
        return self.cube[key]
#    def close(self):
#        self.destroy()
    def Supress(self):
        self.supress=True
    def UnSupress(self):
        self.supress=False
#    
    def Turn(self):
        tempCube = [[self.cube[(n+1) % 4][0],self.cube[n][1],self.cube[n][2]] if n<4 else [list(a) for a in zip(*self.cube[n][::-1])] if n==4 else self.cube[n] for n in range(6)]
        self.cube = tempCube
    __call__ = Turn
    "Main turn method"
    def Clockwise(self):
        tempCube = [[list(a) for a in zip(*self.cube[n])][::-1] if n==2 else [list(a) for a in zip(*self.cube[n][::-1])] for n in range(6)]
        self.cube = [tempCube[i] for i in [0,4,2,5,3,1]]
    __call__ = Clockwise
    def Forward(self):
        tempCube = [[list(a) for a in zip(*self.cube[n][::-1])] if n==1 else [list(a) for a in zip(*self.cube[n])][::-1] if n==3 else [a[::-1] for a in self.cube[n][::-1]] if n==4 or n==2 else self.cube[n] for n in range(6)]
        self.cube = [tempCube[i] for i in [5,1,4,3,0,2]]
    __call__ = Forward
    
    "Above are the base moves, which every other turn can be derived from. This portion of the code does the heavy lifting as far as calculations go."
    
#    def CounterClockwise(self):
#        tempCube = [[list(a) for a in zip(*self.cube[n])][::-1] if n!=2 else [list(a) for a in zip(*self.cube[n][::-1])] for n in range(6)]
#        self.cube = [tempCube[i] for i in [0,5,2,4,1,3]]
#    __call__ = CounterClockwise
#    "Rotates entire cube counterclockwise."
#    def TopRight(self):
#        tempCube = [[self.cube[(n-1) % 4][0],self.cube[n][1],self.cube[n][2]] if n<4 else [list(a) for a in zip(*self.cube[n])][::-1] if n==4 else self.cube[n] for n in range(6)]
#        self.cube = tempCube
#        label = Label(root, text = self.cube)
#        label.pack()
#        print(self.cube)
#    __call__ = TopRight
#    "Turns the top row right."
#    def BotLeft(self):
#        tempCube = [[self.cube[n][0],self.cube[n][1],self.cube[(n+1) % 4][2]] if n<4 else [list(a) for a in zip(*self.cube[n])][::-1] if n==5 else self.cube[n] for n in range(6)]
#        self.cube = tempCube
#        label = Label(root, text = self.cube)
#        label.pack()
#        print(self.cube)
#    __call__ = BotLeft
#    "Turns the bot row left."
#    def BotRight(self):
#        tempCube = [[self.cube[n][0],self.cube[n][1],self.cube[(n-1) % 4][2]] if n<4 else [list(a) for a in zip(*self.cube[n][::-1])] if n==5 else self.cube[n] for n in range(6)]
#        self.cube = tempCube
#        label = Label(root, text = self.cube)
#        label.pack()
#        print(self.cube)
#    "Turns the bot row right."
    
    "These are functional turns, but I came up with a better itea for implementation."

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

    def BackCW(self):
        self.Forward()
        self.Forward()
        self.Forward()
        self.Turn()
        self.Forward()
        self.CallBack()
    __call__ = BackCW
    
    def BackCCW(self):
        self.Forward()
        self.Forward()
        self.Forward()
        self.Turn()
        self.Turn()
        self.Turn()
        self.Forward()
        self.CallBack()
    __call__ = BackCCW    

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

    def RIGHT(self):
        self.Clockwise()
        self.Clockwise()
        self.Clockwise()
        self.Forward()
        self.Clockwise()
        self.CallBack()
    __call__ = RIGHT
    
    def LEFT(self):
        self.Clockwise()
        self.Forward()
        self.Clockwise()
        self.Clockwise()
        self.Clockwise()
        self.CallBack()
    __call__ = LEFT
    
    "The above functions give you the ability to rotate the cube as well as each of the sides. Giving 18 different ways to change the cube's orientation."
    
    def CallBack(self):
        self.cCube = [[[0]*3]*3 for a in range(6)]
#        colorCube = [['white' if n==1 else 'green' if n==2 else 'yellow' if n==3 else 'blue' if n==4 else 'red' if n==5 else 'orange' if n==6] for subset in self.cube for a in subset for n in a]
        for n in range(6):
            for m in range(3):
                for l in range(3):
#                    if self.cube[n][m][l] == [[[a]*3]*3 for a in range(1,7)][n][m][l]:
#                        self.cCube[n][m][l] = 1
#                    else:
#                        self.cCube[n][m][l] = 0
                    "Creates self.cCube for calculations later."
                    label = Label(root, text = self.cube[n][m][l])
                    label.grid(sticky=N+S+E+W, row=self.row[n]+m,column=self.column[n]+l)
        if self.supress==False:    
            print(self.cube)
#        if self.cube[1][1][1] == 1 and self.cube[4][1][3] == 4 and self.cube[5][3][1] == 5:
#            self.correct+=1
#        if self.cube[1][1][2] == 1 and self.cube[5][3][2] == 5:
#            self.correct+=1
#        if self.cube[1][1][3] == 1 and self.cube[5][3][3] == 5 and self.cube[2][1][1] == 2:
#            self.correct+=1
#        if self.cube[1][2][1] == 1 and self.cube[4][2][3] == 4:
#            self.correct+=1
#        if self.cube[1][2][3] == 1 and self.cube[2][2][1] == 2:
#            self.correct+=1
        "This can be done a lot faster."
#        self.cCube = self.cube == [[[n]*3]*3 for n in range(1,7)]
        "Reorganized self.cCube to be non-boolian variables for calculation purposes."
        self.cCube = [[[1 if self.cube[n][m][l] == [[[a]*3]*3 for a in range(1,7)][n][m][l] else 0 for l in range(3)] for m in range(3)] for n in range(6)]
        self.correct = [self.cCube[0][0][0]*self.cCube[3][0][2]*self.cCube[4][2][0],self.cCube[0][0][1]*self.cCube[4][2][1],self.cCube[0][0][2]*self.cCube[4][2][2]*self.cCube[1][0][0],self.cCube[0][1][0]*self.cCube[3][1][2],self.cCube[0][1][2]*self.cCube[1][1][0],self.cCube[0][2][0]*self.cCube[3][2][2]*self.cCube[5][0][0],self.cCube[0][2][1]*self.cCube[5][0][1],self.cCube[0][2][2]*self.cCube[5][0][2]*self.cCube[1][2][0],self.cCube[1][0][1]*self.cCube[4][1][2],self.cCube[1][0][2]*self.cCube[4][0][2]*self.cCube[2][0][0],self.cCube[1][1][2]*self.cCube[2][1][0],self.cCube[1][2][1]*self.cCube[5][1][2],self.cCube[1][2][2]*self.cCube[5][2][2]*self.cCube[2][2][0],self.cCube[2][0][1]*self.cCube[4][0][1],self.cCube[2][0][2]*self.cCube[4][0][2]*self.cCube[3][0][0],self.cCube[2][1][2]*self.cCube[3][1][0],self.cCube[2][2][1]*self.cCube[5][2][1],self.cCube[2][2][2]*self.cCube[3][2][0]*self.cCube[5][2][0],self.cCube[3][0][1]*self.cCube[4][1][0],self.cCube[3][2][1]*self.cCube[5][1][0]]
        "Multiply the 'boolian' value of individual cube's face to find out if you add one to the number of current correct cubes."
        "Cubes are checked by face order. Might change order later for readability."
        
        print(self.cCube[0][0][0]*self.cCube[3][0][2]*self.cCube[4][2][0])
        print(self.cube[0][0][0])
        print([[[a]*3]*3 for a in range(1,7)][0][0][0])

        print(self.cCube)
        print(self.correct)
        print(sum(self.correct))
        
        "Something is wrong with the calculation of the # of correct cubes. Might change the method of calcuation."
#        label = Label(root, text = "correct: "+str(self.correct))
#        label.grid(sticky=N+S+E+W, row=6,column=3,columnspan=2)
    __call__ = CallBack
    
    def Random(self):
        alpha = random.randint(1,13)
        if alpha == 1:
            self.TopLeft()
        elif alpha == 2:
            self.TopRight()
        elif alpha == 3:
            self.BackCCW()
        elif alpha == 4:
            self.BackCW()
        elif alpha == 5:
            self.BotLeft()
        elif alpha == 6:
            self.BotRight()
        elif alpha == 7:
            self.FrontCCW()
        elif alpha == 8:
            self.FrontCW()
        elif alpha == 9:
            self.LeftDown()
        elif alpha == 10:
            self.LeftUp()
        elif alpha == 11:
            self.RightDown()
        else:
            self.RightUp()
    "Random turn"
    
    def Turn20(self):
        for n in range(21):
            self.Random()
    "Randomize cube. Currently allows for repeats and adjacent inverses."
    
root = Tk()
root.geometry("420x250+30+30") 
root.resizable(width=False, height=False)
my_gui = Cube(root)

root.mainloop()
"Actually presents the GUI."