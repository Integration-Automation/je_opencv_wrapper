import cv2
from PIL import ImageGrab

from je_open_cv import template_detection


def find_image_multi(image, draw_image=False):
    grab_image = ImageGrab.grab()
    return template_detection.find_multi_object_cv2_with_pil(grab_image, image, detect_threshold=0.9,
                                                             draw_image=draw_image)


image_data_array = find_image_multi("../test_template.png", draw_image=True)

print(image_data_array[1])

cv2.imshow("test", image_data_array[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
