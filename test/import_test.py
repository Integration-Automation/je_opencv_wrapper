import cv2

from je_open_cv.modules import template_detection

image_data_array = template_detection.find_object("../test.png", "../test_template.png")

print("top_left", image_data_array[2][0], image_data_array[2][1])
print("bottom_right", image_data_array[3][0], image_data_array[3][1])

height = image_data_array[3][0] - image_data_array[2][0]
width = image_data_array[3][1] - image_data_array[2][1]

print(height, width)

center = [int(height / 2), int(width / 2)]

print(center)

template_center = [image_data_array[2][0] + center[0], image_data_array[2][1] + center[1]]

print(template_center)

cv2.imshow("test", image_data_array[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
