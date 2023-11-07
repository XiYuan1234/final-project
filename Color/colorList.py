import numpy as np
import collections


# for example：{color: [min, max]}
# {'red': [array([160,  43,  46]), array([179, 255, 255])]}

def getColorList():
    dict = collections.defaultdict(list)

    # black
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    color_list = [lower_black, upper_black]
    dict['black'] = color_list

    # gray
    lower_gray = np.array([0, 0, 46])
    upper_gray = np.array([180, 43, 220])
    color_list = [lower_gray, upper_gray]
    dict['gray'] = color_list

    # white
    lower_white = np.array([0, 0, 221])
    upper_white = np.array([180, 30, 255])
    color_list = [lower_white, upper_white]
    dict['white'] = color_list

    # red
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    color_list = [lower_red, upper_red]
    dict['red'] = color_list

    # pink
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    color_list = [lower_red, upper_red]
    dict['pink'] = color_list

    # orange
    lower_orange = np.array([26, 43, 46])
    upper_orange = np.array([34, 255, 255])
    color_list = [lower_orange, upper_orange]
    dict['orange'] = color_list

    # yellow
    lower_yellow = np.array([11, 43, 46])
    upper_yellow = np.array([25, 255, 255])
    color_list = [lower_yellow, upper_yellow]
    dict['yellow'] = color_list

    # green
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    color_list = [lower_green, upper_green]
    dict['green'] = color_list

    # cyan
    lower_cyan = np.array([78, 43, 46])
    upper_cyan = np.array([99, 255, 255])
    color_list = [lower_cyan, upper_cyan]
    dict['cyan'] = color_list

    # blue
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    color_list = [lower_blue, upper_blue]
    dict['blue'] = color_list

    # purple
    lower_purple = np.array([125, 43, 46])
    upper_purple = np.array([155, 255, 255])
    color_list = [lower_purple, upper_purple]
    dict['purple'] = color_list

    return dict


if __name__ == '__main__':
    color_dict = getColorList()
    print(color_dict)

    num = len(color_dict)
    print('num=', num)

    for d in color_dict:
        print('key=', d)
        print('value=', color_dict[d][1])
