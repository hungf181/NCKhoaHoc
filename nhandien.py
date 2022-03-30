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

def nhanDien(window):
    
    face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    labelfrm = LabelFrame(window, width=1400, height=760, bd=0)
    labelfrm.place(x=0, y=0)
    labelframe_left = LabelFrame(labelfrm, width=750, height=750, bg='#CFCFCF')
    labelframe_left.place(x=5, y=5)
    labelframe_right = LabelFrame(labelfrm, width=610, height=750, bg='#CFCFCF')
    labelframe_right.place(x=770, y=5)
    tieude = Label(labelframe_left, text="ĐIỂM DANH SINH VIÊN", font=('Arial', 18), bg='#CFCFCF')
    tieude.place(relx=0.5, rely=0.04, anchor='center')

    labelframe_left_top = LabelFrame(labelframe_left, text='Nhận diện', width=730, height=620, bg='#CFCFCF')
    labelframe_left_top.place(x=5, y=50)

    labelframe_left_bottom = LabelFrame(labelframe_left, text='', width=730, height=60, bg='#CFCFCF')
    labelframe_left_bottom.place(x=5, y=680)
    labelframe_right_top = LabelFrame(labelframe_right, text='Kết quả điểm danh', width=590, height=400, bg='#CFCFCF')
    labelframe_right_top.place(x=10, y=50)
    labelframe_right_bottom = LabelFrame(labelframe_right, text='Thông tin môn học', width=370, height=285, bg='#CFCFCF')
    labelframe_right_bottom.place(x=10, y=455)
    labelframe_right_bottom2 = LabelFrame(labelframe_right, width=210, height=280, bg='#CFCFCF')
    labelframe_right_bottom2.place(x=390, y=460)
    # Hình ảnh
    images = LabelFrame(labelframe_right_top, width=200, height=200)
    images.place(x=350, y=80)
    canvas = Canvas(images, width=200, height=200)
    canvas.pack()

    Label(labelframe_right_top, text='Mã sinh viên: ', bg='#CFCFCF').place(x=20, y=100)
    Label(labelframe_right_top, text='Tên sinh viên: ', bg='#CFCFCF').place(x=20, y=150)
    Label(labelframe_right_top, text='Thời gian vào: ', bg='#CFCFCF').place(x=20, y=200)
    maSV = Entry(labelframe_right_top, width=30)
    maSV.place(x=100, y=100)
    hoTen = Entry(labelframe_right_top, width=30)
    hoTen.place(x=100, y=150)
    thoiGian = Entry(labelframe_right_top, width=30)
    thoiGian.place(x=100, y=200)

    #right-bottom
    lopHoc = ttk.Combobox(labelframe_right_bottom, width=15)
    getComboBox(lopHoc, getClass())
    lopHoc.place(x=220, y=30)
    Label(labelframe_right_bottom, text='Chọn lớp học để điểm danh: ', bg='#CFCFCF', font=('Arial', 10, 'bold')).place(x=20, y=30)
    Label(labelframe_right_bottom, text='Mã lớp học: ', bg='#CFCFCF').place(x=40, y=100)
    Label(labelframe_right_bottom, text='Tên lớp học: ', bg='#CFCFCF').place(x=40, y=150)
    Label(labelframe_right_bottom, text='Thời gian học: ', bg='#CFCFCF').place(x=40, y=200)
    maMH = Entry(labelframe_right_bottom, width=25)
    maMH.place(x=130, y=100)
    tenMH = Entry(labelframe_right_bottom, width=25)
    tenMH.place(x=130, y=150)
    khungGio = Entry(labelframe_right_bottom, width=25)
    khungGio.place(x=130, y=200)

    #Hiển thị cam
    canvas = Canvas(labelframe_left_top, width=700, height=525)
    canvas.place(relx=0.5, rely=0.45, anchor='center')
    photo = None
    index = 0
    def update_frame(canvas, photo, label, index, id, cap):
        ret, frame = cap.read()
        frame = cv2.resize(frame, dsize=None, fx=1.1, fy=1.1)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face.detectMultiScale(frame, 1.3, 5)
        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
        label.after(15, lambda: update_frame(canvas, photo, labelframe_left_top, index, id, cap))

    def laydulieu():
        cap = cv2.VideoCapture(0)
        update_frame(canvas, photo, labelframe_left_top, index, maSV.get(), cap)

    def close_cam():
        cv2.destroyAllWindows()
        labelfrm.destroy()
        nhanDien(window)

    def exit_f():
        cv2.destroyAllWindows()
        labelfrm.destroy()

    Button(labelframe_right_top, text="LƯU LẠI", height=2, width=13, bd=0, bg='#00D7FF').place(relx=0.2, rely=0.75, anchor='center')
    Button(labelframe_right_top, text="HỦY BỎ", height=2, width=13, bd=0, bg='#00D7FF').place(relx=0.4, rely=0.75, anchor='center')
    Button(labelframe_left_bottom, text="MỞ WEBCAM", height=2, width=25, bd=0, bg='#00D7FF', command=laydulieu).place(relx=0.2, rely=0.5, anchor='center')
    Button(labelframe_left_bottom, text="ĐÓNG WEBCAM", height=2, width=25, bd=0, bg='#00D7FF', command=close_cam).place(relx=0.5, rely=0.5, anchor='center')
    Button(labelframe_left_bottom, text="THOÁT", height=2, width=25, bd=0, bg='#00D7FF', command=exit_f).place(relx=0.8, rely=0.5, anchor='center')