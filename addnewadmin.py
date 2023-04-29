'''''''''
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql

new_admin_window = Tk()
new_admin_window.title('Add Admin')
new_admin_window.geometry("925x500+300+200")
new_admin_window.config(bg="#ECF9FF")
new_admin_window.resizable(False, False)
img_logo = tkinter.PhotoImage(file='logo.png', master=new_admin_window)
new_admin_window.iconphoto(False, img_logo)
def backfw_btn():
    new_admin_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=new_admin_window)
back_forward_btn = Button(new_admin_window,cursor='hand2',image=bfw_btn,bd=0,bg="#ECF9FF",activebackground="#ECF9FF",height=80,width=80,command=backfw_btn)
back_forward_btn.place(x=10,y=5)


img_logo = tkinter.PhotoImage(file='logo.png',master=new_admin_window)
Label(new_admin_window, bg="white",image=img_logo ,background="#ECF9FF").place(x=50, y=120)
frame = Frame(new_admin_window, width=350, height=400, bg="#ECF9FF")
frame.place(x=480, y=50)

heading = Label(frame, text="انشاء حساب جديد", fg="black", bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 25, 'bold'))
heading.place(x=100, y=10)


def on_enter(e):
    newadmin_fullname_entry.delete(0, 'end')


def on_leave(e):
    name = newadmin_fullname_entry.get()
    if name == '':
        newadmin_fullname_entry.insert(0, 'اسم المستخدم كامل')

newadmin_fullname_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
newadmin_fullname_entry.place(x=30, y=135)
newadmin_fullname_entry.insert(0, 'اسم المستخدم كامل')
newadmin_fullname_entry.bind('<FocusIn>', on_enter)
newadmin_fullname_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=160)


#password
def on_enter(e):
    password_entry.delete(0, 'end')


def on_leave(e):
    password = password_entry.get()
    if password == '':
        password_entry.insert(0, 'كلمه السر')


password_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
password_entry.place(x=30, y=205)
password_entry.insert(0, 'كلمه السر')
password_entry.bind('<FocusIn>', on_enter)
password_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=230)


def on_enter(e):
    conf_pass_entry.delete(0, 'end')


def on_leave(e):
    confirm_password = conf_pass_entry.get()
    if confirm_password == '':
        conf_pass_entry.insert(0, 'تاكيد كلمه السر')


conf_pass_entry = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
conf_pass_entry.place(x=30, y=280)
conf_pass_entry.insert(0, 'تاكيد كلمه السر')
conf_pass_entry.bind('<FocusIn>', on_enter)
conf_pass_entry.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=305)
#End password

def clear():
    newadmin_fullname_entry.delete(0,END)
    newadmin_fullname_entry.insert(0,'اسم المستخدم كامل')

    conf_pass_entry.delete(0, END)
    conf_pass_entry.insert(0,'تاكيد كلمه السر')

    password_entry.delete(0, END)
    password_entry.insert(0,'كلمه السر')


#connect to database
def addDoctor():
    con_db=pymysql.connect(host='localhost',user='root',password='123456789')
    mycursor = con_db.cursor()
    query = 'use facerecognation_attendance_System'
    mycursor.execute(query)
    query = 'select * from admin where full_name=%s'
    mycursor.execute(query, (newadmin_fullname_entry.get()))
    row2 = mycursor.fetchone()
    if row2 != None:
        messagebox.showerror('Error', 'Name already exists')
    else:
        query = 'insert into admin(full_name,pass) values(%s,%s)'
        mycursor.execute(query, (newadmin_fullname_entry.get(),password_entry.get()))
        messagebox.showinfo('Done', 'Registration is done successfully')
        con_db.commit()
        con_db.close()


def creat_account():
    if newadmin_fullname_entry.get()=='اسم المستخدم كامل' or password_entry.get()=='كلمه السر' or conf_pass_entry.get()=='تاكيد كلمه السر':
        messagebox.showerror('Error', 'all fields are required')
    elif password_entry.get()!= conf_pass_entry.get():
        messagebox.showerror('Error','Password must be the same')
    else:
        addDoctor()
        clear()


btn_login = Button(frame, cursor='hand2',width=39, pady=7, text="انشاء الحساب ",
                   bg="#57a1f8", fg='white', border=0,command=creat_account)
btn_login.place(x=35, y=360)

new_admin_window.mainloop()
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
show_table_admin_query="select * from admin"

new_admin_window = Tk()
new_admin_window.title("Add Admin")
new_admin_window.geometry("1450x720+40+40")
new_admin_window.config(bg="#ECF9FF")
new_admin_window.resizable(False,False)
img_logo =tkinter.PhotoImage(file='logo.png',master=new_admin_window)
new_admin_window.iconphoto(False,img_logo)


course_list_frame = LabelFrame(new_admin_window,text="Admin List")
search_frame = LabelFrame(new_admin_window,text="Search")
course_data_frame = LabelFrame(new_admin_window,text="Admin Data")

course_list_frame.pack(fill="both",expand="yes",padx=20,pady=10)
search_frame.pack(fill="both",expand="yes",padx=20,pady=10)
course_data_frame.pack(fill="both",expand="yes",padx=20,pady=10)

def backfw_btn():
    new_doctor_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=new_doctor_window)
back_forward_btn = Button(course_list_frame,cursor='hand2',image=bfw_btn,bd=0,
                          bg="#ECF9FF",activebackground="#ECF9FF",height=60,width=60,command=backfw_btn)
back_forward_btn.place(x=10,y=5)



def showdata(row):
    trv.delete(*trv.get_children())
    for i in row:
        trv.insert('','end',values=i)

#styling the head of table
s = ttk.Style(new_doctor_window)
s.theme_use('clam')
s.configure('Treeview.Heading', background="green3")

trv = ttk.Treeview(course_list_frame, columns=(1,2,3,4,5),show="headings",height="7")
trv.pack()

trv.column(1, anchor=CENTER)
trv.heading(1, text="lecturer_id")

trv.column(2, anchor=CENTER)
trv.heading(2, text="full_name")

trv.column(3, anchor=CENTER)
trv.heading(3, text="email")

trv.column(4, anchor=CENTER)
trv.heading(4, text="pass")

trv.column(5, anchor=CENTER)
trv.heading(5, text="dep_name")


#show the table of the lecturer
try:
    mycursor.execute(show_table_lect_query)
    row = mycursor.fetchall()
    showdata(row)
except Exception as err:
    messagebox.showwarning('Error', 'DB exception: %s' % err)

#reset btn
def reset():
    try:
        mycursor.execute(show_table_lect_query)
        row = mycursor.fetchall()
        showdata(row)
    except Exception as err:
        messagebox.showwarning('Error', 'DB exception: %s' % err)

#search for record
#txtvar_of_search = StringVar()
def search():
    q = search_entry.get()
    if q =='':
        messagebox.showerror('Error','Enter name to search')
    else:
        try:
            search_query = "select * from lecturer where full_name like '%"+q+"%' "
            mycursor.execute(search_query)
            row = mycursor.fetchall()
            showdata(row)
        except Exception as err:
            messagebox.showwarning('Error', 'DB exception: %s' % err)




#search section
search_labl = Label(search_frame,text="Search by name",font=('Microsoft YaHei UI Light ',10,'bold'))
search_labl.pack(side=tkinter.LEFT,padx=10)
search_entry = Entry(search_frame,
                     width=25,fg='#181823',border=1,bg="#ECF9FF",font=('Microsoft YaHei UI Light ',15))
search_entry.pack(side=tkinter.LEFT, padx=20)

serch_btn = Button(search_frame,text="Search",activebackground="#ECF9FF",bd=0,cursor="hand2",
                   width=10,pady=5,background="#57a1f8",fg="white",font=('Microsoft YaHei UI Light ',10,'bold'),command=search)
serch_btn.pack(side=tkinter.LEFT , padx=6)

reset_btn = Button(search_frame,text="Reset",activebackground="#ECF9FF",bd=0,cursor="hand2",
                   width=10,pady=5,background="#57a1f8",fg="white",font=('Microsoft YaHei UI Light ',10,'bold'),command=reset)
reset_btn.pack(side=tkinter.LEFT,padx=6)

#Course data section to update
#get data
txtvar_of_lecid = StringVar(master=new_doctor_window)
txtvar_of_full_name = StringVar(master=new_doctor_window)
txtvar_of_lectemail = StringVar(master=new_doctor_window)
txtvar_of_password = StringVar(master=new_doctor_window)
txtvar_of_department = StringVar(master=new_doctor_window)
def getrow(event):
    row_data = trv.identify_row(event.y)
    data = trv.item(trv.focus())
    txtvar_of_lecid.set(data['values'][0])
    txtvar_of_full_name.set(data['values'][1])
    txtvar_of_lectemail.set(data['values'][2])
    txtvar_of_password.set(data['values'][3])
    txtvar_of_department.set(data['values'][4])

trv.bind("<Double-1>", getrow)

#start Lecturer ID
course_name_label = Label(course_data_frame, text="Lecturer ID",font=('Microsoft YaHei UI Light ',10,'bold'))
course_name_label.grid(row=0,column=0,padx=5,pady=3)

course_name_entry = Entry(course_data_frame,state='disabled',width=25,fg='#181823',border=1,bg="#ECF9FF",
                        font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_lecid)
course_name_entry.grid(row=0,column=1,padx=5,pady=3)
#end Lecturer ID

#start Full Name
lec_email_label = Label(course_data_frame, text="Full Name",
                        font=('Microsoft YaHei UI Light ',10,'bold'))
lec_email_label.grid(row=1,column=0,padx=5,pady=3)
lec_email_entry = Entry(course_data_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                        font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_full_name)
lec_email_entry.grid(row=1,column=1,padx=5,pady=3)
#end Full Name

#start Email
lec_email_label = Label(course_data_frame, text="Email",
                        font=('Microsoft YaHei UI Light ',10,'bold'))
lec_email_label.grid(row=2,column=0,padx=5,pady=3)
lec_email_entry = Entry(course_data_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                        font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_lectemail)
lec_email_entry.grid(row=2,column=1,padx=5,pady=3)
#end Email

#start Password
department_label = Label(course_data_frame, text="Password",
                         font=('Microsoft YaHei UI Light ',10,'bold'))
department_label.grid(row=3,column=0,padx=5,pady=3)
department_entry = Entry(course_data_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                         font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_password)
department_entry.grid(row=3,column=1,padx=5,pady=3)
#end Password

#
dept_combobox = ttk.Combobox(course_data_frame, width=15, textvariable=txtvar_of_department)

# Adding combobox drop down list
dept_combobox['values'] = (' علوم حاسب',
                          ' نظم ومعلومات',
                          ' اداره اعمال',
                          )

dept_combobox.place(x=340 , y=5)
#
try:
    def clear():
        txtvar_of_lecid.set(' ')
        txtvar_of_full_name.set(' ')
        txtvar_of_lectemail.set(' ')
        txtvar_of_password.set(' ')
        txtvar_of_department.set(' ')

    def update():

        query = 'select * from lecturer where email=%s '
        mycursor.execute(query, (txtvar_of_lectemail.get()))
        row_email = mycursor.fetchone()
        if txtvar_of_lectemail.get() == '' or txtvar_of_full_name.get() == '' or txtvar_of_password.get() == '' or txtvar_of_department.get() == '':
            messagebox.showerror('Eror', 'All fields are required')
        elif row_email is None:
            messagebox.showerror('Error', 'This Email did not create yet')
        else:
            if messagebox.askyesno("Confirm", "Are you sure want to update"):
                update_email_query = 'update course set full_name =%s , email =%s , pass =%s , department_name =%s  where lecturer_id =%s'
                mycursor.execute(update_email_query, (
                txtvar_of_full_name.get(), txtvar_of_lectemail.get(), txtvar_of_password.get(),
                txtvar_of_department.get(), txtvar_of_lecid.get()))
                con_db.commit()
                reset()
                messagebox.showinfo('Done', 'Updated Successfully')
            else:
                return True

    def delete():
        if messagebox.askyesno("Confirm", "Are you sure want to delete this record"):
            delete_lec_query = "delete from lecturer where lecturer_id = %s"
            mycursor.execute(delete_lec_query,(txtvar_of_lecid.get()))
            con_db.commit()
            reset()
            messagebox.showinfo('Done','Record is deleted')
        else:
            return True

    def insert():
        query = 'select * from lecturer where lecturer_id=%s '
        mycursor.execute(query, (txtvar_of_lecid.get()))
        row_lec_id = mycursor.fetchone()
        if txtvar_of_lectemail.get() == ' ' or txtvar_of_full_name.get() == ' ' or txtvar_of_password.get() == ' ' or txtvar_of_department.get() == ' ':
            messagebox.showerror('Eror', 'All fields are required')
        elif row_lec_id is not None:
            messagebox.showerror("Error",'This record is already exist')
        else:
            insert_lec_query = "insert into lecturer(full_name,email,pass,dep_name) values(%s,%s,%s,%s)"
            mycursor.execute(insert_lec_query, (
            txtvar_of_full_name.get(), txtvar_of_lectemail.get(), txtvar_of_password.get(), txtvar_of_department.get()))
            con_db.commit()
            reset()

except Exception as err:
        messagebox.showwarning('Error','DB exception: %s' % err)

update_btn = Button(course_data_frame,width=20,text="Update",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=update)
update_btn.place(x=310,y=150)

update_btn = Button(course_data_frame,width=20,text="Delete",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=delete)
update_btn.place(x=510,y=150)

update_btn = Button(course_data_frame,width=20,text="Insert",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=insert)
update_btn.place(x=710,y=150)

update_btn = Button(course_data_frame,width=20,text="Clear Fields",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=clear)
update_btn.place(x=910,y=150)
new_doctor_window.mainloop()