# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 03:31:15 2018

@author: Cnoized
"""
import numpy as np
cube2 = [[[1]*3]*3,[[2]*3]*3,[[3]*3]*3,[[4]*3]*3,[[5]*3]*3,[[6]*3]*3]
tempcube = cube2[1][1][1]
print(tempcube)
cube = np.array([1,2,3],[4,5,6])
print(cube)
backwards = np.array(cube).T
print(backwards)