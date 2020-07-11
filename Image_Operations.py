import cv2

'''
基本圖像處理用
'''

class Image_Operations():

    def __init__(self):
        pass

    def Get_Image_Properties(self,Image):
        Total=[]
        Total.append(Image.shape)
        Total.append(Image.size)
        Total.append(Image.dtype)
        return Total

    #取得圖像 行 列 通道數
    def Get_Image_Shape(self,Image):
        return Image.shape

    #取得 圖片大小
    def Get_Image_Size(self,Image):
        return Image.size

    #取得圖片類型
    def Get_Image_Type(self,Image):
        return Image.dtype

    #分割通道
    def Split_Image(self,Image):
        B,G,R=cv2.split(Image)
        return [B,G,R]

    '''
    The B,G,R channels of an image can be split into their individual planes when needed. Then,
    the individual channels can be merged back together to form a BGR image again. This can be performed by:
    
    b = img[:,:,0]
    
    Suppose, you want to make all the red pixels to zero, you need not split like this and put it equal to zero. 
    You can simply use Numpy indexing which is faster.
    
     img[:,:,2] = 0
    '''

    #組合通道
    def Merge_Image(self,B,G,R):
        return cv2.merge((B,G,R))

    '''
    If you want to create a border around the image, something like a photo frame, you can use cv2.copyMakeBorder() function.
    But it has more applications for convolution operation, zero padding etc. 
    
    This function takes following arguments:
    src - input image
    top, bottom, left, right - border width in number of pixels in corresponding directions
    borderType - Flag defining what kind of border to be added. It can be following types:
    cv2.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
    cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
    cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
    cv2.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
    cv2.BORDER_WRAP - Can’t explain, it will look like this : cdefgh|abcdefgh|abcdefg
    value - Color of border if border type is cv2.BORDER_CONSTANT
    
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    
    BLUE = [255,0,0]
    
    img1 = cv2.imread('opencv_logo.png')
    
    replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
    constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
    
    plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
    plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
    plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
    plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
    plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
    plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
    
    plt.show()
    '''

    '''
    You can add two images by OpenCV function, cv2.add() or simply by numpy operation, 
    res = img1 + img2. Both images should be of same depth and type, or second image can just be a scalar value.
    
    Note
    
    There is a difference between OpenCV addition and Numpy addition. 
    OpenCV addition is a saturated operation while Numpy addition is a modulo operation.
    
    For example, consider below sample:
    
    >>> x = np.uint8([250])
    >>> y = np.uint8([10])
    
    >>> print cv2.add(x,y) # 250+10 = 260 => 255
    [[255]]
    
    >>> print x+y          # 250+10 = 260 % 256 = 4
    [4]
    It will be more visible when you add two images. OpenCV function will provide a better result. 
    So always better stick to OpenCV functions.
    '''


    '''
    This is also image addition, but different weights are given to images so that it gives a feeling of blending or transparency. 
    Images are added as per the equation below:


    you can perform a cool transition between one image to another.

    Here I took two images to blend them together. 
    First image is given a weight of 0.7 and second image is given 0.3. cv2.addWeighted() applies following equation on the image.
    '''
    # 合併2張圖片 採用透明度
    def Image_Blending(self,Image1,Image1_Alpha,Image2,Image2_Alpha):
        return cv2.addWeighted(Image1,Image1_Alpha,Image2,Image2_Alpha,0)

    '''
    # Load two images
    img1 = cv2.imread('messi5.jpg')
    img2 = cv2.imread('opencv_logo.png')
    
    # I want to put logo on top-left corner, So I create a ROI
    rows,cols,channels = img2.shape
    roi = img1[0:rows, 0:cols ]
    
    # Now create a mask of logo and create its inverse mask also
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    
    # Now black-out the area of logo in ROI
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
    
    # Take only region of logo from logo image.
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
    
    # Put logo in ROI and modify the main image
    dst = cv2.add(img1_bg,img2_fg)
    img1[0:rows, 0:cols ] = dst
    
    cv2.imshow('res',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    def Image_Logo():
        pass
    '''