import tkinter
from tkinter import *
from tkinter import Tk
from tkinter.ttk import *
import PIL.ImageTk, PIL.Image
import cv2
from cv2 import *
from database import *
from sinhvien import *
import numpy as np
import os

def getData(window):
    face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    labelfrm = LabelFrame(window, width=1400, height=760, bd=0)
    labelfrm.place(x=0, y=0)
    labelframe_left = LabelFrame(labelfrm, width=680, height=750, bg='#CFCFCF')
    labelframe_left.place(x=5, y=5)
    labelframe_right = LabelFrame(labelfrm, width=690, height=750, bg='#CFCFCF')
    labelframe_right.place(x=700, y=5)
    tieude = Label(labelframe_left, text="TẠO DỮ LIỆU NHẬN DIỆN", font=('Arial', 18), bg='#CFCFCF')
    tieude.place(relx=0.5, rely=0.04, anchor='center')

    labelframe_left_top = LabelFrame(labelframe_left, text='Lấy dữ liệu từ Webcam', width=665, height=500, bg='#CFCFCF')
    labelframe_left_top.place(x=5, y=50)
    

    labelframe_left_bottom = LabelFrame(labelframe_left, text='', width=665, height=190, bg='#CFCFCF')
    labelframe_left_bottom.place(x=5, y=552)
    labelframe_right_top = LabelFrame(labelframe_right, text='Kết quả lấy dữ liệu', width=675, height=450, bg='#CFCFCF')
    labelframe_right_top.place(x=5, y=50)
    labelframe_right_bottom = LabelFrame(labelframe_right, text='', width=675, height=197+50, bg='#CFCFCF')
    labelframe_right_bottom.place(x=5, y=495)
    # Hình ảnh
    labelframe_image = Label(labelframe_right_top, text='Hinh ảnh', width=150, height=150, bd=5, bg='#CFCFCF')
    labelframe_image.place(relx=0.5, rely=0.3, anchor='center')

    Label(labelframe_right_top, text='Số ảnh: ', bg='#CFCFCF').place(x=20, y=350)
    Label(labelframe_right_top, text='Mã sinh viên: ', bg='#CFCFCF').place(x=20, y=200)
    Label(labelframe_right_top, text='Ngày sinh: ', bg='#CFCFCF').place(x=20, y=250)
    Label(labelframe_right_top, text='Tên sinh viên: ', bg='#CFCFCF').place(x=310, y=200)
    Label(labelframe_right_top, text='Địa chỉ: ', bg='#CFCFCF').place(x=310, y=250)
    Label(labelframe_right_top, text='Giới tính: ', bg='#CFCFCF').place(x=310, y=300)
    Label(labelframe_right_top, text='Lớp học: ', bg='#CFCFCF').place(x=20, y=300)
    soanh = ttk.Combobox(labelframe_right_top, width=15)
    soanh['values'] = [100, 150, 200]
    soanh.place(x=100, y=350)
    soanh.current(0)
    maSV = Entry(labelframe_right_top, width=30)
    maSV.place(x=100, y=200)
    ngaySinh = Entry(labelframe_right_top, width=30)
    ngaySinh.place(x=100, y=250)
    hoTen = Entry(labelframe_right_top, width=30)
    hoTen.place(x=400, y=200)
    diaChi = Entry(labelframe_right_top, width=30)
    diaChi.place(x=400, y=250)
    lopHoc = Entry(labelframe_right_top, width=30)
    lopHoc.place(x=100, y=300)
    gioitinh = Entry(labelframe_right_top, width=30)
    gioitinh.place(x=400, y=300)
    col = ('Masv', 'Hoten', 'Gioitinh', 'Diachi', 'Ngaysinh', 'Lophoc')
    tv2 = ttk.Treeview(labelframe_right_bottom, columns=col, show='headings', height=8)
    tv2.heading('Masv', text='Mã sinh viên')
    tv2.column("Masv", anchor='center', width=104)
    tv2.heading('Hoten', text='Tên sinh viên')
    tv2.column("Hoten", anchor='center', width=140)
    tv2.heading('Gioitinh', text='Giới tính')
    tv2.column('Gioitinh', anchor='center', width=104)
    tv2.heading('Diachi', text='Địa chỉ')
    tv2.column('Diachi', anchor='center', width=104)
    tv2.heading('Ngaysinh', text='Ngày sinh')
    tv2.column('Ngaysinh', anchor='center', width=104)
    tv2.heading('Lophoc', text='Lớp học')
    tv2.column('Lophoc', anchor='center', width=104)
    listStudent(tv2, getInfor())
    #Hiển thị cam
    canvas = Canvas(labelframe_left_top, width=640, height=450)
    canvas.place(relx=0.5, rely=0.5, anchor='center')
    photo = None
    index = 0

    def update_frame(canvas, photo, label, index, id, cap):
        ret, frame = cap.read()
        frame = cv2.resize(frame, dsize=None, fx=1, fy=1)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face.detectMultiScale(frame, 1.3, 5)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 0), 2)
            if not os.path.exists('dataSet'):
                os.makedirs('dataSet')
            index += 1
            if index <= int(soanh.get()):
                Label(labelframe_left_bottom, text="Số ảnh: {0}/{1}".format(str(index), soanh.get())).place(x=10, y=10)
                cv2.imwrite('dataSet/User.{0}.{1}.jpg'.format(id, index), cv2.resize(img[y:y + h, x:x + w], dsize=(300, 300)))
            if index == int(soanh.get()) + 1:
                messagebox.showinfo('Thông báo', 'Đã lấy ảnh xong, bạn có thể tắt camera!')
        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)
        label.after(15, lambda: update_frame(canvas, photo, labelframe_left_top, index, id, cap))

    def laydulieu():
        if maSV.get()=='':
            messagebox.showerror('Thông báo', 'Chọn một sinh viên bất kỳ để lấy dữ liệu!')
        else:
            cap = cv2.VideoCapture(0)
            update_frame(canvas, photo, labelframe_left_top, index, maSV.get(), cap)

    def close_cam():
        cv2.destroyAllWindows()
        labelfrm.destroy()
        getData(window)

    def exit_f():
        cv2.destroyAllWindows()
        labelfrm.destroy()

    def open_folder():
        path = "dataSet"
        path = os.path.realpath(path)
        os.startfile(path)

    def select_record_st():
        maSV.delete(0, END)
        hoTen.delete(0, END)
        diaChi.delete(0, END)
        ngaySinh.delete(0, END)
        lopHoc.delete(0, END)
        gioitinh.delete(0, END)
        selected = tv2.focus()
        values = tv2.item(selected, 'values')
        maSV.insert(0, values[0])
        hoTen.insert(0, values[1])
        gioitinh.insert(0, values[2])
        diaChi.insert(0, values[3])
        ngaySinh.insert(0, values[4])
        lopHoc.insert(0, values[5])

    def clicker_st(e):
        select_record_st()

    tv2.bind("<ButtonRelease-1>", clicker_st)
    
    Button(labelframe_right_bottom, text="MENU CHÍNH", height=2, width=15, bd=0,  bg='#00D7FF', command=exit_f).place(relx=0.5, rely=0.89, anchor='center')
    Button(labelframe_left_bottom, text="MỞ WEBCAM", height=2, width=15, bd=0, bg='#00D7FF', command=laydulieu).place(relx=0.2, rely=0.4, anchor='center')
    Button(labelframe_left_bottom, text="ĐÓNG WEBCAM", height=2, width=15, bd=0, bg='#00D7FF', command=close_cam).place(relx=0.4, rely=0.4, anchor='center')
    Button(labelframe_left_bottom, text="XEM THƯ MỤC", height=2, width=15, bd=0, bg='#00D7FF', command=open_folder).place(relx=0.6, rely=0.4, anchor='center')
    Button(labelframe_left_bottom, text="THOÁT", height=2, width=15, bd=0, bg='#00D7FF', command=exit_f).place(relx=0.8, rely=0.4, anchor='center')
    Button(labelframe_left_bottom, text="TRAINING DỮ LIỆU", height=2, width=25, bd=0, bg='#00D7FF').place(relx=0.5, rely=0.7, anchor='center')