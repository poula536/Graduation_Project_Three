'''''''''
import tkinter
from tkinter import *
from tkinter import messagebox

addcourse_window = Tk()
addcourse_window.title('Add Course')
addcourse_window.geometry("925x500+300+200")
addcourse_window.config(bg="#ECF9FF")
addcourse_window.resizable(False, False)


# back forward button
def backfw_btn():
    addcourse_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()


bfw_btn = tkinter.PhotoImage(file='backfw.png', master=addcourse_window)
back_forward_btn = Button(addcourse_window, cursor='hand2', image=bfw_btn, bd=0, bg="#ECF9FF",
                          activebackground="#ECF9FF", height=80, width=80, command=backfw_btn)
back_forward_btn.place(x=10, y=5)

img_logo = tkinter.PhotoImage(file='logo.png', master=addcourse_window)
addcourse_window.iconphoto(False, img_logo)
Label(addcourse_window, image=img_logo, bg="white", background="#ECF9FF").place(x=50, y=120)
frame = Frame(addcourse_window, width=350, height=440, bg="#ECF9FF")
frame.place(x=480, y=50)

heading = Label(frame, text="اضافة مادة", fg="black", bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 25, 'bold'))
heading.place(x=100, y=-6)


def on_enter(e):
    doctorname_entry.delete(0, 'end')


def on_leave(e):
    doctor_name = doctorname_entry.get()
    if doctor_name == '':
        doctorname_entry.insert(0, 'اسم الدكتور')


doctorname_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
doctorname_entry.place(x=30, y=70)
doctorname_entry.insert(0, 'اسم الدكتور')
doctorname_entry.bind('<FocusIn>', on_enter)
doctorname_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=95)


def on_enter(e):
    email_entry.delete(0, 'end')


def on_leave(e):
    name = email_entry.get()
    if name == '':
        email_entry.insert(0, 'عنوان البريد الالكتروني')


email_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
email_entry.place(x=30, y=115)
email_entry.insert(0, 'عنوان البريد الالكتروني')
email_entry.bind('<FocusIn>', on_enter)
email_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=140)


def on_enter(e):
    password_entry.delete(0, 'end')


def on_leave(e):
    password = password_entry.get()
    if password == '':
        password_entry.insert(0, 'كلمه السر')


password_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
password_entry.place(x=30, y=150)
password_entry.insert(0, 'كلمه السر')
password_entry.bind('<FocusIn>', on_enter)
password_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=175)


def on_enter(e):
    institute_entry.delete(0, 'end')


def on_leave(e):
    institute_name = institute_entry.get()
    if institute_name == '':
        institute_entry.insert(0, 'اسم المعهد')


institute_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
institute_entry.place(x=30, y=185)
institute_entry.insert(0, 'اسم المعهد')
institute_entry.bind('<FocusIn>', on_enter)
institute_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=210)


def on_enter(e):
    department_entry.delete(0, 'end')


def on_leave(e):
    department_name = department_entry.get()
    if department_name == '':
        department_entry.insert(0, 'اسم الشعبة')


department_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
department_entry.place(x=30, y=225)
department_entry.insert(0, 'اسم الشعبة')
department_entry.bind('<FocusIn>', on_enter)
department_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=250)


def on_enter(e):
    subject_entry.delete(0, 'end')


def on_leave(e):
    material_name = subject_entry.get()
    if material_name == '':
        subject_entry.insert(0, 'اسم المادة')


subject_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
subject_entry.place(x=30, y=265)
subject_entry.insert(0, 'اسم المادة')
subject_entry.bind('<FocusIn>', on_enter)
subject_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=290)


def on_enter(e):
    academic_year_entry.delete(0, 'end')


def on_leave(e):
    year_number = academic_year_entry.get()
    if year_number == '':
        academic_year_entry.insert(0, 'العام الدراسي')


academic_year_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF",
                            font=('Microsoft YaHei UI Light ', 15))
academic_year_entry.place(x=30, y=295)
academic_year_entry.insert(0, 'العام الدراسي')
academic_year_entry.bind('<FocusIn>', on_enter)
academic_year_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=320)


def on_enter(e):
    semester_entry.delete(0, 'end')


def on_leave(e):
    semester_name = semester_entry.get()
    if semester_name == '':
        semester_entry.insert(0, 'الفصل الدراسي')


semester_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
semester_entry.place(x=30, y=330)
semester_entry.insert(0, 'الفصل الدراسي')
semester_entry.bind('<FocusIn>', on_enter)
semester_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=358)


def clear():
    email_entry.delete(0, END)
    email_entry.insert(0, 'عنوان البريد الالكتروني')
    subject_entry.delete(0, END)
    subject_entry.insert(0, 'اسم المادة')
    semester_entry.delete(0, END)
    semester_entry.insert(0, 'الفصل الدراسي')
    department_entry.delete(0, END)
    department_entry.insert(0, 'اسم الشعبة')
    doctorname_entry.delete(0, END)
    doctorname_entry.insert(0, 'اسم الدكتور')
    password_entry.delete(0, END)
    password_entry.insert(0, 'كلمه السر')
    institute_entry.delete(0, END)
    institute_entry.insert(0, 'اسم المعهد')
    academic_year_entry.delete(0, END)
    academic_year_entry.insert(0, 'العام الدراسي')


def add():
    if email_entry.get() == 'عنوان البريد الالكتروني' or subject_entry.get() == 'اسم المادة' or semester_entry.get() == 'الفصل الدراسي' or department_entry.get() == 'اسم الشعبة' or doctorname_entry.get() == 'اسم الدكتور' or password_entry.get() == 'كلمه السر' or institute_entry.get() == 'اسم المعهد' or academic_year_entry.get() == 'العام الدراسي':
        messagebox.showerror('Error', 'all fields are required')
    else:
        messagebox.showinfo('Done', 'Registration is done successfully')
        clear()


btn_login = Button(frame, width=39, pady=7, text="اضافه ", bg="#57a1f8", fg='white', border=0, command=add)
btn_login.place(x=35, y=380)

addcourse_window.mainloop()
'''''

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

con_db = pymysql.connect(host='localhost', user='root', password='123456789')
mycursor = con_db.cursor()
query = 'use facerecognation_attendance_System'
mycursor.execute(query)
show_table_course_query="select * from course"

addcourse_window = Tk()
addcourse_window.title("Add Course")
addcourse_window.geometry("1450x720+40+40")
addcourse_window.config(bg="#ECF9FF")
addcourse_window.resizable(False,False)
img_logo =tkinter.PhotoImage(file='logo.png',master=addcourse_window)
addcourse_window.iconphoto(False,img_logo)


Course_list_frame = LabelFrame(addcourse_window,text="Course List")
search_frame = LabelFrame(addcourse_window,text="Search")
Course_data_frame = LabelFrame(addcourse_window,text="Course Data")

Course_list_frame.pack(fill="both",expand="yes",padx=20,pady=65)
search_frame.pack(fill="both",expand="yes",padx=20,pady=2)
Course_data_frame.pack(fill="both",expand="yes" ,padx=20,pady=10)

def backfw_btn():
    addcourse_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=addcourse_window)
back_forward_btn = Button(addcourse_window,cursor='hand2',image=bfw_btn,bd=0,
                          bg="#ECF9FF",activebackground="#ECF9FF",height=60,width=60,command=backfw_btn)
back_forward_btn.place(x=10,y=0)



def showdata(row):
    trv.delete(*trv.get_children())
    for i in row:
        trv.insert('','end',values=i)

#styling the head of table
s = ttk.Style(addcourse_window)
s.theme_use('clam')
s.configure('Treeview.Heading', background="green3")

trv = ttk.Treeview(Course_list_frame, columns=(1,2,3,4,5,6,7),show="headings",height="7")
trv.pack()

trv.column(1, anchor=CENTER)
trv.heading(1, text="Course Id")

trv.column(2, anchor=CENTER)
trv.heading(2, text="Course Name")

trv.column(3, anchor=CENTER)
trv.heading(3, text="Department Name")

trv.column(4, anchor=CENTER)
trv.heading(4, text="Lecturer Email")

trv.column(5, anchor=CENTER)
trv.heading(5, text="Acadymic Year")

trv.column(6, anchor=CENTER)
trv.heading(6, text="Semester")

trv.column(7, anchor=CENTER)
trv.heading(7, text="Student Id")

#show the table of the lecturer
try:
    mycursor.execute(show_table_course_query)
    row = mycursor.fetchall()
    showdata(row)
except Exception as err:
    messagebox.showwarning('Error', 'DB exception: %s' % err)

#reset btn
def reset():
    try:
        mycursor.execute(show_table_course_query)
        row = mycursor.fetchall()
        showdata(row)
    except Exception as err:
        messagebox.showwarning('Error', 'DB exception: %s' % err)

#search section
#get data
txtvar_of_courseid = StringVar(master=addcourse_window)
txtvar_of_course_name = StringVar(master=addcourse_window)
txtvar_of_department = StringVar(master=addcourse_window)
txtvar_of_lectemail = StringVar(master=addcourse_window)
txtvar_of_acadymic_year = StringVar(master=addcourse_window)
txtvar_of_semester = StringVar(master=addcourse_window)
txtvar_of_studid = StringVar(master=addcourse_window)
#search for record
#txtvar_of_search = StringVar()
def search():
    q = search_entry.get()
    if q =='':
        messagebox.showerror('Error','Enter course name/id or email of doctor to search')
    else:
        try:
            search_query = "select * from course where course_name like '%"+q+"%' or course_id like '%"+q+"%' or lecturer_email like '%"+q+"%' "
            mycursor.execute(search_query)
            row = mycursor.fetchall()
            showdata(row)
        except Exception as err:
            messagebox.showwarning('Error', 'DB exception: %s' % err)

search_labl = Label(search_frame,text="Search",font=('Microsoft YaHei UI Light ',10,'bold'))
search_labl.pack(side=tkinter.LEFT,padx=10)
search_entry = Entry(search_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",font=('Microsoft YaHei UI Light ',15))
search_entry.pack(side=tkinter.LEFT, padx=20)

serch_btn = Button(search_frame,text="Search",activebackground="#ECF9FF",bd=0,cursor="hand2",
                   width=10,pady=5,background="#57a1f8",fg="white",font=('Microsoft YaHei UI Light ',10,'bold'),command=search)
serch_btn.pack(side=tkinter.LEFT , padx=6)

reset_btn = Button(search_frame,text="Reset",activebackground="#ECF9FF",bd=0,cursor="hand2",
                   width=10,pady=5,background="#57a1f8",fg="white",font=('Microsoft YaHei UI Light ',10,'bold'),command=reset)
reset_btn.pack(side=tkinter.LEFT,padx=6)

#Course data section to update

def getrow(event):
    row_data = trv.identify_row(event.y)
    data = trv.item(trv.focus())
    txtvar_of_courseid.set(data['values'][0])
    txtvar_of_course_name.set(data['values'][1])
    txtvar_of_department.set(data['values'][2])
    txtvar_of_lectemail.set(data['values'][3])
    txtvar_of_acadymic_year.set(data['values'][4])
    txtvar_of_semester.set(data['values'][5])
    txtvar_of_studid.set(data['values'][6])

trv.bind("<Double-1>", getrow)

#start course ID
course_id_label = Label(Course_data_frame, text="Course ID",font=('Microsoft YaHei UI Light ',10,'bold'))
course_id_label.grid(row=0,column=0,padx=5,pady=3)

course_id_entry = Entry(Course_data_frame,state='disabled',width=25,fg='#181823',border=1,bg="#ECF9FF",
                        font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_courseid)
course_id_entry.grid(row=0,column=1,padx=5,pady=3)
#end course ID

#start Course Name
course_name_label = Label(Course_data_frame, text="Course Name",
                        font=('Microsoft YaHei UI Light ',10,'bold'))
course_name_label.grid(row=1,column=0,padx=5,pady=3)
course_name_entry = Entry(Course_data_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                        font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_course_name)
course_name_entry.grid(row=1,column=1,padx=5,pady=3)
#end Course Name

#start Email
lec_email_label = Label(Course_data_frame, text="Lecturer Email",
                        font=('Microsoft YaHei UI Light ',10,'bold'))
lec_email_label.grid(row=2,column=0,padx=5,pady=3)
lec_email_entry = Entry(Course_data_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                        font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_lectemail)
lec_email_entry.grid(row=2,column=1,padx=5,pady=3)
#end Email

#start Acadymic Year
acadymic_year_label = Label(Course_data_frame, text="Acadymic Year",
                         font=('Microsoft YaHei UI Light ',10,'bold'))
acadymic_year_label.grid(row=3,column=0,padx=5,pady=3)
acadymic_year_entry = Entry(Course_data_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                         font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_acadymic_year)
acadymic_year_entry.grid(row=3,column=1,padx=5,pady=3)
#end Acadymic Year

#start Semester
semester_label = Label(Course_data_frame, text="Semester",
                         font=('Microsoft YaHei UI Light ',10,'bold'))
semester_label.grid(row=4,column=0,padx=5,pady=3)

semester_combobox = ttk.Combobox(Course_data_frame,width=31, textvariable=txtvar_of_semester)
# Adding combobox drop down list
semester_combobox['values'] = ('first','second')
semester_combobox.grid(row=4,column=1,padx=5,pady=3)

#end Semester

#start Student id
stud_id_label = Label(Course_data_frame, text="Student Id",
                         font=('Microsoft YaHei UI Light ',10,'bold'))
stud_id_label.grid(row=5,column=0,padx=5,pady=3)
stud_id_entry = Entry(Course_data_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                         font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_studid)
stud_id_entry.grid(row=5,column=1,padx=5,pady=3)
#end Student id

# start department
dept_label = Label(Course_data_frame, text="Department",
                         font=('Microsoft YaHei UI Light ',10,'bold'))
dept_label.grid(row=0,column=2,padx=5,pady=3)
dept_combobox = ttk.Combobox(Course_data_frame, width=15, textvariable=txtvar_of_department)
# Adding combobox drop down list
dept_combobox['values'] = (' علوم حاسب' , '')
                          #' نظم ومعلومات',
                          #' اداره اعمال'

dept_combobox.grid(row=0,column=3,padx=5,pady=3)
#end start department
def clear():
    txtvar_of_courseid.set('')
    course_name_entry.delete(0,END)
    lec_email_entry.delete(0,END)
    acadymic_year_entry.delete(0,END)
    txtvar_of_semester.set('')
    stud_id_entry.delete(0, END)
    txtvar_of_department.set('')
    search_entry.delete(0, END)



def update():
    try:
        query = 'select * from lecturer where email=%s '
        mycursor.execute(query, (txtvar_of_lectemail.get()))
        row_lec_email = mycursor.fetchone()
        query = "select * from student where student_id=%s"
        mycursor.execute(query, (txtvar_of_studid.get()))
        row_studid = mycursor.fetchone()
        if txtvar_of_courseid.get() == '' or txtvar_of_course_name.get() == '' or txtvar_of_department.get() == '' or txtvar_of_lectemail.get() == '' or txtvar_of_acadymic_year.get() == '' or txtvar_of_semester.get() == '':
            messagebox.showerror('Eror', 'All fields are required')
        elif row_lec_email is None:
            messagebox.showerror('Error', 'Lecturer email did not create yet')
        elif row_studid is None:
            messagebox.showerror('Error', 'Student Id does not exist')
        else:
            t1 = txtvar_of_course_name.get()
            t2 = txtvar_of_department.get()
            t3 = txtvar_of_lectemail.get()
            t4 = txtvar_of_acadymic_year.get()
            t5 = txtvar_of_semester.get()
            t6= txtvar_of_studid.get()
            t7= txtvar_of_courseid.get()
            if messagebox.askyesno("Confirm", "Are you sure want to update"):
                update_email_query = "update course set course_name=%s , dept_name=%s , lecturer_email=%s , acadymic_year=%s , semester=%s , student_id=%s where course_id=%s"
                mycursor.execute(update_email_query, (t1,t2,t3,t4,t5,t6,t7))
                con_db.commit()
                reset()
                messagebox.showinfo('Done', 'Updated Successfully')
            else:
                return True
    except Exception as err:
        messagebox.showwarning('Error','DB exception: %s' % err)


def delete():
    try:
        if txtvar_of_courseid.get() == '' or txtvar_of_course_name.get() == '' or txtvar_of_department.get() == '' or txtvar_of_lectemail.get() == '' or txtvar_of_acadymic_year.get() == '' or txtvar_of_semester.get()== '' or txtvar_of_studid.get()== '':
            messagebox.showerror('Eror', 'All fields are required')
        elif messagebox.askyesno("Confirm", "Are you sure want to delete this record"):
            delete_lec_query = "delete from course where course_id = %s"
            mycursor.execute(delete_lec_query, (txtvar_of_courseid.get()))
            con_db.commit()
            reset()
            messagebox.showinfo('Done', 'Record is deleted')
        else:
            return True
    except Exception as err:
        messagebox.showwarning('Error','DB exception: %s' % err)



def insert():
    try:
        query = 'select * from lecturer where email=%s '
        mycursor.execute(query, (txtvar_of_lectemail.get()))
        row_lec_email = mycursor.fetchone()
        query = "select * from student where student_id=%s"
        mycursor.execute(query, (txtvar_of_studid.get()))
        row_studid = mycursor.fetchone()
        if txtvar_of_course_name.get() == '' or txtvar_of_department.get() == '' or txtvar_of_lectemail.get() == '' or txtvar_of_acadymic_year.get() == '' or txtvar_of_semester.get()== '' or txtvar_of_studid.get() == '':
            messagebox.showerror('Eror', 'All fields are required')
        elif row_lec_email is None:
            messagebox.showerror('Error', 'Lecturer email did not create yet')
        elif row_studid is None:
            messagebox.showerror('Error', 'Student Id does not exist')
        else:
            insert_lec_query = "insert into course(course_name,dept_name,lecturer_email,acadymic_year,semester,student_id) values(%s,%s,%s,%s,%s,%s)"
            mycursor.execute(insert_lec_query, (
                txtvar_of_course_name.get(), txtvar_of_department.get(), txtvar_of_lectemail.get(),
                txtvar_of_acadymic_year.get(), txtvar_of_semester.get(), txtvar_of_studid.get()))
            messagebox.showinfo('Done', 'Record is inserted')
            con_db.commit()
            reset()
    except Exception as err:
        messagebox.showwarning('Error','DB exception: %s' % err)


update_btn = Button(Course_data_frame,width=20,text="Update",pady=5,cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=update)
update_btn.place(x=410,y=150)

update_btn = Button(Course_data_frame,width=20,text="Delete",pady=5,cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=delete)
update_btn.place(x=630,y=150)

update_btn = Button(Course_data_frame,width=20,text="Insert",pady=5,cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=insert)
update_btn.place(x=840,y=150)

update_btn = Button(Course_data_frame,width=20,text="Clear Fields",pady=5,cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=clear)
update_btn.place(x=1060,y=150)


addcourse_window.mainloop()
