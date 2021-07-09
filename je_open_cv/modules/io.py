import cv2

'''
基本的輸出入圖片
'''


def read_image(image, flag=1):
    return cv2.imread(image, flag)


def show_image(image, window_name='image'):
    cv2.imshow(window_name, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


def output_image(image, file_name='image'):
    cv2.imwrite(file_name, image)
