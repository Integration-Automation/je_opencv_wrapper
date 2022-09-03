import cv2
import numpy as np


def ignore_same_image(image, points, threshold, width, height, draw_image=False):
    flag = False
    image_points_list = []
    for left, top in points:
        for image_x_y in image_points_list:
            if ((left - image_x_y[0]) ** 2 + (top - image_x_y[1]) ** 2) < threshold ** 2:
                break
        else:
            right = left + width
            bottom = top + height
            image_data_tuple = left, top, right, bottom
            if draw_image:
                draw_detect(image, (left, top), right, bottom)
            image_points_list.append(image_data_tuple)
            flag = True

    return flag, image_points_list


def draw_detect(image, points, right, bottom):
    cv2.rectangle(image, points, (right, bottom), (0, 0, 255), 2)


def detect(image, template, detect_threshold=1, draw_image=False):
    image_points_tuple = ()
    w, h = template.shape[::-1]
    flag = False
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    threshold = detect_threshold
    loc = np.where(res >= threshold)
    for points in zip(*loc[::-1]):
        right = points[0] + w
        bottom = points[1] + h
        image_points_tuple = points[0], points[1], right, bottom
        if draw_image:
            draw_detect(image, points, right, bottom)
        flag = True
        break

    if draw_image:
        return flag, image_points_tuple, image
    else:
        return flag, image_points_tuple


def detect_multi(image, template, detect_threshold=1, draw_image=False):
    width, height = template.shape[::-1]
    res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    threshold = detect_threshold
    loc = np.where(res >= threshold)
    points = zip(*loc[::-1])

    if draw_image:
        return image, ignore_same_image(image, points, min(template.shape[0], template.shape[1]), width, height,
                                        draw_image)
    else:
        return ignore_same_image(image, points, min(template.shape[0], template.shape[1]), width, height)


def image_translate(image, template):
    if type(image) is str:
        image = cv2.imread(image, 0)
    else:
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    if type(template) is str:
        template = cv2.imread(template, 0)
    else:
        template = cv2.cvtColor(np.array(template), cv2.COLOR_RGB2GRAY)
    return image, template


def find_object(image, template, detect_threshold=1, draw_image=False):
    new_image, new_template = image_translate(image, template)
    return detect(image=new_image, template=new_template, detect_threshold=detect_threshold, draw_image=draw_image)


def find_multi_object(image, template, detect_threshold=1, draw_image=False):
    new_image, new_template = image_translate(image, template)
    return detect_multi(image=new_image, template=new_template, detect_threshold=detect_threshold, draw_image=draw_image)
