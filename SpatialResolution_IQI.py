# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:33:52 2018

@author: 212719605 
"""
#from scipy.signal import find_peaks
import function
import cv2
import numpy as np
from scipy.misc import bytescale
from skimage.filters import threshold_otsu
import Automatic_ROI
import LineProfile
import math
from skimage import io
#im = io.imread(jpg)




def SpatialResolution_IQI(imagePath,pixelSize,newangle):
    imagePath=imagePath
    image = io.imread(imagePath)
    #image=ndimage.zoom(image,2.0,mode='constant')
    #cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/Zoomed_Image.tif',image)
    img=bytescale(image)

    #pixel size in  μm
    pixel_size=pixelSize
    #interpolation=1
#    phantomSizeInPixels=function.phantom_size(pixel_size)
    Sobelx = cv2.Sobel(img, cv2.CV_16SC1 , 1, 0)
    Sobely = cv2.Sobel(img, cv2.CV_16SC1 , 0, 1)
    
    sobelX = np.uint8(np.absolute(Sobelx))
    sobelY = np.uint8(np.absolute(Sobely))
    sobel = cv2.bitwise_or(sobelX, sobelY)
#    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/sobel.tif',sobel)
    thresh =threshold_otsu(sobel)
    
    lowThresh = 0.5*thresh
    edges = cv2.Canny(img,lowThresh,thresh)
    img_shape = image.shape
    blank =np.zeros((img_shape[0],img_shape[1]))
    duplexWireLength=function.hough_line_length(pixel_size)
    actual_duplexWireLength=function.percentage(70,duplexWireLength)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength=actual_duplexWireLength,maxLineGap=10)
    lines1 = lines[:,0,:]
    
    
    temp1=np.array(lines1[:,0])
    temp2=np.array(lines1[:,1])
    temp3=np.array(lines1[:,2])
    temp4=np.array(lines1[:,3])
    
    Concatenate_t1t2=np.column_stack((temp1,temp2))
    Concatenate_t3t4=np.column_stack((temp3,temp4))
    setofPoints=np.concatenate((Concatenate_t1t2,Concatenate_t3t4),axis=0)
    
    
    for x1,y1,x2,y2 in lines1[:]:
        cv2.line(blank,(x1,y1),(x2,y2),(255,255,255),1)
    
#    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/hough.tif',blank)
#    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/canny.tif',edges)
    
    y, x = np.nonzero(blank)
    x = x - np.mean(x)
    y = y - np.mean(y)
    coords = np.vstack([x, y])
    cov = np.cov(coords)
    evals, evecs = np.linalg.eig(cov)
    sort_indices = np.argsort(evals)[::-1]
    x_v1, y_v1 = evecs[:, sort_indices[0]]  # Eigenvector with largest eigenvalue
    x_v2, y_v2 = evecs[:, sort_indices[1]]
    
    theta = math.atan2((y_v1),(x_v1)) 
    angle=theta/np.pi*180
    
    
    #angle+= -90
    x, y, width, height = cv2.boundingRect(setofPoints)

    roi = image[y-function.freeway_size(pixel_size)-30:y+height+function.freeway_size(pixel_size)+30, x-function.freeway_size(pixel_size)-30:x+width+function.freeway_size(pixel_size)+30]
    
    
#    color_image1=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),2)
    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/roi_original image.tif',img)
    cv2.imwrite("C:/Users/212719605/Downloads/text-skew-correction/rotation/images/roi.tif", roi)
    img=bytescale(roi)
    
    #pixel size in  μm
    
    #interpolation=1
    
    Sobelx = cv2.Sobel(img, cv2.CV_16SC1 , 1, 0)
    Sobely = cv2.Sobel(img, cv2.CV_16SC1 , 0, 1)
    
    sobelX = np.uint8(np.absolute(Sobelx))
    sobelY = np.uint8(np.absolute(Sobely))
    sobel = cv2.bitwise_or(sobelX, sobelY)
#    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/sobel1.tif',sobel)
    thresh =threshold_otsu(sobel)
    
    lowThresh = 0.5*thresh
    edges = cv2.Canny(img,lowThresh,thresh)
    img_shape = image.shape
    blank =np.zeros((img_shape[0],img_shape[1]))
    duplexWireLength=function.hough_line_length(pixel_size)
    actual_duplexWireLength=function.percentage(70,duplexWireLength)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength=actual_duplexWireLength,maxLineGap=10)
    lines1 = lines[:,0,:]
    
    
    temp1=np.array(lines1[:,0])
    temp2=np.array(lines1[:,1])
    temp3=np.array(lines1[:,2])
    temp4=np.array(lines1[:,3])
    
    Concatenate_t1t2=np.column_stack((temp1,temp2))
    Concatenate_t3t4=np.column_stack((temp3,temp4))
    setofPoints=np.concatenate((Concatenate_t1t2,Concatenate_t3t4),axis=0)
    
    
    for x1,y1,x2,y2 in lines1[:]:
        cv2.line(blank,(x1,y1),(x2,y2),(255,255,255),1)
    
    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/hough1.tif',blank)
    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/canny1.tif',edges)
    
    y, x = np.nonzero(blank)
    x = x - np.mean(x)
    y = y - np.mean(y)
    coords = np.vstack([x, y])
    cov = np.cov(coords)
    evals, evecs = np.linalg.eig(cov)
    sort_indices = np.argsort(evals)[::-1]
    x_v1, y_v1 = evecs[:, sort_indices[0]]  # Eigenvector with largest eigenvalue
    x_v2, y_v2 = evecs[:, sort_indices[1]]
    
    theta = math.atan2((y_v1),(x_v1)) 
    angle=theta/np.pi*180
    
    
    #angle+= -90
    rect = cv2.minAreaRect(setofPoints)
    
    
    
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    angle=rect[2]
    angle=angle+ newangle
    image_cropped,alignment=Automatic_ROI.crop_minAreaRect(image,rect,angle,roi,pixelSize)
    #
    
    #
    
    #
    
    
    if alignment==('vertical'):
        lineProfilePoints=np.mean(image_cropped,axis=1)
    else:
        lineProfilePoints=np.mean(image_cropped,axis=0)
      
    lineProfilePoints = np.array(lineProfilePoints)
    SrbValue=LineProfile.lineprofile(lineProfilePoints)
    return SrbValue,angle
    
    
     
    #        lineprofile(lineProfilePoints):
