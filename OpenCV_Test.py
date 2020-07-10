import cv2
import numpy as np
from Core import Core

def Sw(x):
    pass

JE=Core()
cv2.namedWindow('ooo')
JE.UI.AddTrackbar('ooo',Sw,Track_Name='AAA',End=100)
JE.Draw.Show_Canvas('ooo')
