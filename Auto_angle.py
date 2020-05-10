# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 16:30:19 2019

@author: 212719605
"""

import csv

def Automated_Rotation(angle):
    output  = []
    for i in range (-10,10,0.1):
        newangle=angle+i
        

    
    
        output.append([newangle, result[i]])
    with open(SAVEPATH, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows([])
