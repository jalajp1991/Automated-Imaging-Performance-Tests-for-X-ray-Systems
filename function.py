# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 13:17:50 2018

@author: 212719605
"""
#import numpy as np


def percentage(percent, whole):
  return ((percent * whole) // 100)



def hough_line_length(pixelSize):
    pixelsizeIn_mm=(pixelSize/1000.0)
    return (15/pixelsizeIn_mm)



def symbol_length(pixelSize):
    pixelsizeIn_mm=(pixelSize/1000.0)
    return (14/pixelsizeIn_mm)

def phantom_size(pixelSize):
    pixelsizeIn_mm=(pixelSize/1000.0)
    return (57/pixelsizeIn_mm)

def WindowSize(pixelSize):
    pixelsizeIn_mm=(pixelSize/1000.0)
    return (4/pixelsizeIn_mm)

def freeway_size(pixelSize):
#    import SpatialResolution_IQI
    pixelsizeIn_mm=((pixelSize)/1000.0)
    return int(3/pixelsizeIn_mm)

Back_Peaks_Values_Pair_Values = []
def flatten_values(Back_Peaks_Values_Pair):
    for i in Back_Peaks_Values_Pair:
        for j in i:
            Back_Peaks_Values_Pair_Values.append(j)

Back_Peaks_Values_Pair_Index = []
def flatten_index(Back_Peaks_Index_Pair):
    for i in Back_Peaks_Index_Pair:
        for j in i:
            Back_Peaks_Values_Pair_Index.append(j)
Back_Line_Poly_Values=[]
Back_Line_Poly_Index=[]

#def backline_poly(Back_Peaks_Values_Pair_Index):
#    for i in Back_Peaks_Values_Pair_Index:
##        for index in range(len(average_of_arrays)):
#        Back_Line_Poly_Values.append(p[0]*(i) + p[1])
#        Back_Line_Poly_Index.append(i)

