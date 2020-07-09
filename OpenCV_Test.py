import numpy as np
import cv2

from OpenCV_Core import OpenCV_Core
a=OpenCV_Core()

a.OpenCV_Video.Show_Video('walk.mp4')


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
