#School Database

import mysql.connector as a
connect = a.connect(host='localhost',user='root',passwd='password',database='log',auth_plugin='mysql_native_password')

def ast():
    n = input("Student Name : ")
    cn = input("Class Name: ")
    r = input("Roll No: ")
    a = input("Address: ")
    p = input("Phone: ")
    data = (n,cn,r,a,p)
    sql ='insert into student values(%s,%s,%s,%s,%s)'
    c = connect.cursor()
    c.execute(sql,data)
    connect.commit()
    print("data enterd succesfully")
    print('*----------------------------------------------*')
    main()

def rst():
    cn=input("class name : ")
    r=input("Roll no : ")
    data=(cn,r)
    sql= 'delete from student where class = %s and roll = %s'
    c = connect.cursor()
    c.execute(sql,data)
    connect.commit()
    print("Data Updated")
    print('*---------------------------------------------- *')
    main()

def at():
    n=input("name: ")
    p=input("post: ")
    s=input("salary: ")
    a=input("address: ")
    ph=input("phone : ")
    data=(n,p,s,a,ph)
    sql = 'insert into teacher values(%s,%s,%s,%s,%s)'
    c = connect.cursor()
    c.execute(sql,data)
    connect.commit()
    print("data enterd succesfully")
    print('*---------------------------------------------- *')
    main()

def rt():
    n=input("Teacher name: ")
    p=input("post: ")
    data=(n,p)
    sql = 'delete from teacher where name = %s and post = %s'
    c = connect.cursor()
    c.execute(sql,data)
    connect.commit()
    print("data updated")
    print('*---------------------------------------------- *')
    main()

def sf():
    n=input("student name: ")
    c=input("class name: ")
    r=input("roll no: ")
    m=input("month and year: ")
    f=input("fees: ")
    d=input("date: ")
    data=(n,c,r,m,f,d)
    sql = 'insert into fees values(%s,%s,%s,%s,%s,%s)'
    c = connect.cursor()
    c.execute(sql,data)
    connect.commit()
    print("data enterd succesfully")
    print('*---------------------------------------------- *')
    main()

def ps():
    n=input("teacher name: ")
    m=input("month: ")
    p=input("yes/no : ")
    data=(n,m,p)
    sql = 'insert into salary values(%s,%s,%s)'
    c = connect.cursor()
    c.execute(sql, data)
    connect.commit()
    print("data enterd succesfully")
    print('*---------------------------------------------- *')
    main()

def dc():
    cl=input("class: ")
    data = (cl,)
    sql = 'select * from student where class = %s'
    c = connect.cursor()
    c.execute(sql,data)
    d = c.fetchall()
    for i in d:
        print("name: ",i[0])
        print("class: ", i[1])
        print("roll: ", i[2])
        print("address: ", i[3])
        print("phone: ", i[4])
    print('*---------------------------------------------- *')
    main()

def ts():
    sql = 'select * from teacher'
    c = connect.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("name: ", i[0])
        print("post: ", i[1])
        print("salary: ", i[2])
        print("address: ", i[3])
        print("phone: ", i[4])
        print('*---------------------------------------------- *')
        main()


def main():
    print("""                                   ROTARY CENTRAL SCHOOL
                    1.ADD STUDENT                       2.REMOVE STUDENT
                    3.ADD TEACHER                       4.REMOVE TEACHER
                    5.SUBMIT FEES                       6.PAY SALARY
                    7.DISPLAY CLASS                     8.TEACHERS LIST  """)
    choice=input("Enter Task No : ")
    print("*-------------------------------*")
    if (choice== '1'):
        ast()
    elif (choice =='2'):
        rst()
    elif (choice =='3'):
        at()
    elif (choice =='4'):
        rt()
    elif (choice =='5'):
        sf()
    elif (choice =='6'):
        ps()
    elif (choice =='7'):
        dc()
    elif (choice =='8'):
        ts()
    else:
        print("wrong choice....")
        main()
#input password as 'password'
def passwd():
    p = input('password: ')
    if p=="password":
        main()
    else:
        print("Wrong password")
        passwd()


if __name__ == '__main__':
    passwd()