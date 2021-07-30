import cv2
from PIL import ImageGrab

from je_open_cv import template_detection


def find_image(image, draw_image=False):
    grab_image = ImageGrab.grab()
    return template_detection.find_object_cv2_with_pil(grab_image, image, draw_image=draw_image)


image_data_array = find_image("../test1.png", draw_image=True)

print(image_data_array[1])
print(image_data_array[2])

if len(image_data_array[2]) > 0:
    print("left_top", image_data_array[2][0], image_data_array[2][1])
    print("right_bottom", image_data_array[2][2], image_data_array[2][3])
    height = image_data_array[2][2] - image_data_array[2][0]
    width = image_data_array[2][3] - image_data_array[2][1]
    print(height, width)
    center = [int(height / 2), int(width / 2)]
    print(center)
    template_center = [image_data_array[2][0] + center[0], image_data_array[2][1] + center[1]]
    print(template_center)

cv2.imshow("test", image_data_array[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
