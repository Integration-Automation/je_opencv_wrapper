import cv2
import numpy as np


def get_hist_open_cv(image):
    return cv2.calcHist([image], [0], None, [256], [0, 256])


def get_hist_num_py(image):
    return np.histogram(image.ravel(), 256, [0, 256])
