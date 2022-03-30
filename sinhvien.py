from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import *


def listClass(tv):
    for item in tv.get_children():
        tv.delete(item)
    for i in getClass():
        tv.insert('', END, values=i)
    tv.place(x=320, y=20)


def listStudent(tv, arr):
    for item in tv.get_children():
        tv.delete(item)
    for i in arr:
        tv.insert('', END, values=i)
    tv.place(x=5, y=5)

def listTeachers(tv):
    for item in tv.get_children():
        tv.delete(item)
    for i in getGV():
        tv.insert('', END, values=i)
    tv.place(x=280, y=20)

def getComboBox(cbName, list):
    x = []
    for i in list:
        x.append(i[1])
    cbName['values'] = x
    if x:
        cbName.current(0)
    else:
        cbName.set("")

    
def sinhvien(window):
    labelfrm = LabelFrame(window, width=1400, height=760, bd=0)
    labelfrm.pack()
    labelframe_left = LabelFrame(labelfrm, width=680, height=750, bg='#CFCFCF')
    labelframe_left.place(x=5, y=5)

    tieude = Label(labelframe_left, text="THÔNG TIN SINH VIÊN", font=('Arial', 18), bg='#CFCFCF')
    tieude.place(relx=0.5, rely=0.04, anchor='center')

    labelframe_left_top = LabelFrame(labelframe_left, text='Thông tin cá nhân', width=665, height=350, bg='#CFCFCF')
    labelframe_left_top.place(x=5, y=50)
    labelframe_left_bottom = LabelFrame(labelframe_left, text='Thông tin lớp học', width=665, height=340, bg='#CFCFCF')
    labelframe_left_bottom.place(x=5, y=400)


    # labelFrame2
    Label(labelframe_left_top, text='Mã sinh viên: ', bg='#CFCFCF').place(x=20, y=50)
    Label(labelframe_left_top, text='Ngày sinh: ', bg='#CFCFCF').place(x=20, y=100)
    Label(labelframe_left_top, text='Tên sinh viên: ', bg='#CFCFCF').place(x=310, y=50)
    Label(labelframe_left_top, text='Địa chỉ: ', bg='#CFCFCF').place(x=310, y=100)
    Label(labelframe_left_top, text='Giới tính: ', bg='#CFCFCF').place(x=310, y=150)
    Label(labelframe_left_top, text='Lớp học: ', bg='#CFCFCF').place(x=20, y=150)

    maSV = Entry(labelframe_left_top, width=30)
    maSV.place(x=100, y=50)
    ngaySinh = Entry(labelframe_left_top, width=30)
    ngaySinh.place(x=100, y=100)
    hoTen = Entry(labelframe_left_top, width=30)
    hoTen.place(x=400, y=50)
    diaChi = Entry(labelframe_left_top, width=30)
    diaChi.place(x=400, y=100)
    lopHoc = ttk.Combobox(labelframe_left_top, width=27)
    getComboBox(lopHoc, getClass())
    lopHoc.place(x=100, y=150)
    gioitinh = ttk.Combobox(labelframe_left_top, width=15)
    gioitinh['values'] = ['Nam', 'Nữ']
    gioitinh.place(x=400, y=150)
    gioitinh.current(0)


    # labelFrame3
    Label(labelframe_left_bottom, text='Mã lớp: ', bg='#CFCFCF').place(x=20, y=40)
    Label(labelframe_left_bottom, text='Tên lớp học: ', bg='#CFCFCF').place(x=20, y=80)
    Label(labelframe_left_bottom, text='Thuộc khoa: ', bg='#CFCFCF').place(x=20, y=120)
    malop = Entry(labelframe_left_bottom, width=30)
    malop.place(x=100, y=40)
    tenlop = Entry(labelframe_left_bottom, width=30)
    tenlop.place(x=100, y=80)
    khoa = Entry(labelframe_left_bottom, width=30)
    khoa.place(x=100, y=120)
    #Treeview - Class
    tv = ttk.Treeview(labelframe_left_bottom, columns=('Malop', 'Tenlop', 'Khoa'), show='headings', height=10)
    tv.heading('Malop', text='Mã lớp')
    tv.column("Malop", anchor='center', width=80)
    tv.heading('Tenlop', text='Tên lớp')
    tv.column("Tenlop", anchor='w', width=100)
    tv.heading('Khoa', text='Khoa')
    tv.column("Khoa", anchor='w', width=145)
    listClass(tv)

    def select_record():
        malop.delete(0, END)
        tenlop.delete(0, END)
        khoa.delete(0, END)
        selected = tv.focus()
        values = tv.item(selected, 'values')
        malop.insert(0, values[0])
        tenlop.insert(0, values[1])
        khoa.insert(0, values[2])

    def clicker(e):
        select_record()

    tv.bind("<ButtonRelease-1>", clicker)
    # labelframe_right
    labelframe_right = LabelFrame(labelfrm, width=690, height=750, bg='#CFCFCF')
    labelframe_right.place(x=700, y=5)
    tieude = Label(labelframe_right, text="DANH SÁCH SINH VIÊN", font=('Arial', 18), bg='#CFCFCF')
    tieude.place(relx=0.5, rely=0.04, anchor='center')
    labelframe_right_top = LabelFrame(labelframe_right, text='Tìm kiếm sinh viên', width=675, height=100, bg='#CFCFCF')
    labelframe_right_top.place(x=5, y=50)
    labelframe_right_bottom = LabelFrame(labelframe_right, text='Kết quả tìm kiếm', width=675, height=250, bg='#CFCFCF')
    labelframe_right_bottom.place(x=5, y=150)
    # Treeview - Student
    col = ('Masv', 'Hoten', 'Gioitinh', 'Diachi', 'Ngaysinh', 'Lophoc')
    tv2 = ttk.Treeview(labelframe_right_bottom, columns = col, show = 'headings', height = 9)
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
    labelframe_right_bottom2 = LabelFrame(labelframe_right, text='Thông tin giảng viên', width=665, height=280, bg='#CFCFCF')
    labelframe_right_bottom2.place(x=5, y=400)
    Label(labelframe_right_bottom2, text='Mã giáo viên: ', bg='#CFCFCF').place(x=20, y=40)
    Label(labelframe_right_bottom2, text='Tên giáo viên: ', bg='#CFCFCF').place(x=20, y=80)
    Label(labelframe_right_bottom2, text='Địa chỉ: ', bg='#CFCFCF').place(x=20, y=120)
    Label(labelframe_right_bottom2, text='Số điện thoại: ', bg='#CFCFCF').place(x=20, y=160)
    magv = Entry(labelframe_right_bottom2, width=25)
    magv.place(x=110, y=40)
    tengv = Entry(labelframe_right_bottom2, width=25)
    tengv.place(x=110, y=80)
    dcgv = Entry(labelframe_right_bottom2, width=25)
    dcgv.place(x=110, y=120)
    phone = Entry(labelframe_right_bottom2, width=25)
    phone.place(x=110, y=160)
    col = ('Magv', 'Tengv', 'diachi', 'Phone')
    tv3 = ttk.Treeview(labelframe_right_bottom2, columns=col, show='headings', height=7)
    tv3.heading('Magv', text='Mã giáo viên')
    tv3.column("Magv", anchor='center', width=80)
    tv3.heading('Tengv', text='Tên giáo viên')
    tv3.column("Tengv", anchor='center', width=110)
    tv3.heading('diachi', text='Địa chỉ')
    tv3.column("diachi", anchor='center', width=90)
    tv3.heading('Phone', text='Số điện thoại')
    tv3.column("Phone", anchor='center', width=90)
    listTeachers(tv3)
    def select_record_gv():
        magv.delete(0, END)
        tengv.delete(0, END)
        dcgv.delete(0, END)
        phone.delete(0, END)
        selected = tv3.focus()
        values = tv3.item(selected, 'values')
        magv.insert(0, values[0])
        tengv.insert(0, values[1])
        dcgv.insert(0, values[2])
        phone.insert(0, values[3])
    def clicker_gv(e):
        select_record_gv()

    tv3.bind("<ButtonRelease-1>", clicker_gv)
    # labelframe_right_top
    label_Name = Label(labelframe_right_top, text='Nhập mã sinh viên: ', bg='#CFCFCF', font=('Arial', 10, 'bold'))
    label_Name.place(x=20, y=30)
    maSVSearch = Entry(labelframe_right_top, width=30)
    maSVSearch.place(x=150, y=30)

    # labelframe_right_bottom

    def insertSV():
        if maSV.get() == '':
            messagebox.showerror('Thông báo', 'Mã sinh viên không được để trống !')
        else:
            try:
                insertStudent(maSV.get(), hoTen.get(), gioitinh.get(), diaChi.get(), ngaySinh.get(), getID(lopHoc.get())[0][0])
                listStudent(tv2, getInfor())
            except:
                messagebox.showerror('Thông báo', 'Lỗi khi thêm mới sinh viên !')
    def editSV():
        if maSV.get() == '':
            messagebox.showerror('Thông báo', 'Mã sinh viên không được để trống !')
        else:
            try:
                editStudent(maSV.get(), hoTen.get(), gioitinh.get(), diaChi.get(), ngaySinh.get(), getID(lopHoc.get())[0][0])
                listStudent(tv2, getInfor())
            except:
                messagebox.showerror('Thông báo','Lỗi khi sửa mới sinh viên !')
    def deleteSV():
        if maSV.get() == '':
            messagebox.showerror('Thông báo', 'Mã sinh viên không được để trống!')
        else:
            try:
                deleteStudent(maSV.get())
                listStudent(tv2, getInfor())
            except:
                messagebox.showerror('Thông báo', 'Lỗi khi xóa một sinh viên!')

    def lookSV():
        if maSVSearch.get() == '':
            listStudent(tv2, getInfor())
        else:
            listStudent(tv2, lookInfor(maSVSearch.get()))
    def insertLop():
        if malop.get() == '':
            messagebox.showerror('Thông báo', 'Mã lớp không được để trống!')
        else:
            try:
                insertClass(malop.get(), tenlop.get(), khoa.get())
                listClass(tv)
                getComboBox(lopHoc, getClass())
            except:
                messagebox.showerror('Thông báo', 'Có lỗi khi thêm lớp học!')
    def deleteLop():
        if malop.get() == '':
            messagebox.showerror('Thông báo', 'Mã lớp không được để trống!')
        else:
            try:
                deleteClass(malop.get())
                listClass(tv)
                getComboBox(lopHoc, getClass())
            except:
                messagebox.showerror('Thông báo', 'Có lỗi lỗi khi xóa lớp học!')

    def editLop():
        if malop.get() == '':
            messagebox.showerror('Thông báo', 'Mã lớp không được để trống!')
        else:
            try:
                editClass(malop.get(), tenlop.get(), khoa.get())
                listClass(tv)
                getComboBox(lopHoc, getClass())
            except:
                messagebox.showerror('Thông báo', 'Có lỗi khi sửa thông tin lớp học!')
    def insertGV():
        if magv.get() == '':
            messagebox.showerror('Thông báo', 'Mã giáo viên không được để trống!')
        else:
            try:
                insertTeachers(magv.get(), tengv.get(), dcgv.get(), phone.get())
                listTeachers(tv3)
            except:
                messagebox.showerror('Thông báo', 'Có lỗi khi thêm thông tin giáo viên !')
    def deleteGV():
        if magv.get() == '':
            messagebox.showerror('Thông báo', 'Mã giáo viên không được để trống !')
        else:
            try:
                deleteTeachers(magv.get())
                listTeachers(tv3)
            except:
                messagebox.showerror('Thông báo', 'Có lỗi khi xóa thông tin giáo viên !')
    def editGV():
        if magv.get() == '':
            messagebox.showerror('Thông báo', 'Mã giáo viên không được để trống !')
        else:
            try:
                editTeachers(magv.get(), tengv.get(), dcgv.get(), phone.get())
                listTeachers(tv3)
            except:
                messagebox.showerror('Thông báo', 'Có lỗi khi sửa thông tin giáo viên !')
    #Button - Sinh viên
    insert_button_sv = Button(labelframe_left_top, text="THÊM MỚI", height=2, width=15, bd=0, bg='#00D7FF', command=insertSV)
    insert_button_sv.place(x=150, y=220)
    edit_button_sv = Button(labelframe_left_top, text="CHỈNH SỬA", height=2, width=15, bd=0, bg='#00D7FF', command=editSV)
    edit_button_sv.place(x=300, y=220)
    delete_button_sv = Button(labelframe_left_top, text="XÓA", height=2, width=15, bd=0, bg='#00D7FF', command=deleteSV)
    delete_button_sv.place(x=450, y=220)
    #Button - Lớp
    insert_button = Button(labelframe_left_bottom, text="THÊM MỚI", height=2, width=10, bd=0, bg='#00D7FF', command=insertLop)
    insert_button.place(x=30, y=200)
    edit_button = Button(labelframe_left_bottom, text="CHỈNH SỬA", height=2, width=10, bd=0, bg='#00D7FF', command=editLop)
    edit_button.place(x=130, y=200)
    delete_button = Button(labelframe_left_bottom, text="XÓA", height=2, width=10, bd=0, bg='#00D7FF', command=deleteLop)
    delete_button.place(x=230, y=200)
    #Button - tìm kiếm
    search_button = Button(labelframe_right_top, text="TÌM KIẾM", width=15, bd=0, bg='#00D7FF', command=lookSV)
    search_button.place(x=350, y=28)
    # Button - GV
    insert_button_gv = Button(labelframe_right_bottom2, text="THÊM MỚI", height=2, width=10, bd=0, bg='#00D7FF', command=insertGV)
    insert_button_gv.place(relx=0.33, rely=0.85, anchor='center')
    edit_button_gv = Button(labelframe_right_bottom2, text="CHỈNH SỬA", height=2, width=10, bd=0, bg='#00D7FF', command=editGV)
    edit_button_gv.place(relx=0.5, rely=0.85, anchor='center')
    delete_button_gv = Button(labelframe_right_bottom2, text="XÓA", height=2, width=10, bd=0, bg='#00D7FF', command=deleteGV)
    delete_button_gv.place(relx=0.67, rely=0.85, anchor='center')
    Button(labelframe_right, text="MENU CHÍNH", height=2, width=15, bd=0, bg='#00D7FF', command=labelfrm.destroy).place(relx=0.5, rely=0.96, anchor='center')
