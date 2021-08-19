import cv2

from je_open_cv import template_detection

image_data_array = template_detection.find_object("../test.png", "../test_template.png", detect_threshold=0.9, draw_image=True)

print(image_data_array)

if image_data_array[0] is True:
    height = image_data_array[1][2] - image_data_array[1][0]
    width = image_data_array[1][3] - image_data_array[1][1]
    center = [int(height / 2), int(width / 2)]
    print(center)

cv2.imshow("test", image_data_array[2])
cv2.waitKey(0)
cv2.destroyAllWindows()
