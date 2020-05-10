# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:03:58 2018

@author: 212719605
"""
import cv2
import numpy as np
from scipy.misc import bytescale



def crop_minAreaRect(image,rect,angle,roi,pixelSize):
    import Required_ROI
    # rotate img
#    angle=rect[2]
    
#   
#    else:
#    if (angle < -45.0):
#        angle += -90
#    else:
#        angle=angle
#    angle = (-90 + angle)
###    angle = (-90 + angle)#DoubleDuplex_Horizontal,CRTestPhantomVertical
#    rows,cols = roi.shape[0], roi.shape[1]
#    M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
#    
#
#    img_rot = cv2.warpAffine(roi,M,(cols,rows),flags=cv2.INTER_NEAREST)
    (h, w) = roi.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX,cY),angle,4)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
 
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    img_rot = cv2.warpAffine(roi,M,(nW,nH),flags=cv2.INTER_NEAREST)
    # rotate bounding box
#    rect0 = (rect[0], rect[1], 0.0)
    box = (cv2.boxPoints(rect))
    pts = np.int0(cv2.transform(np.array([box]), M))[0]    
    pts[pts < 0] = 0
    
    
    
    # crop
    img_crop = img_rot[np.min(pts[:,1]):np.max(pts[:,1]), 
                       np.min(pts[:,0]):np.max(pts[:,0])]
    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/Cropped Rotated Image.tif',img_crop)
    required_img_crop,boundingPoints,alignment=Required_ROI.auto_60_roi(pts,img_rot,pixelSize)

#    M_boundingpoits = cv2.getRotationMatrix2D((cols/2,rows/2),-angle,1)
    inverse = cv2.invertAffineTransform(M)
    pts_boundingPoints =(cv2.transform(np.array([boundingPoints]), inverse))[0]
    pts_boundingPoints[pts_boundingPoints < 0] = 0

    
    
    box = np.int0(box)
    
    # draw a red 'nghien' rectangle
    image8=bytescale(roi)
    color_image=cv2.cvtColor(image8,cv2.COLOR_GRAY2RGB)
    color_image1=cv2.cvtColor(image8,cv2.COLOR_GRAY2RGB)
    cv2.drawContours(color_image, [pts_boundingPoints], 0, (255, 0, 0),2)
#    cv2.drawContours(color_image1, [inverse], 0, (0,0,255),2)
    cv2.drawContours(color_image, [box], 0, (0, 0, 255),2)
    
    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/BoundingBox.tif',color_image)
    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/BoundingBoxnew.tif',color_image1)
    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/RotatedImage.tif',img_rot)
    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/Cropped Rotated Image.tif',img_crop)
    cv2.imwrite('C:/Users/212719605/Downloads/text-skew-correction/rotation/images/Required_rotatedimage.tif',required_img_crop)

    return required_img_crop,alignment


