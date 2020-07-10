import cv2
import numpy

class UI():

    def __init__(self):
        pass

    '''
    Switch_Function 要有一個參數 會發送目前位置給Switch_Function的參數
    '''
    def AddTrackbar(self,Canvas_Name,Switch_Function,Track_Name='Name',Start=0,End=255):
        cv2.createTrackbar(Track_Name,Canvas_Name,Start,End,Switch_Function)

    def GetTrackbarPos(self,Track_Name,Canvas_Name):
        return cv2.getTrackbarPos(Track_Name,Canvas_Name)