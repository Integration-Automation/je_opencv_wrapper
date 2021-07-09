import cv2

'''
基本圖像處理用
'''


# 取得圖像 行 列 通道數
def get_image_properties(image):
    total = [image.shape, image.size, image.dtype]
    return total


def get_image_shape(image):
    return image.shape


# 取得 圖片大小
def get_image_size(image):
    return image.size


# 取得圖片類型
def get_image_type(image):
    return image.dtype


# 分割通道
def split_image(image):
    B, G, R = cv2.split(image)
    return [B, G, R]


'''
The B,G,R channels of an image can be split into their individual planes when needed. Then,
the individual channels can be merged back together to form a BGR image again. This can be performed by:

b = img[:,:,0]

Suppose, you want to make all the red pixels to zero, you need not split like this and put it equal to zero. 
You can simply use Numpy indexing which is faster.

 img[:,:,2] = 0
'''


# 組合通道
def merge_image(B, G, R):
    return cv2.merge((B, G, R))


# 合併2張圖片 採用透明度
def image_Blending(image1, image1_Alpha, image2, image2_Alpha):
    return cv2.addWeighted(image1, image1_Alpha, image2, image2_Alpha, 0)
