import cv2

from je_open_cv import template_detection

image_data_array = template_detection.find_multi_object_cv2("../test.png", "../test_template.png")

cv2.imshow("test", image_data_array[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
