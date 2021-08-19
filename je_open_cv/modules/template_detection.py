import cv2
import numpy as np

'''
對圖片的物件進行尋找
'''

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


def ignore_same_image(image, points, threshold, width, height, draw_image=False):
    flag = False
    image_points_list = []
    for left, top in points:
        for image_x_y in image_points_list:
            if ((left - image_x_y[0]) ** 2 + (top - image_x_y[1]) ** 2) < threshold ** 2:
                break
        else:
            right = left + width
            bottom = top + height
            image_data_tuple = left, top, right, bottom
            if draw_image:
                draw_detect(image, (left, top), right, bottom)
            image_points_list.append(image_data_tuple)
            flag = True

    return flag, image_points_list


def draw_detect(image, points, right, bottom):
    cv2.rectangle(image, points, (right, bottom), (0, 0, 255), 2)


def detect(image, template, detect_threshold=1, draw_image=False):
    image_points_tuple = ()
    w, h = template.shape[::-1]
    flag = False
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    threshold = detect_threshold
    loc = np.where(res >= threshold)
    for points in zip(*loc[::-1]):
        right = points[0] + w
        bottom = points[1] + h
        image_points_tuple = points[0], points[1], right, bottom
        if draw_image:
            draw_detect(image, points, right, bottom)
        flag = True
        break

    if draw_image:
        return flag, image_points_tuple, image
    else:
        return flag, image_points_tuple


def detect_multi(image, template, detect_threshold=1, draw_image=False):
    width, height = template.shape[::-1]
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    threshold = detect_threshold
    loc = np.where(res >= threshold)
    points = zip(*loc[::-1])

    if draw_image:
        return image, ignore_same_image(image, points, min(template.shape[0], template.shape[1]), width, height,
                                        draw_image)
    else:
        return ignore_same_image(image, points, min(template.shape[0], template.shape[1]), width, height)


# 尋找圖中的物件
def find_object(image, template, detect_threshold=1, draw_image=False):
    if type(image) is str:
        image = cv2.imread(image, 0)
    else:
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    if type(template) is str:
        template = cv2.imread(template, 0)
    else:
        template = cv2.cvtColor(np.array(template), cv2.COLOR_RGB2GRAY)
    return detect(image=image, template=template, detect_threshold=detect_threshold, draw_image=draw_image)


'''
尋找圖中的多個重複物件
which occurs only once in the image. 
Suppose you are searching for an object which has multiple occurances, cv2.
minMaxLoc() won’t give you all the locations. In that case, we will use thresholding.
'''


def find_multi_object(image, template, detect_threshold=1, draw_image=False):
    if type(image) is str:
        image = cv2.imread(image, 0)
    else:
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    if type(template) is str:
        template = cv2.imread(template, 0)
    else:
        template = cv2.cvtColor(np.array(template), cv2.COLOR_RGB2GRAY)
    return detect_multi(image=image, template=template, detect_threshold=detect_threshold, draw_image=draw_image)
