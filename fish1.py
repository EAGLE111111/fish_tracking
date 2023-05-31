import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import math 
import csv
cap = cv2.VideoCapture('1.mp4')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

ret , image = cap.read() 
# setup initial location of window
# r,h,c,w - region of image
#           simply hardcoded the values
y,h,x,w = 50,40,390,40  
track_window = (x,y,w,h)

# set up the ROI for tracking
roi = image[y:y+h, x:x+w]
hsv_roi =  cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array([180, 255.,255.]),np.array([0, 60, 0.4]))
roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

# Read until video is completed
while(cap.isOpened()):
# Capture frame-by-frame
    true, image = cap.read()
    if true:

        roi = image[y:y+h, x:x+w]
        hsv_roi =  cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array([180, 255.,255.]),np.array([0, 60, 0.4]))
        roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
        print(track_window)
        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(image, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('img2',img2)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        result = cv2.VideoWriter('meanShift.mp4',fourcc,10,(int(cap.get(3)),int(cap.get(4))))
        result.write(img2)
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite(chr(k)+".jpg",img2)
            

        

# Break the loop
    else: 
        break
    
# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
