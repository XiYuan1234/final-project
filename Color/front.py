import tkinter as tk
from tkinter import *

import heapq
from PIL import Image, ImageTk
import tkinter.font as tkFont
import pymysql

window = tk.Tk()
window.title("Color Emoji Filter")
window.geometry('600x600')
ft1 = tkFont.Font(family='Fixdsys', slant=tkFont.ITALIC)
a = tk.Label(window, text="Main color", bg='red', font=ft1, width=15, height=1, relief=GROOVE)
a.place(relx=0.15, y=80)
e5 = tk.Entry(window, show="", )
e5.place(relx=0.4, y=80)
a1 = tk.Label(window, text="Second color", bg='green', font=ft1, width=15, height=1, relief=GROOVE)
a1.place(relx=0.15, y=160)
e1 = tk.Entry(window, show="", )
e1.place(relx=0.4, y=160)
a3 = tk.Label(window, text="Third color", bg='cyan', font=ft1, width=15, height=1, relief=GROOVE)
a3.place(relx=0.15, y=240)
e3 = tk.Entry(window, show="", )
e3.place(relx=0.4, y=240)


def NEXT():
    try:
        v1 = e5.get()
        v2 = e1.get()
        v3 = e3.get()
        db = pymysql.connect("localhost", "root", "123456", "memes")
        cursor = db.cursor()
        cursor.execute('SELECT color1 from `memes`')
        data = cursor.fetchall()
        cursor.execute('SELECT color2 from `memes`')
        data1 = cursor.fetchall()
        cursor.execute('SELECT color3 from `memes`')
        data2 = cursor.fetchall()
        q = 0
        a1, a2, a3, a4, a5, a6, a7, a8, a9, d = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        zy = []
        while q < 1658:
            str_array1 = ','.join(map(str, data[q]))
            str_array2 = ','.join(map(str, data1[q]))
            str_array3 = ','.join(map(str, data2[q]))

            if v1 == str_array1:
                a1 += 10
            if v1 == str_array2:
                a2 += 9
            if v1 == str_array3:
                a3 += 8
            if v2 == str_array1:
                a4 += 6
            if v2 == str_array2:
                a5 += 8
            if v2 == str_array3:
                a6 += 5
            if v3 == str_array3:
                a7 += 8
            if v3 == str_array2:
                a8 += 2
            if v3 == str_array1:
                a9 += 1
            # print(a1, a2, a3, a4, a5, a6, a7, a8, a9)
            d = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 - q * 0.001
            zy.append(d)
            a1, a2, a3, a4, a5, a6, a7, a8, a9, d = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            q += 1
        windowshow = tk.Toplevel(window)
        windowshow.title("OUTPUT")
        windowshow.geometry('1600x1600')

        max_num_index_list = list(map(zy.index, heapq.nlargest(18, zy)))

        try:
            cursor.execute('SELECT imagename from `memes`')
            names = []
            for name in cursor.fetchall():
                names.append(name)
            i = 0
            r = []
            while i < 18:
                str_array = ','.join(map(str, names[max_num_index_list[i]]))
                sql_getimage = "SELECT `imagelink` from `memes` WHERE `imagename` = %s"
                cursor.execute(sql_getimage, [str_array])
                for link in cursor.fetchall():
                    r.append(link)
                i += 1
        except pymysql.Error as e:
            print(e)
            print('Load failed')
        str_array = ','.join(map(str, r[9]))

        def resize(w, h, w_box, h_box, pil_image):
            f1 = 1.0 * w_box / w
            f2 = 1.0 * h_box / h
            factor = min([f1, f2])

            width = int(w * factor)
            height = int(h * factor)
            return pil_image.resize((width, height), Image.ANTIALIAS)

        w_box = 300
        h_box = 300
        img1 = Image.open(str_array)
        w, h = img1.size
        pil_image_resized = resize(w, h, w_box, h_box, img1)
        tk_image1 = ImageTk.PhotoImage(pil_image_resized)
        p1 = tk.Label(windowshow, image=tk_image1, width=w_box, height=h_box)
        p1.place(relx=0.0, y=0)

        str_array = ','.join(map(str, r[10]))
        img2 = Image.open(str_array)
        w, h = img2.size
        pil_image_resized = resize(w, h, w_box, h_box, img2)
        tk_image2 = ImageTk.PhotoImage(pil_image_resized)
        p2 = tk.Label(windowshow, image=tk_image2, compound=tk.CENTER, width=w_box, height=h_box)
        p2.place(relx=0.0, y=400)

        str_array = ','.join(map(str, r[11]))
        img3 = Image.open(str_array)
        w, h = img3.size
        pil_image_resized = resize(w, h, w_box, h_box, img3)
        tk_image3 = ImageTk.PhotoImage(pil_image_resized)
        p3 = tk.Label(windowshow, image=tk_image3, compound=tk.CENTER, width=w_box, height=h_box)
        p3.place(relx=0.0, y=700)

        str_array = ','.join(map(str, r[12]))
        img4 = Image.open(str_array)
        w, h = img4.size
        pil_image_resized = resize(w, h, w_box, h_box, img4)
        tk_image4 = ImageTk.PhotoImage(pil_image_resized)
        p3 = tk.Label(windowshow, image=tk_image4, compound=tk.CENTER)
        p3.place(x=400, y=0)

        str_array = ','.join(map(str, r[13]))
        img5 = Image.open(str_array)
        w, h = img5.size
        pil_image_resized = resize(w, h, w_box, h_box, img5)
        tk_image5 = ImageTk.PhotoImage(pil_image_resized)
        p4 = tk.Label(windowshow, image=tk_image5, compound=tk.CENTER)
        p4.place(x=400, y=400)

        str_array = ','.join(map(str, r[14]))
        img6 = Image.open(str_array)
        w, h = img6.size
        pil_image_resized = resize(w, h, w_box, h_box, img6)
        tk_image6 = ImageTk.PhotoImage(pil_image_resized)
        p5 = tk.Label(windowshow, image=tk_image6, compound=tk.CENTER)
        p5.place(x=400, y=700)

        str_array = ','.join(map(str, r[15]))
        img7 = Image.open(str_array)
        w, h = img7.size
        pil_image_resized = resize(w, h, w_box, h_box, img7)
        tk_image7 = ImageTk.PhotoImage(pil_image_resized)
        p5 = tk.Label(windowshow, image=tk_image7, compound=tk.CENTER)
        p5.place(x=800, y=0)

        str_array = ','.join(map(str, r[16]))
        img8 = Image.open(str_array)
        w, h = img8.size
        pil_image_resized = resize(w, h, w_box, h_box, img8)
        tk_image8 = ImageTk.PhotoImage(pil_image_resized)
        p6 = tk.Label(windowshow, image=tk_image8, compound=tk.CENTER, width=w_box, height=h_box)
        p6.place(x=800, y=400)

        str_array = ','.join(map(str, r[17]))
        img9 = Image.open(str_array)
        w, h = img9.size
        pil_image_resized = resize(w, h, w_box, h_box, img9)
        tk_image9 = ImageTk.PhotoImage(pil_image_resized)
        p6 = tk.Label(windowshow, image=tk_image9, compound=tk.CENTER)
        p6.place(x=800, y=700)

        windowshow.mainloop()

    except pymysql.Error as e:
        print(e)
        print('Database operation error')

    finally:
        if db:
            db.close()


def SEARCH():
    try:
        v1 = e5.get()
        v2 = e1.get()
        v3 = e3.get()
        db = pymysql.connect("localhost", "root", "123456", "memes")
        cursor = db.cursor()
        cursor.execute('SELECT color1 from `memes`')
        data = cursor.fetchall()
        cursor.execute('SELECT color2 from `memes`')
        data1 = cursor.fetchall()
        cursor.execute('SELECT color3 from `memes`')
        data2 = cursor.fetchall()
        q = 0
        a1, a2, a3, a4, a5, a6, a7, a8, a9, d = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        zy = []
        while q < 1658:
            str_array1 = ','.join(map(str, data[q]))
            str_array2 = ','.join(map(str, data1[q]))
            str_array3 = ','.join(map(str, data2[q]))

            if v1 == str_array1:
                a1 += 10
            if v1 == str_array2:
                a2 += 9
            if v1 == str_array3:
                a3 += 8
            if v2 == str_array1:
                a4 += 6
            if v2 == str_array2:
                a5 += 8
            if v2 == str_array3:
                a6 += 5
            if v3 == str_array3:
                a7 += 8
            if v3 == str_array2:
                a8 += 2
            if v3 == str_array1:
                a9 += 1
            # print(a1, a2, a3, a4, a5, a6, a7, a8, a9)
            d = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 - q * 0.001
            zy.append(d)
            a1, a2, a3, a4, a5, a6, a7, a8, a9, d = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
            q += 1
        print(zy)
        windowshow = tk.Toplevel(window)
        windowshow.title("OUTPUT")
        windowshow.geometry('1600x1600')
        c = tk.Button(windowshow, text='next', width=10, height=2, command=NEXT)
        c.place(x=1300, y=500)

        max_num_index_list = list(map(zy.index, heapq.nlargest(18, zy)))

        try:
            cursor.execute('SELECT imagename from `memes`')
            names = []
            for name in cursor.fetchall():
                names.append(name)
            i = 0
            r = []
            while i < 18:
                str_array = ','.join(map(str, names[max_num_index_list[i]]))
                sql_getimage = "SELECT `imagelink` from `memes` WHERE `imagename` = %s"
                cursor.execute(sql_getimage, [str_array])
                for link in cursor.fetchall():
                    r.append(link)
                i += 1
        except pymysql.Error as e:
            print(e)
            print('Load failed')
        str_array = ','.join(map(str, r[0]))

        def resize(w, h, w_box, h_box, pil_image):
            f1 = 1.0 * w_box / w
            f2 = 1.0 * h_box / h
            factor = min([f1, f2])

            width = int(w * factor)
            height = int(h * factor)
            return pil_image.resize((width, height), Image.ANTIALIAS)

        w_box = 300
        h_box = 300
        img1 = Image.open(str_array)
        w, h = img1.size
        pil_image_resized = resize(w, h, w_box, h_box, img1)
        tk_image1 = ImageTk.PhotoImage(pil_image_resized)
        p1 = tk.Label(windowshow, image=tk_image1, width=w_box, height=h_box)
        p1.place(relx=0.0, y=0)

        str_array = ','.join(map(str, r[1]))
        img2 = Image.open(str_array)
        w, h = img2.size
        pil_image_resized = resize(w, h, w_box, h_box, img2)
        tk_image2 = ImageTk.PhotoImage(pil_image_resized)
        p2 = tk.Label(windowshow, image=tk_image2, compound=tk.CENTER, width=w_box, height=h_box)
        p2.place(relx=0.0, y=400)

        str_array = ','.join(map(str, r[2]))
        img3 = Image.open(str_array)
        w, h = img3.size
        pil_image_resized = resize(w, h, w_box, h_box, img3)
        tk_image3 = ImageTk.PhotoImage(pil_image_resized)
        p3 = tk.Label(windowshow, image=tk_image3, compound=tk.CENTER, width=w_box, height=h_box)
        p3.place(relx=0.0, y=700)

        str_array = ','.join(map(str, r[3]))
        img4 = Image.open(str_array)
        w, h = img4.size
        pil_image_resized = resize(w, h, w_box, h_box, img4)
        tk_image4 = ImageTk.PhotoImage(pil_image_resized)
        p3 = tk.Label(windowshow, image=tk_image4, compound=tk.CENTER)
        p3.place(x=400, y=0)

        str_array = ','.join(map(str, r[4]))
        img5 = Image.open(str_array)
        w, h = img5.size
        pil_image_resized = resize(w, h, w_box, h_box, img5)
        tk_image5 = ImageTk.PhotoImage(pil_image_resized)
        p4 = tk.Label(windowshow, image=tk_image5, compound=tk.CENTER)
        p4.place(x=400, y=400)

        str_array = ','.join(map(str, r[5]))
        img6 = Image.open(str_array)
        w, h = img6.size
        pil_image_resized = resize(w, h, w_box, h_box, img6)
        tk_image6 = ImageTk.PhotoImage(pil_image_resized)
        p5 = tk.Label(windowshow, image=tk_image6, compound=tk.CENTER)
        p5.place(x=400, y=700)

        str_array = ','.join(map(str, r[6]))
        img7 = Image.open(str_array)
        w, h = img7.size
        pil_image_resized = resize(w, h, w_box, h_box, img7)
        tk_image7 = ImageTk.PhotoImage(pil_image_resized)
        p5 = tk.Label(windowshow, image=tk_image7, compound=tk.CENTER)
        p5.place(x=800, y=0)

        str_array = ','.join(map(str, r[7]))
        img8 = Image.open(str_array)
        w, h = img8.size
        pil_image_resized = resize(w, h, w_box, h_box, img8)
        tk_image8 = ImageTk.PhotoImage(pil_image_resized)
        p6 = tk.Label(windowshow, image=tk_image8, compound=tk.CENTER, width=w_box, height=h_box)
        p6.place(x=800, y=400)

        str_array = ','.join(map(str, r[8]))
        img9 = Image.open(str_array)
        w, h = img9.size
        pil_image_resized = resize(w, h, w_box, h_box, img9)
        tk_image9 = ImageTk.PhotoImage(pil_image_resized)
        p6 = tk.Label(windowshow, image=tk_image9, compound=tk.CENTER)
        p6.place(x=800, y=700)

        windowshow.mainloop()

    except pymysql.Error as e:
        print(e)
        print('Database operation error')

    finally:
        if db:
            db.close()


if __name__ == '__main__':
    b = tk.Button(window, text='search', width=10, height=2, command=SEARCH)
    b.place(relx=0.4, y=300)
    canvas = tk.Canvas(window, height=600, width=600)
    img = Image.open('背景.jpg')
    photo = ImageTk.PhotoImage(img)
    image = canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.place(relx=0, y=350)
    window.mainloop()
