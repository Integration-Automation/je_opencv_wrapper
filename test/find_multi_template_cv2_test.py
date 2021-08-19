import cv2

from je_open_cv import template_detection

image_data_array = template_detection.find_multi_object("../test.png", "../test_template.png", detect_threshold=0.9, draw_image=True)

print(image_data_array)

cv2.imshow("test", image_data_array[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
