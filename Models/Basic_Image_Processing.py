import cv2
import numpy as np
from matplotlib import pyplot as plt

class Basic_Image_Processing():

    def __init__(self):
        pass

    '''
    OpenCV提供了150多種顏色空間轉換方法。但是，我們將只研究兩個使用最廣泛的模型，即BGR Gray和BGR HSV
    
    There are more than 150 color-space conversion methods available in OpenCV. 
     But we will look into only two which are most widely used ones, BGR <- Gray and BGR <- HSV.

    對於顏色轉換，我們使用where 函數確定轉換類型。cv2.cvtColor(input_image, flag)
    For color conversion, we use the function cv2.cvtColor(input_image, flag) where flag determines the type of conversion.

    對於BGR 灰色轉換，我們使用標誌cv2.COLOR_BGR2GRAY。
     同樣，對於BGR HSV，我們使用標誌cv2.COLOR_BGR2HSV。
      要獲取其他標誌，只需在Python終端中運行以下命令：
    For BGR -> Gray conversion we use the flags cv2.COLOR_BGR2GRAY. Similarly for BGR -> HSV, we use the flag cv2.COLOR_BGR2HSV.
     To get other flags, just run following commands in your Python terminal
    
    import cv2
    flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    print (flags)
    '''
    def Change_Color(self,Image,Flag=cv2.COLOR_BGR2HSV):
        return cv2.cvtColor(Image,Flag)

    '''
    OpenCV提供了兩個轉換函數，cv2.warpAffine和cv2.warpPerspective，您可以使用它們進行各種轉換。
     cv2.warpAffine採用2x3轉換矩陣，而cv2.warpPerspective採用3x3轉換矩陣作為輸入。
    
    Transformations
     OpenCV provides two transformation functions, cv2.warpAffine and cv2.warpPerspective, 
      with which you can have all kinds of transformations. 
       cv2.warpAffine takes a 2x3 transformation matrix while cv2.warpPerspective takes a 3x3 transformation matrix as input.

    縮放只是調整圖像的大小。為此，OpenCV帶有一個函數cv2.resize（）。
     圖像的大小可以手動指定，也可以指定縮放比例。
      使用了不同的插值方法。首選插值方法是cv2.INTER_AREA用於縮小，cv2.INTER_CUBIC（慢）和cv2.INTER_LINEAR用於縮放。
       默認情況下，出於所有調整大小的目的，使用的插值方法是cv2.INTER_LINEAR。您可以使用以下方法之一調整輸入圖像的大小
       
    Scaling
     Scaling is just resizing of the image. 
      OpenCV comes with a function cv2.resize() for this purpose. 
       The size of the image can be specified manually, or you can specify the scaling factor. 
        Different interpolation methods are used. 
         Preferable interpolation methods are cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming. 
          By default, interpolation method used is cv2.INTER_LINEAR for all resizing purposes. 
           You can resize an input image either of following methods:
    
    res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
    #OR
    height, width = img.shape[:2]
    res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
    '''
    def Resize(self,Image,FX,FY,Mode):
        return cv2.resize(Image,None,FX,FY,Mode)


    '''
    Translation is the shifting of object’s location. 
     If you know the shift in (x,y) direction, let it be (t_x,t_y), you can create the transformation matrix 
    
    You can take make it into a Numpy array of type np.float32 and pass it into cv2.warpAffine() function. 
     See below example for a shift of (100,50):
    '''
    def Move(self,Image,Martix1=[1, 0, 100],Martix2=[0, 1, 50]):
        rows, cols = Image.shape
        M = np.float32([Martix1,Martix2 ])
        return cv2.warpAffine(Image, M, (cols, rows))

    '''
    通過以下形式的變換矩陣可以將圖像旋轉一個角度
    Rotation of an image for an angle  is achieved by the transformation matrix of the form
    '''
    def Rotation(self,Image,Angle):
        rows, cols = Image.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), Angle, 1)
        return cv2.warpAffine(Image, M, (cols, rows))

    def Affine(self,Image,Points1=[[50, 50], [200, 50], [50, 200]],Points2=[[10, 100], [200, 50], [100, 250]]):
        rows, cols, ch = Image.shape
        pts1 = np.float32(Points1)
        pts2 = np.float32(Points2)
        M = cv2.getAffineTransform(pts1, pts2)
        dst = cv2.warpAffine(Image, M, (cols, rows))
        plt.subplot(121), plt.imshow(Image), plt.title('Input')
        plt.subplot(122), plt.imshow(dst), plt.title('Output')
        plt.show()
        return cv2.warpAffine(Image, M, (cols, rows))

    def Perspective(self,Image,
                    Points1=[[56, 65], [368, 52], [28, 387], [389, 390]],
                    Points2=[[0, 0], [300, 0], [0, 300], [300, 300]],
                    Size=(300,300)):
        rows, cols, ch = Image.shape
        pts1 = np.float32(Points1)
        pts2 = np.float32(Points2)
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(Image, M, Size)
        plt.subplot(121), plt.imshow(Image), plt.title('Input')
        plt.subplot(122), plt.imshow(dst), plt.title('Output')
        plt.show()
        return dst

    def Crop_Image(self,Image,X,Y,W,H):
        W=W-X
        H=H-Y
        return Image[Y:Y+H, X:X+W]
