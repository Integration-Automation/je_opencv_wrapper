import cv2
import numpy as np

'''
特徵點檢測
'''

class Feature():

    def __init__(self):
        pass

    '''
    As usual, we have to create an ORB object with the function, cv2.ORB() or using feature2d common interface. 
    It has a number of optional parameters. 
    Most useful ones are nFeatures which denotes maximum number of features to be retained (by default 500), 
    scoreType which denotes whether Harris score or FAST score to rank the features (by default, Harris score) etc. 
    Another parameter, WTA_K decides number of points that produce each element of the oriented BRIEF descriptor. 
    By default it is two, ie selects two points at a time. 
    In that case, for matching, NORM_HAMMING distance is used. 
    If WTA_K is 3 or 4, which takes 3 or 4 points to produce BRIEF descriptor, then matching distance is defined by NORM_HAMMING2.
    
    詳情:
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_orb/py_orb.html#orb
    '''
    def ORB_Feature(self,Image):

        Image = cv2.imread(Image, 0)

        ORB = cv2.ORB_create()

        kp = ORB.detect(Image, None)

        kp, des = ORB.compute(Image, kp)

        Image = cv2.drawKeypoints(Image, kp, Image, color=(0, 255, 0), flags=0)

        return Image

    def Harris(self,Image):
        gray = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray, 2, 3, 0.04)
        # result is dilated for marking the corners, not important
        dst = cv2.dilate(dst, None)
        # Threshold for an optimal value, it may vary depending on the image.
        Image[dst > 0.01 * dst.max()] = [0, 0, 255]
        return Image


