import cv2
import numpy as np

'''
平滑圖像

對圖像進行濾波 會變模糊
'''

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

2D Convolution ( image Filtering )
'''


def convolution2_d(image, kernel=(5, 5)):
    return cv2.filter2D(image, -1, np.ones(kernel, np.float32) / 25)


'''
image blurring is achieved by convolving the image with a low-pass filter kernel. 
It is useful for removing noise.
It actually removes high frequency content (e.g: noise, edges)
from the image resulting in edges being blurred when this is filter is applied.
(Well, there are blurring techniques which do not blur edges). OpenCV provides mainly four types of blurring techniques.
  
1. Averaging
This is done by convolving the image with a normalized box filter. 
It simply takes the average of all the pixels under kernel area and replaces the central element with this average. 
This is done by the function cv2.blur() or cv2.boxFilter(). 
Check the docs for more details about the kernel. 
We should specify the width and height of kernel.
'''


def averaging(image, kernel=(5, 5)):
    return cv2.blur(image, kernel)


'''
In this approach, instead of a box filter consisting of equal filter coefficients, a Gaussian kernel is used.
It is done with the function, cv2.GaussianBlur().
We should specify the width and height of the kernel which should be positive and odd.
We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively.
If only sigmaX is specified, sigmaY is taken as equal to sigmaX. 
If both are given as zeros, they are calculated from the kernel size. Gaussian filtering is highly effective in removing Gaussian noise from the image.
'''


def gaussian_blur(image, kernel=(5, 5)):
    return cv2.GaussianBlur(image, kernel, 0)


'''
Here, the function cv2.medianBlur() computes the median of all the pixels 
under the kernel window and the central pixel is replaced with this median value. 
This is highly effective in removing salt-and-pepper noise. 
One interesting thing to note is that, in the Gaussian and box filters, 
the filtered value for the central element can be a value which may not exist in the original image.
However this is not the case in median filtering, since the central element is always replaced by some pixel value in the image.
This reduces the noise effectively. The kernel size must be a positive odd integer.
'''


def median_blur(image, kernel=5):
    return cv2.medianBlur(image, kernel)


'''
This is not the case for the bilateral filter, cv2.bilateralFilter(),
which was defined for, and is highly effective at noise removal while preserving edges. 
But the operation is slower compared to other filters. 
We already saw that a Gaussian filter takes the a neighborhood around the pixel and finds its Gaussian weighted average. 
This Gaussian filter is a function of space alone, that is, nearby pixels are considered while filtering. 
It does not consider whether pixels have almost the same intensity value and does not consider 
whether the pixel lies on an edge or not. 
The resulting effect is that Gaussian filters tend to blur edges, which is undesirable.

The bilateral filter also uses a Gaussian filter in the space domain, 
but it also uses one more (multiplicative) Gaussian filter component which is a function of pixel intensity differences. 
The Gaussian function of space makes sure that only pixels are ‘spatial neighbors’ are considered for filtering, 
while the Gaussian component applied in the intensity domain (a Gaussian function of intensity differences) ensures 
that only those pixels with intensities similar to that of the central pixel (‘intensity neighbors’) are included 
to compute the blurred intensity value. As a result, this method preserves edges, since for pixels lying near edges, 
neighboring pixels placed on the other side of the edge,
and therefore exhibiting large intensity variations when compared to the central pixel, will not be included for blurring.
'''


def bilateral(image):
    return cv2.bilateralFilter(image, 9, 75, 75)
