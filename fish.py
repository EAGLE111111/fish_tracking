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
 
# Read until video is completed
with open('1.csv', 'w', encoding='UTF8',newline='') as f:
    header=["X1","Y1","W1","H1","X2","Y2","W2","H2"]
    writer = csv.writer(f)
    writer.writerow(header) 
    prev_xi,prev_yi,prev_xj,prev_yj=-1,-1,-1,-1 
    while(cap.isOpened()):
    # Capture frame-by-frame
        ret, image = cap.read()
        if ret == True:
            height, width = image.shape[:2]
            window_name='Tracker'
            xx=0
            yy=0
            start_point = (yy-10, xx-10)
            end_point = (yy+10, xx+10)
            r_color = (0, 0, 255)
            g_color=(0, 255 ,0)
            thickness = 2
            data=[]
            for y in range(50,height-10,5):
                temp=""
                for x in range(10,width-10,5):
                    if image[y, x][0]<80:
                        data.append([y,x])                             
                        cv2.imshow(window_name, image)        
            mx_r=55
            array_len=len(data)     
            # print(range(0, array_len))       
            for i in range(0,array_len):        
                xi=data[i][0]
                yi=data[i][1]   
                     
                for j in range(i+1,array_len):
                    xj=data[j][0]
                    yj=data[j][1]    
                    num1=0
                    num2=0
                    chk_array=[]
                    r_array=[]
                    g_array=[]
                    for ii in range(0,array_len): 
                        chk_array.append(0)
                    for ii in range(0,array_len):
                        xii=data[ii][0]
                        yii=data[ii][1]    
                        s=math.sqrt((xi-xii)*(xi-xii)+(yi-yii)*(yi-yii))
                        if s<mx_r:
                            chk_array[ii]=1
                            r_array.append([xii,yii])
                        s=math.sqrt((xii-xj)*(xii-xj)+(yii-yj)*(yii-yj))
                        if s<mx_r:
                            chk_array[ii]=2
                            g_array.append([xii,yii])
                    flag=0
                    for ii in range(0,array_len): 
                        if chk_array[ii]==0:
                            flag=1
                            break                    
                    if flag==0:
                        m_x1=0
                        m_y1=0
                        mr=[1000,1000,-1000,-1000]
                        for ii in r_array:
                            m_x1=m_x1+int(ii[0])
                            m_y1=m_y1+int(ii[1])
                            if ii[0]<mr[0]:
                                mr[0]=ii[0]
                            if ii[1]<mr[1]:
                                mr[1]=ii[1]
                            if ii[0]>mr[2]:
                                mr[2]=ii[0]
                            if ii[1]>mr[3]:
                                mr[3]=ii[1]    
                        m_x1=int(m_x1/len(r_array))
                        m_y1=int(m_y1/len(r_array))
                        m_x2=0
                        m_y2=0
                        mg=[1000,1000,-1000,-1000]
                        for ii in g_array:
                            m_x2=m_x2+int(ii[0])
                            m_y2=m_y2+int(ii[1])
                            if ii[0]<mg[0]:
                                mg[0]=ii[0]
                            if ii[1]<mg[1]:
                                mg[1]=ii[1]
                            if ii[0]>mg[2]:
                                mg[2]=ii[0]
                            if ii[1]>mg[3]:
                                mg[3]=ii[1] 
                        m_x2=int(m_x2/len(g_array))
                        m_y2=int(m_y2/len(g_array))
                        s1=math.sqrt((m_x1-prev_xi)*(m_x1-prev_xi)+(m_y1-prev_yi)*(m_y1-prev_yi))
                        s2=math.sqrt((m_x2-prev_xi)*(m_x2-prev_xi)+(m_y2-prev_yi)*(m_y2-prev_yi))
                        if s2<s1:
                            prev_xi=m_x2
                            prev_yi=m_y2
                            prev_xj=m_x1
                            prev_yj=m_y1
                            image = cv2.rectangle(image, (prev_yj-30,prev_xj-30), (prev_yj+30,prev_xj+30), g_color, thickness)
                            image = cv2.rectangle(image, (prev_yi-30,prev_xi-30), (prev_yi+30,prev_xi+30), r_color, thickness)

                            image = cv2.rectangle(image, (mr[1],mr[0]), (mr[3],mr[2]), (100,100,100), thickness)
                            image = cv2.rectangle(image, (mg[1],mg[0]), (mg[3],mg[2]), (100,100,100), thickness)
                        
                        else:
                            prev_xi=m_x1
                            prev_yi=m_y1
                            prev_xj=m_x2
                            prev_yj=m_y2
                            image = cv2.rectangle(image, (prev_yj-30,prev_xj-30), (prev_yj+30,prev_xj+30), g_color, thickness)
                            image = cv2.rectangle(image, (prev_yi-30,prev_xi-30), (prev_yi+30,prev_xi+30), r_color, thickness)

                            image = cv2.rectangle(image, (mr[1],mr[0]), (mr[3],mr[2]), (100,100,100), thickness)
                            image = cv2.rectangle(image, (mg[1],mg[0]), (mg[3],mg[2]), (100,100,100), thickness)   
                        # for ii in range(0,array_len):
                        #     xx=data[ii][0]
                        #     yy=data[ii][1]   
                        #     if chk_array[ii]==1:
                        #         p_color=(0, 0, 255)
                        #     else:
                        #         p_color=(0, 255, 0)
                        #     image = cv2.rectangle(image, (yy,xx), (yy+2,xx+2), r_color, thickness)                                               
                        row_data=[xi,yi,mr[2]-mr[0],mr[3]-mr[1],xj,yj,mg[2]-mg[0],mg[3]-mg[1]]
                        writer.writerow(row_data)      
                        
                        
                        break
                if flag==0:
                    break

            cv2.imshow(window_name, image) 

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    # Break the loop
        else: 
            break
    
    # When everything done, release the video capture object
    cap.release()
    
    # Closes all the frames
    cv2.destroyAllWindows()
