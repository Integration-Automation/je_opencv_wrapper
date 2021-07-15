import cv2

'''
邊緣檢測用
'''

"""
First argument is our input image. 
Second and third arguments are our minVal and maxVal respectively. 
Third argument is aperture_size. 
It is the size of Sobel kernel used for find image gradients. 
By default it is 3. Last argument is L2gradient which specifies the equation for finding gradient magnitude. 
If it is True, it uses the equation mentioned above which is more accurate, By default, it is False.
"""


# Canny 邊緣檢測
def canny_edge(image, edge_min=100, edge_max=200):
    return cv2.Canny(image, edge_min, edge_max)
