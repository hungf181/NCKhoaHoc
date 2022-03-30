from tkinter import *
from sinhvien import *
from laydulieu import getData
from tkinter import ttk
from nhandien import *
from monhoc import *
window = Tk()
window.title('Hệ thống quản lý - Điểm danh sinh viên')
window.geometry('1200x760')
window.minsize(1400, 760)
window.maxsize(1400, 760)
window.configure(bg='lavender')
tieude = Label(window, text="QUẢN LÝ SINH VIÊN", font=('Arial', 26), bg='lavender')
tieude.place(relx=0.5, rely=0.2, anchor='center')
sinhvien_button = Button(window, text="SINH VIÊN", height=10, width=30, bd=0, bg='#5F9EA0', command=lambda: sinhvien(window))
sinhvien_button.place(relx=0.32, rely=0.42, anchor='center')
getData_button = Button(window, text="LẤY DỮ LIỆU", height=10, width=30, bd=0, bg='#5F9EA0', command=lambda: getData(window))
getData_button.place(relx=0.5, rely=0.42, anchor='center')
diemdanh_button = Button(window, text="ĐIỂM DANH", height=10, width=30, bd=0, bg='#5F9EA0', command=lambda: nhanDien(window))
diemdanh_button.place(relx=0.68, rely=0.42, anchor='center')
thongke_button = Button(window, text="THỐNG KÊ", height=10, width=30, bd=0, bg='#5F9EA0')
thongke_button.place(relx=0.32, rely=0.68, anchor='center')
giaovien_button = Button(window, text="ĐÁNH GIÁ", height=10, width=30, bd=0, bg='#5F9EA0')
giaovien_button.place(relx=0.5, rely=0.68, anchor='center')
monhoc_button = Button(window, text="MÔN HỌC", height=10, width=30, bd=0, bg='#5F9EA0', command=lambda: Monhoc(window))
monhoc_button.place(relx=0.68, rely=0.68, anchor='center')

window.mainloop()
