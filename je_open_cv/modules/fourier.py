import cv2
import numpy as np

'''
Numpy has an FFT package to do this. 
np.fft.fft2() provides us the frequency transform which will be a complex array. 
Its first argument is the input image, which is grayscale. 
Second argument is optional which decides the size of output array. 
If it is greater than size of input image, input image is padded with zeros before calculation of FFT. 
If it is less than input image, input image will be cropped. 
If no arguments passed, Output array size will be same as input.

Now once you got the result, zero frequency component (DC component) will be at top left corner. 
If you want to bring it to center, you need to shift the result by \frac{N}{2} in both the directions. 
This is simply done by the function, np.fft.fftshift(). 
(It is more easier to analyze). 
Once you found the frequency transform, you can find the magnitude spectrum.
'''


def fourier_numpy(image):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    return 20 * np.log(np.abs(fshift))


'''
OpenCV provides the functions cv2.dft() and cv2.idft() for this. 
It returns the same result as previous, but with two channels. 
First channel will have the real part of the result and second channel will have the imaginary part of the result. 
The input image should be converted to np.float32 first.
'''


def fourier_open_cv(image):
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    return 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
