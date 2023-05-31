import cv2
import numpy as np

cap = cv2.VideoCapture('1.mp4')
cap.set(cv2.CAP_PROP_POS_FRAMES, 500)


for i in range(10):
    success,frame = cap.read()

if not success:
    exit(1)

frame_h,frame_w = frame.shape[:2]
size = (frame_h,frame_w)

w =frame_w//8
h =frame_h//8
x =50
y =390
track_window = (x,y,w,h)

roi =frame[y:y+h, x-w:x]

true,frame = cap.read()



while true:
    ret, frame = cap.read()
    # frame = cv2.GaussianBlur(frame, (3,3), 0)
    hsv_roi = cv2.cvtColor(frame ,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_roi, np.array([180, 255.,255.]),np.array([0, 60, 0.4]))
    roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])
    cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
    back_project = cv2.calcBackProject([hsv_roi], [0],roi_hist, [0,180],1)
    print(back_project.size)
    # remove_other_color(frame)
    term_criteria =(cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS,10,1)
    num_iters,track_window = cv2.meanShift(back_project,track_window,term_criteria)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    result = cv2.VideoWriter('meanShift.mp4',fourcc,10,(int(cap.get(3)),int(cap.get(4))))

    x,y,w,h = track_window
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
#     cv2.imshow('back-projection',back_project)


    cv2.imshow('meanshift', frame)
    result.write(frame)


    k = cv2.waitKey(50)
    if k == 27:
        break
    if k == ord('p'):
        cv2.waitKey(-1)


cv2.destroyAllWindows()

    # true,frame = cap.read()