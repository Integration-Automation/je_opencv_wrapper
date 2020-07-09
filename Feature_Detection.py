import cv2
import numpy as np
from matplotlib import pyplot as plt

class Feature_Detection():

    def __init__(self):
        pass

    '''
    For BF matcher, first we have to create the BFMatcher object using cv2.BFMatcher(). 
    It takes two optional params. First one is normType. 
    It specifies the distance measurement to be used. 
    By default, it is cv2.NORM_L2. It is good for SIFT, SURF etc (cv2.NORM_L1 is also there). 
    For binary string based descriptors like ORB, BRIEF, BRISK etc, cv2.NORM_HAMMING should be used, 
    which used Hamming distance as measurement. If ORB is using VTA_K == 3 or 4, cv2.NORM_HAMMING2 should be used.
    
    Second param is boolean variable, crossCheck which is false by default. 
    If it is true, Matcher returns only those matches with value (i,j) 
    such that i-th descriptor in set A has j-th descriptor in set B as the best match and vice-versa. 
    That is, the two features in both sets should match each other. 
    It provides consistant result, and is a good alternative to ratio test proposed by D.Lowe in SIFT paper.
    '''

    '''
    DMatch.distance - Distance between descriptors. The lower, the better it is.
    DMatch.trainIdx - Index of the descriptor in train descriptors
    DMatch.queryIdx - Index of the descriptor in query descriptors
    DMatch.imgIdx - Index of the train image.
    '''
    #ORB 暴力尋找法
    def ORB_Brute_Matching(self,Query_Image,Train_Image):
        Query_Image=cv2.imread(Query_Image,0)
        Train_Image=cv2.imread(Train_Image,0)
        ORB=cv2.ORB()
        kp1,des1=ORB.detectAndCompute(Query_Image,None)
        kp2,des2=ORB.detectAndCompute(Train_Image,None)
        BFMatch = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
        Matchers=BFMatch.match(des1,des2)
        Matchers=sorted(Matchers,key= lambda x:x.distance)
        # Draw first 10 matches.
        img3 = cv2.drawMatches(Query_Image, kp1, Train_Image, kp2, Matchers[:10], flags=2)
        plt.imshow(img3), plt.show()

    #比對圖片相似度
    def Similarity(self,Image_1,Image_2):
        try:
            #讀圖
            img1 = cv2.imread(Image_1, 0)
            img2 = cv2.imread(Image_2, 0)

            # ORB檢測器
            orb = cv2.ORB_create()
            kp1, des1 = orb.detectAndCompute(img1, None)
            kp2, des2 = orb.detectAndCompute(img2, None)

            # 特徵點
            bf = cv2.BFMatcher(cv2.NORM_HAMMING)

            # knn塞選
            matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)

            # 匹配點數目
            good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
            print(len(good))
            print(len(matches))
            similary = len(good) / len(matches)
            print("相似度:%s" % similary)
            return similary

        except:
            print('無法計算相似度')


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
    #尋找圖中的物件
    def Find_Obeject(self,Image,Find_Object):
            Tmp=(0,0)
            count=0
            Image = cv2.imread(Image,0)
            Image2 = Image.copy()
            template = cv2.imread(Find_Object,0)
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

                if count==0:
                    Tmp=top_left
                    count+=1
                else:
                    if Tmp ==top_left:
                        print('以上一張圖為基準',meth,'此方法匹配到')
                        count+=1

                cv2.rectangle(Image, top_left, bottom_right, 255, 2)
                plt.subplot(121), plt.imshow(res, cmap='gray')
                plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
                plt.subplot(122), plt.imshow(Image)
                plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
                plt.suptitle(meth)
                plt.show()

    def SIFT_Brute_Matching(self):
        pass
