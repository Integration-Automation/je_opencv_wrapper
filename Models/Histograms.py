import cv2
import numpy as np
from matplotlib import pyplot as plt


class Histograms():

    def __init__(self):
        pass

    def Get_Hist_OpenCV(self,Image):
        return cv2.calcHist([Image], [0], None, [256], [0, 256])

    def Get_Hist_NumPy(self,Image):
        return np.histogram(Image.ravel(),256,[0,256])

    def Get_Hist_Plt(self,Image):
        plt.hist(Image.ravel(),256,[0,256]); plt.show()

