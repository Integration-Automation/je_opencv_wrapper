import cv2
import numpy as np

class Morphological():

    def __init__(self):
        pass

    '''
    The basic idea of erosion is just like soil erosion only, 
     it erodes away the boundaries of foreground object (Always try to keep foreground in white). So what does it do? 
      The kernel slides through the image (as in 2D convolution). 
       A pixel in the original image (either 1 or 0) will be considered 1 only if all the pixels under the kernel is 1,
        otherwise it is eroded (made to zero).

    So what happends is that, all the pixels near boundary will be discarded depending upon the size of kernel. 
      So the thickness or size of the foreground object decreases or simply white region decreases in the image. 
       It is useful for removing small white noises (as we have seen in colorspace chapter), detach two connected objects etc.
    '''
    def Erosion(self,Image,kernel=(5,5)):
        return cv2.erode(Image, np.ones(kernel, np.uint8), iterations=1)

    '''
    It is just opposite of erosion. 
    Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’. 
    So it increases the white region in the image or size of foreground object increases. 
    Normally, in cases like noise removal, erosion is followed by dilation. 
    Because, erosion removes white noises, but it also shrinks our object.
    So we dilate it. Since noise is gone, they won’t come back, but our object area increases. 
    It is also useful in joining broken parts of an object.
    '''
    def Dilation(self,Image,kernel=(5,5)):
        return cv2.dilate(Image, np.ones(kernel, np.uint8), iterations=1)

    '''
    Opening is just another name of erosion followed by dilation. 
    It is useful in removing noise, as we explained above. 
    Here we use the function, cv2.morphologyEx()
    '''
    def Opening(self,Image,kernel=(5,5)):
        return cv2.morphologyEx(Image, cv2.MORPH_OPEN, np.ones(kernel, np.uint8))

    '''
    Closing is reverse of Opening, Dilation followed by Erosion. 
    It is useful in closing small holes inside the foreground objects, or small black points on the object.
    '''
    def Closing(self,Image,kernel=(5,5)):
        return cv2.morphologyEx(Image, cv2.MORPH_CLOSE, np.ones(kernel, np.uint8))

    '''
    It is the difference between dilation and erosion of an image.
    The result will look like the outline of the object.
    '''
    def Morphological(self,Image,kernel=(5,5)):
        return cv2.morphologyEx(Image, cv2.MORPH_GRADIENT, np.ones(kernel, np.uint8))

    '''
    It is the difference between input image and Opening of the image.
    '''
    def Top_Hat(self,Image,kernel=(5,5)):
        return cv2.morphologyEx(Image, cv2.MORPH_TOPHAT, np.ones(kernel, np.uint8))

    '''
    It is the difference between the closing of the input image and input image.
    '''
    def Black_Hat(self,Image,kernel=(5,5)):
        return cv2.morphologyEx(Image, cv2.MORPH_BLACKHAT, np.ones(kernel, np.uint8))

    '''
    We manually created a structuring elements in the previous examples with help of Numpy. 
    It is rectangular shape. But in some cases, you may need elliptical/circular shaped kernels. 
    So for this purpose, OpenCV has a function, cv2.getStructuringElement(). 
    You just pass the shape and size of the kernel, you get the desired kernel.
    '''
    def Get_Kernel(self,Mode,kernel=(5,5)):
        return cv2.getStructuringElement(cv2.MORPH_RECT, kernel)