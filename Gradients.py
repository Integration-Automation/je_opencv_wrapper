import cv2
import numpy as np

'''
圖像漸變用
'''

class Gradients():

    def __init__(self):
        pass

    '''
    OpenCV provides three types of gradient filters or High-pass filters, Sobel, Scharr and Laplacian.
    '''
    #拉普拉斯算法 取XY方向
    def Laplacian(self,Image):
        return cv2.Laplacian(Image, cv2.CV_64F)

    #SobelX 取 x方向
    def SobelX(self,Image):
        return cv2.Sobel(Image, cv2.CV_64F, 1, 0, ksize=5)

    #SobelY 取 Y方向
    def SobelY(self,Image):
        return cv2.Sobel(Image, cv2.CV_64F, 0, 1, ksize=5)

    '''
    output datatype is cv2.CV_8U or np.uint8. But there is a slight problem with that. 
    Black-to-White transition is taken as Positive slope (it has a positive value) 
    while White-to-Black transition is taken as a Negative slope (It has negative value). 
    So when you convert data to np.uint8, all negative slopes are made zero. 
    In simple words, you miss that edge.

    If you want to detect both edges, better option is to keep the output datatype to some higher forms, 
    like cv2.CV_16S, cv2.CV_64F etc, take its absolute value and then convert back to cv2.CV_8U. 
    Below code demonstrates this procedure for a horizontal Sobel filter and difference in results.
    '''

    #cv2.CV_8U
    def CV_8U(self,Image):
        return cv2.Sobel(Image, cv2.CV_8U, 1, 0, ksize=5)

    #cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
    def CV_64_To_CV_8U(self,Image):
        sobelx64f = cv2.Sobel(Image, cv2.CV_64F, 1, 0, ksize=5)
        abs_sobel64f = np.absolute(sobelx64f)
        return np.uint8(abs_sobel64f)