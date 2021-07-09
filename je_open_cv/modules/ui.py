import cv2

'''
用OpenCV做的模塊
'''

'''
switch_function 要有一個參數 會發送目前位置給Switch_Function的參數
'''


def add_trackbar(canvas_name, switch_function, track_name='name', start=0, end=255):
    cv2.createTrackbar(track_name, canvas_name, start, end, switch_function)


def get_trackbar_pos(track_name, canvas_name):
    return cv2.getTrackbarPos(track_name, canvas_name)
