import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
對圖片的物件進行尋找
'''
class Template_Detection():

    def __init__(self):
        pass

    '''
      原理:
      輸入兩張影像，分別為 image、template
      不斷滑動 template，得到 image 上各個位置的比較值，比較值代表相似程度
      然後將 image 左上角位置，作為 result 比較值的存放位置
      完成後可得到 result
      可用 minMaxLoc() 函式，找出結果圖的最大或最小值，定位出搜尋位置
    
      限制 :
    
      物體有旋轉時，會找不到
      物體大小改變時，會找不到
    
      參數
      image-被尋找的圖片-必須為 8-bit or 32-bit
    
      template-尋找的物品圖片
    
      size 不能大於 image，且格式需一致
    
      method-比對的方法
    
      result-比較的結果，格式為 numpy.ndarray (dtype=float32)-可傳入想儲存結果的 array
    
      CV_TM_SQDIFF : 平方差，越小越相似
    
      CV_TM_SQDIFF_NORMED : 正規化平方差，越小越相似 保證當 pixel 亮度都乘上同一係數時，相似度不變
    
      CV_TM_CCORR : 相關係數，越大越相似
    
      CV_TM_CCORR_NORMED : 正規化相關係數，越大越相似 保證當 pixel 亮度都乘上同一係數時，相似度不變
    
      CV_TM_CCOEFF : 去掉直流成份的相關係數，越大越相似
    
      CV_TM_CCOEFF_NORMED : 正規化 去掉直流成份的相關係數 保證當 pixel 亮度都乘上同一係數時，相似度不變
      計算出的相關係數被限制在了 -1 到 1 之間
      1 表示完全相同
      -1 表示亮度正好相反
      0 表示没有線性相關
    
      詳情 :
      https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_template_matching/py_template_matching.html?highlight=matchtemplate
      '''


    # 尋找圖中的物件
    def Find_Obeject(self, Image, Find_Object):
        Tmp = (0, 0)
        count = 0
        Image = cv2.imread(Image, 0)
        Image2 = Image.copy()
        template = cv2.imread(Find_Object, 0)
        w = template.shape[1]
        h = template.shape[0]

        # All the 6 methods for comparison in a list
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                   'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

        for meth in methods:
            Image = Image2.copy()
            method = eval(meth)

            # Apply template Matching
            res = cv2.matchTemplate(Image, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)

            if count == 0:
                Tmp = top_left
                count += 1
            else:
                if Tmp == top_left:
                    print('以上一張圖為基準', meth, '此方法與上一張結果一樣')
                    count += 1

            cv2.rectangle(Image, top_left, bottom_right, 255, 2)
            plt.subplot(121), plt.imshow(res, cmap='gray')
            plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(Image)
            plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            plt.suptitle(meth)
            plt.show()

    '''
    尋找圖中的多個重複物件
    which occurs only once in the image. 
    Suppose you are searching for an object which has multiple occurances, cv2.
    minMaxLoc() won’t give you all the locations. In that case, we will use thresholding.
    '''
    def Find_Multi_Object(self,Image_RGB,Template):
        Image_RGB = cv2.imread(Image_RGB)
        Image_GRAY = cv2.cvtColor(Image_RGB, cv2.COLOR_BGR2GRAY)
        Template = cv2.imread(Template, 0)
        w, h = Template.shape[::-1]

        res = cv2.matchTemplate(Image_GRAY, Template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(Image_RGB, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        return Image_RGB