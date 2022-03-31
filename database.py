import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=HUNG-F181\LEHUNGDB;'
                      'Database=SVDiemDanh;'
                      'Trusted_Connection=yes;')

def getInfor():
    cursor = conn.cursor()
    cursor.execute('SELECT masv, fullname, gender, address, birthday, name FROM students, class where students.malop= class.malop')
    a = []
    for i in cursor:
        a.append(list(i))
    conn.commit()
    return a


def lookInfor(masv):
    cursor = conn.cursor()
    cursor.execute("SELECT masv, fullname, gender, address, birthday, name FROM students, class where students.malop= class.malop and masv = '{0}'".format(masv))
    a = []
    for i in cursor:
        a.append(list(i))
    conn.commit()
    return a

def getClass():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM class')
    a = []
    for i in cursor:
        a.append(list(i))
    return a
def getGV():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Teachers')
    a = []
    for i in cursor:
        a.append(list(i))
    return a
#Bang students
def getID(name):
    cursor = conn.cursor()
    cursor.execute("SELECT malop FROM class where name = '{0}'".format(name))
    a = []
    for i in cursor:
        a.append(list(i))
    return a

def insertStudent(masv, name, gender, adress, birthday, malop):
    cursor = conn.cursor()
    query = "insert into Students values('{0}',N'{1}',N'{2}',N'{3}','{4}','{5}')".format(masv, name, gender, adress, birthday, malop)
    cursor.execute(query)
    conn.commit()
def deleteStudent(masv):
    cursor = conn.cursor()
    query = "delete from students where masv='{0}'".format(masv)
    cursor.execute(query)
    conn.commit()
def editStudent(masv, name, gender, adress, birthday, malop):
    cursor = conn.cursor()
    query = "update Students set fullname=N'{0}', gender=N'{1}', address=N'{2}', birthday='{3}', malop='{4}' where masv='{5}'".format(name, gender, adress, birthday, malop, masv)
    cursor.execute(query)
    conn.commit()

#Bang Class
def insertClass(malop, name, khoa):
    cursor = conn.cursor()
    query = "insert into Class values('{0}','{1}',N'{2}')".format(malop, name, khoa)
    cursor.execute(query)
    conn.commit()
def deleteClass(malop):
    cursor = conn.cursor()
    query = "delete from Class where malop='{0}'".format(malop)
    cursor.execute(query)
    conn.commit()
def editClass(malop, name, khoa):
    cursor = conn.cursor()
    query = "update Class set name='{0}', khoa=N'{1}' where malop='{2}'".format(name, khoa, malop)
    cursor.execute(query)
    conn.commit()
#Bảng Teachers
def insertTeachers(magv, name, diachi, phone):
    cursor = conn.cursor()
    query = "insert into Teachers values('{0}',N'{1}',N'{2}','{3}')".format(magv, name, diachi, phone)
    cursor.execute(query)
    conn.commit()

def deleteTeachers(magv):
    cursor = conn.cursor()
    query = "delete from Teachers where magv='{0}'".format(magv)
    cursor.execute(query)
    conn.commit()

def editTeachers(magv, name, diachi, sdt):
    cursor = conn.cursor()
    query = "update Teachers set fullname=N'{0}', address=N'{1}', phone='{2}' where magv='{3}'".format(name, diachi, sdt, magv)
    cursor.execute(query)
    conn.commit()
#Bang subjects

def getSSubjects():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM subjects')
    a = []
    for i in cursor:
        a.append(list(i))
    return a
def insertSubjects(mamh, tenmh, giovao, giora):
    cursor = conn.cursor()
    query = "insert into Subjects values('{0}',N'{1}',N'{2}','{3}')".format(mamh, tenmh, giovao, giora)
    cursor.execute(query)
    conn.commit()