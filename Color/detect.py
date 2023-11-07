# coding=utf-8
import cv2
import numpy as np
import sql as sql

import colorList
import pymysql


def get_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    a = {}
    color_dict = colorList.getColorList()
    for d in color_dict:
        mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
        cv2.imwrite(d + '.jpg', mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        # binary = cv2.erode(binary, None, iterations=2)
        # binary = cv2.dilate(binary, None, iterations=2)
        kernel = np.ones((5, 5), np.uint8)
        binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        img, cnts, hiera = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        for c in cnts:
            sum += cv2.contourArea(c)
        a[d] = sum

    return order_dict(a, 3)


def order_dict(dicts, n):
    result = []
    result1 = []
    p = sorted([(k, v) for k, v in dicts.items()], reverse=True)
    s = set()
    for i in p:
        s.add(i[1])
    for i in sorted(s, reverse=True)[:n]:
        for j in p:
            if j[1] == i:
                result.append(j)
    for r in result:
        if r[1] > 5000:
            result1.append((r[0]))

    return result1


if __name__ == '__main__':
    try:
        db = pymysql.connect("localhost", "root", "123456", "memes")
        cursor = db.cursor()
        cursor.execute('SELECT imagelink from `memes`')
        a = []
        for link in cursor.fetchall():
            a.append(link)
        n = [x for x in range(1659)]
        for i in n:
            str_array = ','.join(map(str, a[i]))
            frame = cv2.imread(str_array)
            r = get_color(frame)
            sql_update1 = "UPDATE `memes` SET color1 = %s where `imagelink` = %s"
            sql_update2 = "UPDATE `memes` SET color2 = %s where `imagelink` = %s"
            sql_update3 = "UPDATE `memes` SET color3 = %s where `imagelink` = %s"
            try:
                cursor.execute(sql_update1, [r[0], str_array])
                cursor.execute(sql_update2, [r[1], str_array])
                cursor.execute(sql_update3, [r[2], str_array])
                db.commit()
                print("update success")
            except Exception as e:
                db.rollback()

        cursor.close()
    except pymysql.Error as e:
        print(e)
        print('Database operation error')
    finally:
        if db:
            db.close()
