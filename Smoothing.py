import cv2
import numpy as np

class Smoothing():

    def __init__(self):
        pass

    '''
    As for one-dimensional signals, images also can be filtered with various low-pass filters (LPF), high-pass filters (HPF), etc. 
    A LPF helps in removing noise, or blurring the image. A HPF filters helps in finding edges in an image.

    OpenCV provides a function, cv2.filter2D(), to convolve a kernel with an image.
    As an example, we will try an averaging filter on an image.
    
    kernel = 5x5
    
    Filtering with the above kernel results in the following being performed: 
    for each pixel, a 5x5 window is centered on this pixel, all pixels falling within this window are summed up, 
    and the result is then divided by 25. 
    This equates to computing the average of the pixel values inside that window. 
    This operation is performed for all the pixels in the image to produce the output filtered image.
    
    2D Convolution ( Image Filtering )
    '''
    def Convolution2D(self,Image,kernel=(5,5)):
        return  cv2.filter2D(Image, -1, np.ones(kernel, np.float32) / 25)