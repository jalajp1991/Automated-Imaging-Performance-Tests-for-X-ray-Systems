# -*- coding: utf-8 -*-
"""
angle += -90
Created on Mon Dec  3 17:14:06 2018

@author: 212719605
"""
from scipy.signal import find_peaks
import numpy as np
import matplotlib.pyplot as plt

import peakutils.peak



def lineprofile(lineProfilePoints):
    import SlidingWindowMedian
    
    x=lineProfilePoints
    Cpeaks_index_2d=[]
    ABpeaks_index_Values=[]
    ABpeaks_index_Valuess=[]
    Bpeaks_index=[]
    Bpeaks_indexx=[]
    Cpeaks_index=[]
    Sliding_Window_Median=[]
    Sliding_Window_Median=SlidingWindowMedian.RunningMedian(x)

    
    
    ABpeaks_index=[]
    MedianValues=[]
    MedianIndex=[]

    peaks1, _ = find_peaks(-x)
    peaks =peakutils.peak.indexes(-x,thres=0.01/(np.max(-x)),min_dist=2)
    for index in peaks:
        try:
            valuelp=lineProfilePoints[index]#value in line pair
            valuesm=Sliding_Window_Median[index]#value in line sliding window median
        except:
            break
        if valuelp < valuesm:
            MedianValues.append(valuesm)
            MedianIndex.append(index)
            
        else:
            pass
        
        
        
        
        
        
    ''' Deleting the non pair indexes in AB peaks Pair   '''
    
    
#    
    ABpeaks_index=MedianIndex
    for index in range(0,len(ABpeaks_index),2):
        try:
            valueA=ABpeaks_index[index]                                                 #value in line pair
            valueB=ABpeaks_index[index+1]                                                 #value in line sliding window median
        except:
            break
        n=len(ABpeaks_index)//2
        if n==0:
            break
            
        else:
            if index >(len(ABpeaks_index)//1.3) and valueB-valueA > 15:
                Non_pair_index=len(ABpeaks_index) - index
                del ABpeaks_index[-Non_pair_index:]
            else:
                pass
                                          #deleting all the non pair indexes 
    
    
    
    
    ''' Calculating C peaks from AB pair Indexes '''
    
    for index in range(0,len(ABpeaks_index),2):
        try:
            valueA=ABpeaks_index[index]                                                 #value in line pair
            valueB=ABpeaks_index[index+1]                                                 #value in line sliding window median
        except:
            break
        ABpeaks_index_Valuess.append(lineProfilePoints[valueA:valueB])
        for sublist in ABpeaks_index_Valuess:
            for item in sublist:
                ABpeaks_index_Values.append(item)
        Cpeaks_index_2d.append(np.where(lineProfilePoints==np.max(ABpeaks_index_Values)))
        Cpeaks_index1=[y for x in Cpeaks_index_2d for y in x]
        Cpeaks_index=[y for x in Cpeaks_index1 for y in x]
        del ABpeaks_index_Values[:]
        del ABpeaks_index_Valuess[:]
#
    C_Peak_Values=lineProfilePoints[Cpeaks_index] 
    ''' Calculating Back line peaks from AB pair Indexes '''
#    
    count=0
    
    for index in range(1,len(ABpeaks_index),2):
        try:
            valueA=ABpeaks_index[index]                                                 #value in line pair
            valueB=ABpeaks_index[index+1]                                                 #value in line sliding window median
        except:
            break
        tmp=((valueB-valueA)//2)
        reqindex=int(tmp/2.5)
        startIndex=valueA+reqindex
        stopIndex=valueB-reqindex
        
        if count == 0:
            Bpeaks_indexx.append([i for i in range(startIndex,stopIndex)]) 
            startIndex=0
            stopIndex=startIndex+reqindex
            Bpeaks_indexx.append([i for i in range(startIndex,stopIndex)])
            startIndex=ABpeaks_index[-1]+reqindex
            stopIndex=startIndex+reqindex
            Bpeaks_indexx.append([i for i in range(startIndex,stopIndex)])
            count+=1
        else:
            Bpeaks_indexx.append([i for i in range(startIndex,stopIndex)]) 
            Bpeaks_index=[y for x in Bpeaks_indexx for y in x] #list(itertools.chain(*Bpeaks_indexx))
            Bpeaks_index.sort()
#    
#    
#
#    plt.plot(Cpeaks_index, lineProfilePoints[Cpeaks_index], "o" ,label='Cpeaks_index')
#    plt.plot(Bpeaks_index, lineProfilePoints[Bpeaks_index], "x" ,label='Back peaks_index')
#    plt.plot(ABpeaks_index, lineProfilePoints[ABpeaks_index], "o" ,label='ABpeaks_index')
#    plt.plot(MedianIndex, MedianValues, "d" ,label='Median values')

    plt.plot(peaks1, lineProfilePoints[peaks1], "o" ,label='peaks')
    plt.plot(x,label='Line Profile')
    plt.plot(Sliding_Window_Median,label='median')
#    plt.plot(Medianvalues,label='median peaks') 
    plt.grid(True)
    plt.legend()
    plt.show()

##    
#    Back_Poly_Cvalues=[]
#
#    A_Peak_Values=[]
#    B_Peak_Values=[]
#    B_Peak_Index=[]
#    A_Peak_Index=[]
#    
#
#    abc=[]
#    abc.append(lineProfilePoints[ABpeaks_index])
#                                                                 
#    ABpeaks_index=np.array(ABpeaks_index)
#    len_Cpeaks_index=len(Cpeaks_index)
#    len_ABpeaks_index=len(ABpeaks_index)
#    n=len_ABpeaks_index-2*len_Cpeaks_index
#    AB_Peak_Values=lineProfilePoints[ABpeaks_index]
#    AB_Peak_Values=AB_Peak_Values.tolist()
#    if n==0:
#        pass
#    else:
#        del AB_Peak_Values[-n:]
#    AB_Peak_Values=np.array(AB_Peak_Values)
#    ABpeaks_index=ABpeaks_index.tolist()
#    if n==0:
#        pass
#    else:
#        del ABpeaks_index[-n:]
#    for index in range(0,len(ABpeaks_index),2):
#        tmp=ABpeaks_index[index]
#        tmp1=ABpeaks_index[index+1]
#        A_Peak_Index.append(tmp)
#        B_Peak_Index.append(tmp1)
#    for index in range(0,len(AB_Peak_Values),2):
#        A_Peak_Values.append(AB_Peak_Values[index])
#        B_Peak_Values.append(AB_Peak_Values[index+1])
##    plt.plot(Bpeaks_index, lineProfilePoints[Bpeaks_index], "o" ,label='Bpeaks_index')
##    plt.plot(ABpeaks_index, lineProfilePoints[ABpeaks_index], "d" ,label='ABpeaks_index')
###    plt.plot(ABpeaks_index, lineProfilePoints[ABpeaks_index], "d" ,label='ABpeaks_index')
##    plt.plot(x,label='Line Profile')
###    plt.plot(peaks,lineProfilePoints[peaks],"o")
##    plt.grid(True)
##    plt.legend()
##    plt.show()
#    
#    '''             # Calculate Back peaks                                    '''
##
#
#    
#    ##############################################################################
#    
#    #p = np.polyfit(Bpeaks_index,j,1)
#    tmp = []
#    Threshold=10
#    tmp1=[]
#    tmp2=[]
#    count=0
#    Back_Peaks_Values=[]
#    Back_Peaks_Index=[]
##    print(Bpeaks_index)
#    for index in range(len(Bpeaks_index)):
#        try:
#            Bpeaks_index1=Bpeaks_index[index]
#            Bpeaks_index2=Bpeaks_index[index+1]
#        except:
#            break
#        
#        if (Bpeaks_index2-Bpeaks_index1) < Threshold:
#    #        sum1 += Bpeaks_index1
#            tmp.append(Bpeaks_index1)
#            if Bpeaks_index2 == Bpeaks_index[-1]:
#                tmp.append(Bpeaks_index2)
#                first_element, last_element = tmp[0], tmp[-1]
#                for index in range (first_element,last_element+1):
#                    tmp2.append(index)
#                    tmp1.append(lineProfilePoints[index])
#                Back_Peaks_Values.append(tmp1)
#                Back_Peaks_Index.append(tmp2)
#                tmp1=[]
#                tmp=[]
#                tmp2=[]
#            
#        
#        
#           
#        else:
#            tmp.append(Bpeaks_index1)
#            first_element, last_element = tmp[0], tmp[-1]
#            for index in range (first_element,last_element+1):
#                tmp2.append(index)
#                tmp1.append(lineProfilePoints[index])    
#            Back_Peaks_Values.append(tmp1)
#            Back_Peaks_Index.append(tmp2)
#            count+=1
#    #        Back_Peaks_Values.append(tmp)
#            tmp1=[]
#            tmp=[]
#            tmp2=[]
#
#
#    Back_Peaks_Values_Pair_Values = []
#    def flatten_values(Back_Peaks_Values_Pair):
#        for i in Back_Peaks_Values_Pair:
#            for j in i:
#                Back_Peaks_Values_Pair_Values.append(j)
#    
#    Back_Peaks_Values_Pair_Index = []
#    def flatten_index(Back_Peaks_Index_Pair):
#        for i in Back_Peaks_Index_Pair:
#            for j in i:
#                Back_Peaks_Values_Pair_Index.append(j)
#    Back_Line_Poly_Values=[]
#    Back_Line_Poly_Index=[]
#    
#    def backline_poly(Back_Peaks_Values_Pair_Index):
#        for i in Back_Peaks_Values_Pair_Index:
#    #        for index in range(len(lineProfilePoints)):
#            Back_Line_Poly_Values.append(p[0]*(i) + p[1])
#            Back_Line_Poly_Index.append(i)
#    #            Back_Line_Poly_Values.append(p[0]*(index) + p[1])
#    #            Back_Line_Poly_Index.append(index)
#            
#    
#    DiP=[]
#    Back_Peaks_Values_Pair=[]
#    #print(idx)
#    Back_Poly_Avalues=[]
#    Back_Poly_Bvalues=[]
#    Back_Peaks_Index_Pair=[]
#    
#    #Back_Peaks_Values_Pair=np.array([np.array(xi) for xi in Back_Peaks_Values_Pair])
#    for index in range(len(Back_Peaks_Values)):
#        try:
#            tmp1=Back_Peaks_Values[index]
#            tmp2=Back_Peaks_Values[index+1]
#            tmp3=Back_Peaks_Index[index]
#            tmp4=Back_Peaks_Index[index+1]
#            cindex=Cpeaks_index[index]
#            a=ABpeaks_index[2*index]
#            b=ABpeaks_index[2*index+1]
#        except:
#            break
#        Back_Peaks_Index_Pair.append(tmp3)
#        Back_Peaks_Index_Pair.append(tmp4)
#        Back_Peaks_Values_Pair.append(tmp1)
#        Back_Peaks_Values_Pair.append(tmp2)
#        flatten_values(Back_Peaks_Values_Pair)
#        flatten_index(Back_Peaks_Index_Pair)
#        p=np.polyfit(Back_Peaks_Values_Pair_Index,Back_Peaks_Values_Pair_Values,1)
#        Back_Poly_Cvalues.append(p[0]*(cindex) + p[1])
#        Back_Poly_Avalues.append(p[0]*(a) + p[1])       
#        Back_Poly_Bvalues.append(p[0]*(b) + p[1])
#        backline_poly(Back_Peaks_Values_Pair_Index)
#        C=Back_Poly_Cvalues-C_Peak_Values[index]
#        Back_Poly_Avalues=np.array(Back_Poly_Avalues)
#        Back_Poly_Bvalues=np.array(Back_Poly_Bvalues)
#        B_Peak_Values=np.array(B_Peak_Values)
#        A_Peak_Values=np.array(A_Peak_Values)
#        A=Back_Poly_Avalues-A_Peak_Values[index]
#        B=Back_Poly_Bvalues-B_Peak_Values[index]
#        Dip=100*((A+B-2*C)/(A+B))
#        DiP.append(Dip)
##        plt.plot(Back_Peaks_Values_Pair_Index,Back_Peaks_Values_Pair_Values,'o',label='Actual Back peaks',color='blue')
##        plt.plot(Back_Line_Poly_Index,Back_Line_Poly_Values,'-',label='Actual Back Line',color='black')
##        plt.plot(Cpeaks_index, lineProfilePoints[Cpeaks_index], "x" ,label='Cpeaks')
##        plt.plot(ABpeaks_index, lineProfilePoints[ABpeaks_index], "d" ,label='ABpeaks')
##        plt.vlines(x=A_Peak_Index, ymin=A_Peak_Values, ymax=Back_Poly_Avalues,color='gray',label='Total A Height')
##        plt.vlines(x=B_Peak_Index, ymin=B_Peak_Values, ymax=Back_Poly_Bvalues,color='purple',label='Total B Height')
##        plt.vlines(x=Cpeaks_index, ymin=C_Peak_Values, ymax=Back_Poly_Cvalues,color='green',label='Total C Height')
##        plt.title('Profile of Duplex Wire \n Averaged from 21 Line Profiles')
##        plt.xlabel('X Distance -->')
##        plt.ylabel('Gray Values -->')
##          #plt.plot(peaks, x[peaks], )
##        plt.plot(x,label='Line Profile')
##        plt.grid(True)
##        plt.legend()
##        plt.show()
###        ctmp.append(p)
##        print('''---------------------------------------------------- ''')
##        print(p)
##        print('''----Coefficients for a particular A B & C Values --- ''')
##        print('''---------------------------------------------------- ''')
##        print(Back_Poly_Avalues,Back_Poly_Cvalues,Back_Poly_Bvalues)
##        print('''--A Max Values--  -C Max Values-    -B Max Values- ''')
##        print('''---------------------------------------------------- ''')
##        print(A,C,B)
##        print('''------Total Distance of A,B & C ------ ''')
#        Back_Peaks_Values_Pair=[]
#        Back_Peaks_Index_Pair=[]
#        Back_Poly_Cvalues=[]
#        Back_Poly_Bvalues=[]
#        Back_Poly_Avalues=[]
#        Back_Peaks_Values_Pair_Index=[]
#        Back_Peaks_Values_Pair_Values=[]
#    
#    Wire_Pair_Spacing=[800,630,500,400,320,250,200,160,130,100,80,63,50,40,32]
#    Req_Wire_Pair_Spacing=[]
#    Dip_Percent=[]
#    for j in DiP:
#        for i in j:
#            Dip_Percent.append(i)
#    
#    Len_Dip_Percent=len(Dip_Percent)    
#    for index in range (0,Len_Dip_Percent):
#        tmp=Wire_Pair_Spacing[index]
#        Req_Wire_Pair_Spacing.append(tmp)
#    
#    del Req_Wire_Pair_Spacing[:-5]
#    del Dip_Percent[:-5]    
#    
#    Dip_poly2d=np.polyfit(Req_Wire_Pair_Spacing,Dip_Percent,2)
#    Dip_Poly=[]
#    for index in range(1, 200):
#        Dip_Poly.append(Dip_poly2d[0]*(index**2) + Dip_poly2d[1]*(index)+ Dip_poly2d[2])
#    
#    #Dip_modulation=20
#    Dip_poly2d[-1] -= 20
#    
#    iSRB_Detector=np.roots(Dip_poly2d)
#    
##    plt.plot(range(1, 200),Dip_Poly,'-',label='Dip 2dPloynomial')
##    plt.plot(Req_Wire_Pair_Spacing,Dip_Percent,'o',label='Dip Percentage')
##    plt.legend()
##    plt.show()
##    print('Value of iSRb Detector is Below')
#    print(iSRB_Detector[1])
#    SrbValue=iSRB_Detector[1]
#    file = open('SrbDetectorIQI.txt','w')
#    file.write(str("%s\n" % SrbValue))
#    for item in DiP:
#        file.write("%s\n" % item)
#    file.write(str(len(Cpeaks_index)))
#    file.close()
#    return SrbValue
##    
##    
#    #plt.plot(A,lineProfilePoints[A],label='Distance A')
