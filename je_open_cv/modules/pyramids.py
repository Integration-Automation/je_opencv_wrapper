import cv2
import numpy as np

'''
高斯金字塔

高斯圖像融合

圖片金字塔
'''


# 降階金字塔 圖片會變小
def down_image(image):
    return cv2.pyrDown(image)


# 升階金字塔 圖片會變大
def up_image(image):
    return cv2.pyrUp(image)


'''
One application of Pyramids is Image Blending. 
For example, in image stitching, you will need to stack two images together, 
but it may not look good due to discontinuities between images. 
In that case, image blending with Pyramids gives you seamless blending without leaving much data in the images.

Load the two images of apple and orange
Find the Gaussian Pyramids for apple and orange (in this particular example, number of levels is 6)
From Gaussian Pyramids, find their Laplacian Pyramids
Now join the left half of apple and right half of orange in each levels of Laplacian Pyramids
Finally from this joint image pyramids, reconstruct the original image.

將2張圖片融合
'''

global cols


def blending_image_pyramids(image1, image2):
    # generate Gaussian pyramid for A
    global cols
    g = image1.copy()
    gpA = [g]
    for i in range(6):
        g = cv2.pyrDown(g)
        gpA.append(g)

    # generate Gaussian pyramid for B
    g = image2.copy()
    gpB = [g]
    for i in range(6):
        g = cv2.pyrDown(g)
        gpB.append(g)

    # generate Laplacian Pyramid for A
    lpA = [gpA[5]]
    for i in range(5, 0, -1):
        GE = cv2.pyrUp(gpA[i])
        L = cv2.subtract(gpA[i - 1], GE)
        lpA.append(L)

    # generate Laplacian Pyramid for B
    lpB = [gpB[5]]
    for i in range(5, 0, -1):
        GE = cv2.pyrUp(gpB[i])
        L = cv2.subtract(gpB[i - 1], GE)
        lpB.append(L)

    # Now add left and right halves of images in each level
    LS = []
    for la, lb in zip(lpA, lpB):
        rows, cols, dpt = la.shape
        ls = np.hstack((la[:, 0:cols / 2], lb[:, cols / 2:]))
        LS.append(ls)

    # now reconstruct
    ls_ = LS[0]
    for i in range(1, 6):
        ls_ = cv2.pyrUp(ls_)
        ls_ = cv2.add(ls_, LS[i])

    # image with direct connecting each half
    return np.hstack((image1[:, :cols / 2], image2[:, cols / 2:]))
