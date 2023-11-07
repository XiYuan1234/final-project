import colorsys
import math

import cv2
import numpy as np
import webcolors
import PIL.Image as Image

import colorList

# 使用PIL截取图像，然后将RGB转为HSV进行判断，统计判断颜色，最后输出RGB值
import colorList


def get_dominant_color(image):
    max_score = 0.0001
    sec_score = 0.0001
    trd_score = 0.0001
    dominant_color = (255, 255, 255)
    secondary_color = (255, 255, 255)
    third_color = (255, 255, 255)
    tem = (255, 255, 255)
    for count, (r, g, b) in image.getcolors(image.size[0] * image.size[1]):
        # 转为HSV标准
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        y = (y - 16.0) / (235 - 16)
        hsv = BGR2HSV(r, g, b)

        # 忽略高亮色
        if y > 0.9:
            continue
        score = (saturation + 0.1) * count
        tem = (r, g, b)
        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)
        if max_score > score > sec_score and ColorDistance(dominant_color, tem) > 50:
            sec_score = score
            secondary_color = tem
        if max_score > sec_score > score > trd_score and ColorDistance(dominant_color, tem) > 50 and ColorDistance(
                secondary_color, tem) > 50:
            trd_score = score
            third_color = tem
        if ColorDistance(dominant_color, tem) < 50:
            secondary_color = (255, 255, 255)
        if ColorDistance(dominant_color, tem) < 50 and ColorDistance(secondary_color, tem) < 50:
            third_color = (255, 255, 255)
    return dominant_color, secondary_color, third_color, get_colour_name(dominant_color), get_colour_name(secondary_color), get_colour_name(third_color)


def ColorDistance(rgb_1, rgb_2):
    R_1, G_1, B_1 = rgb_1
    R_2, G_2, B_2 = rgb_2
    rmean = (R_1 + R_2) / 2
    R = R_1 - R_2
    G = G_1 - G_2
    B = B_1 - B_2
    return math.sqrt((2 + rmean / 256) * (R ** 2) + 4 * (G ** 2) + (2 + (255 - rmean) / 256) * (B ** 2))


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def BGR2HSV(R, G, B):
    color = np.uint8([[[B, G, R]]])
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    hsv = np.ndarray.tolist(hsv_color)
    H = hsv[0][0][0]
    S = hsv[0][0][1]
    V = hsv[0][0][2]
    return H, S, V


def get_colour_name(requested_colour):
    try:
        closest_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
    return closest_name


if __name__ == '__main__':
    image = Image.open('image1.jpg')
    image = image.convert('RGB')
    print(get_dominant_color(image))
