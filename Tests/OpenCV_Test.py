import numpy as np
import cv2

from OpenCV_Core.OpenCV_Core import OpenCV_Core
a=OpenCV_Core()
print(a.Event.Events())
a.Event.Set_Callback_Event('ooo')
a.Draw.Show_Canvas('ooo')

'''# mouse callback function
def draw_circle(event,x,y):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('ooo')
cv2.setMouseCallback('ooo',draw_circle)

while(1):
    cv2.imshow('ooo',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()'''

'''
c=a.Feature.ORB_Feature('may.png')
cv2.imshow('may',c)
cv2.waitKey()
'''

'''
c=a.Template_Detection.Find_Multi_Object('box.png','find_umbrella.png')
cv2.imshow('oo',c)
cv2.waitKey()
'''
