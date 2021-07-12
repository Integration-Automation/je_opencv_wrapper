import cv2

from je_open_cv import template_detection

image_data_array = template_detection.find_object_cv2("test.png", "test_template.png")

