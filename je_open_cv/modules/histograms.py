import cv2
import numpy as np


def get_hist_open_cv(Image):
    return cv2.calcHist([Image], [0], None, [256], [0, 256])


def get_hist_num_py(Image):
    return np.histogram(Image.ravel(), 256, [0, 256])
