# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 09:42:40 2019

@author: 212719605
"""
from collections import deque
from bisect import insort, bisect_left
from itertools import islice
import numpy as np
import function

def RunningMedian(x):
    import SrbDetectorIQI
    """
     Purpose: Find the median for the points in a sliding window (odd number in size) 
              as it is moved from left to right by one point at a time.
      Inputs:
            seq -- list containing items for which a running median (in a sliding window) 
                   is to be calculated
              M -- number of items in window (window size) -- must be an integer > 1
      Otputs:
         medians -- list of medians with size N - M + 1
       Note:
         1. The median of a finite list of numbers is the "center" value when this list
            is sorted in ascending order. 
         2. If M is an even number the two elements in the window that
            are close to the center are averaged to give the median (this
            is not by definition)
    """
    seq = iter(x)
    d = deque()
    s = []
    Window_Size=int(function.WindowSize(SrbDetectorIQI.pixelSize))+50
    Sliding_Window_Median = []
     # Set up list s (to be sorted) and load deque with first window of seq
    for item in islice(seq, Window_Size):
        d.append(item)
        insort(s, item)# Sort it in increasing order and extract the median ("center" of the sorted window)
         # Simple lambda function to handle even/odd window sizes    
        Sliding_Window_Median.append(s[len(d)//2])          # Simple lambda function to handle even/odd window sizes   
    m = Window_Size // 2
    
    # Now slide the window by one point to the right for each new position (each pass through 
    # the loop). Stop when the item in the right end of the deque contains the last item in seq
    for item in seq:
        old = d.popleft()                                   # pop oldest from left
        d.append(item)                                      # push newest in from right
        del s[bisect_left(s, old)]                          # locate insertion point and then remove old 
        insort(s, item)                                     # insert newest such that new sort is not required   
        Sliding_Window_Median.append(s[m]) 
    Sliding_Window_Median=np.array(Sliding_Window_Median)
    Sliding_Window_Median=Sliding_Window_Median*0.985
    return Sliding_Window_Median