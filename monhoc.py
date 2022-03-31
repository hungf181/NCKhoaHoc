import tkinter
from tkinter import *
from tkinter import Tk
from tkinter.ttk import *
import PIL.ImageTk, PIL.Image
import cv2
from PIL import ImageTk, Image
from cv2 import *
from database import *
from sinhvien import *
import numpy as np
import os
def listSubjects(tv):
    for item in tv.get_children():
        tv.delete(item)
    for i in getSSubjects():
        tv.insert('', END, values=i)
    tv.place(x=320, y=20)

def Monhoc(window):
    labelfrm = LabelFrame(window, width=1400, height=760, bd=0)
    labelfrm.place(x=0, y=0)
    labelframe_left = LabelFrame(labelfrm, width=750, height=750, bg='#CFCFCF')
    labelframe_left.place(x=5, y=5)
    labelframe_right = LabelFrame(labelfrm, width=610, height=750, bg='#CFCFCF')
    labelframe_right.place(x=770, y=5)
    tieude = Label(labelframe_left, text="MÔN HỌC", font=('Arial', 18), bg='#CFCFCF')
    tieude.place(relx=0.5, rely=0.04, anchor='center')

    labelframe_left_top = LabelFrame(labelframe_left, text='Thông tin môn học', width=730, height=620, bg='#CFCFCF')
    labelframe_left_top.place(x=5, y=50)

    labelframe_left_bottom = LabelFrame(labelframe_left, text='', width=730, height=60, bg='#CFCFCF')
    labelframe_left_bottom.place(x=5, y=680)
    labelframe_right_top = LabelFrame(labelframe_right, text='Đăng ký môn học', width=590, height=400, bg='#CFCFCF')
    labelframe_right_top.place(x=10, y=50)
    labelframe_right_bottom = LabelFrame(labelframe_right, text='Thông tin môn học', width=370, height=285,
                                         bg='#CFCFCF')
    labelframe_right_bottom.place(x=10, y=455)
    labelframe_right_bottom2 = LabelFrame(labelframe_right, width=210, height=280, bg='#CFCFCF')
    labelframe_right_bottom2.place(x=390, y=460)
    # Hình ảnh
    Label(labelframe_left_top, text='Mã môn học: ', bg='#CFCFCF').place(x=20, y=50)
    Label(labelframe_left_top, text='Tên môn học: ', bg='#CFCFCF').place(x=20, y=100)
    Label(labelframe_left_top, text='Giờ vào: ', bg='#CFCFCF').place(x=20, y=150)
    Label(labelframe_left_top, text='Giờ ra: ', bg='#CFCFCF').place(x=20, y=200)
    maMh = Entry(labelframe_left_top, width=30)
    maMh.place(x=100, y=50)
    tenMh = Entry(labelframe_left_top, width=30)
    tenMh.place(x=100, y=100)
    gioVao = Entry(labelframe_left_top, width=30)
    gioVao.place(x=100, y=150)
    gioRa = Entry(labelframe_left_top, width=30)
    gioRa.place(x=100, y=200)

    tv = ttk.Treeview(labelframe_left_top, columns=('Malop', 'Tenlop', 'Giovao', 'Giora'), show='headings', height=10)
    tv.heading('Malop', text='Mã môn học')
    tv.column("Malop", anchor='center', width=80)
    tv.heading('Tenlop', text='Tên môn học')
    tv.column("Tenlop", anchor='w', width=100)
    tv.heading('Giovao', text='Giờ vào')
    tv.column("Giovao", anchor='w', width=100)
    tv.heading('Giora', text='Giờ vào')
    tv.column("Giora", anchor='w', width=100)
    listSubjects(tv)
    # right-bottom
    lopHoc = ttk.Combobox(labelframe_right_bottom, width=15)
    getComboBox(lopHoc, getClass())
    lopHoc.place(x=220, y=30)
    Label(labelframe_right_bottom, text='Chọn lớp học để điểm danh: ', bg='#CFCFCF', font=('Arial', 10, 'bold')).place(
        x=20, y=30)
    Label(labelframe_right_bottom, text='Mã lớp học: ', bg='#CFCFCF').place(x=40, y=100)
    Label(labelframe_right_bottom, text='Tên lớp học: ', bg='#CFCFCF').place(x=40, y=150)
    Label(labelframe_right_bottom, text='Thời gian học: ', bg='#CFCFCF').place(x=40, y=200)
    maMH = Entry(labelframe_right_bottom, width=25)
    maMH.place(x=130, y=100)
    tenMH = Entry(labelframe_right_bottom, width=25)
    tenMH.place(x=130, y=150)
    khungGio = Entry(labelframe_right_bottom, width=25)
    khungGio.place(x=130, y=200)
    def exit_f():
        labelfrm.destroy()

    Button(labelframe_left_top, text="LƯU LẠI", height=2, width=13, bd=0, bg='#00D7FF').place(relx=0.2, rely=0.75,
                                                                                               anchor='center')
    Button(labelframe_left_top, text="HỦY BỎ", height=2, width=13, bd=0, bg='#00D7FF').place(relx=0.4, rely=0.75,
                                                                                              anchor='center')
    Button(labelframe_left_bottom, text="MỞ WEBCAM", height=2, width=25, bd=0, bg='#00D7FF').place(relx=0.2, rely=0.5, anchor='center')
    Button(labelframe_left_bottom, text="ĐÓNG WEBCAM", height=2, width=25, bd=0, bg='#00D7FF').place(relx=0.5, rely=0.5, anchor='center')
    Button(labelframe_left_bottom, text="THOÁT", height=2, width=25, bd=0, bg='#00D7FF', command=exit_f).place(relx=0.8,
                                                                                                               rely=0.5,
                                                                                                               anchor='center')