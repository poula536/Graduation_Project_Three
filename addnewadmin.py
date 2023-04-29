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
new_admin_window.title("Add Doctor")
new_admin_window.geometry("1450x720+40+40")
new_admin_window.config(bg="#ECF9FF")
new_admin_window.resizable(False,False)
img_logo =tkinter.PhotoImage(file='logo.png',master=new_admin_window)
new_admin_window.iconphoto(False,img_logo)


admin_list_frame = LabelFrame(new_admin_window,text="Admin List")
search_frame = LabelFrame(new_admin_window,text="Search")
admin_data_frame = LabelFrame(new_admin_window,text="Admin Data")

admin_list_frame.pack(fill="both",expand="yes",padx=20,pady=10)
search_frame.pack(fill="both",expand="yes",padx=20,pady=10)
admin_data_frame.pack(fill="both",expand="yes" ,padx=20,pady=10)

def backfw_btn():
    new_admin_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=new_admin_window)
back_forward_btn = Button(admin_list_frame,cursor='hand2',image=bfw_btn,bd=0,
                          bg="#ECF9FF",activebackground="#ECF9FF",height=60,width=60,command=backfw_btn)
back_forward_btn.place(x=10,y=5)


def showdata(row):
    trv.delete(*trv.get_children())
    for i in row:
        trv.insert('','end',values=i)

#styling the head of table
s = ttk.Style(new_admin_window)
s.theme_use('clam')
s.configure('Treeview.Heading', background="green3")

trv = ttk.Treeview(admin_list_frame, columns=(1,2,3),show="headings",height="7")
trv.pack()

trv.column(1, anchor=CENTER)
trv.heading(1, text="Admin Id")

trv.column(2, anchor=CENTER)
trv.heading(2, text="Admin Name")

trv.column(3, anchor=CENTER)
trv.heading(3, text="Password")


#show the table of the lecturer
try:
    mycursor.execute(show_table_admin_query)
    row = mycursor.fetchall()
    showdata(row)
except Exception as err:
    messagebox.showwarning('Error', 'DB exception: %s' % err)

#reset btn
def reset():
    try:
        mycursor.execute(show_table_admin_query)
        row = mycursor.fetchall()
        showdata(row)
    except Exception as err:
        messagebox.showwarning('Error', 'DB exception: %s' % err)


#search section
#get data
txtvar_of_admnid = StringVar(master=new_admin_window)
txtvar_of_fullname = StringVar(master=new_admin_window)
txtvar_of_password = StringVar(master=new_admin_window)

#search for record
#txtvar_of_search = StringVar()
def search():
    q = search_entry.get()
    if q =='':
        messagebox.showerror('Error','Enter name to search')
    else:
        try:
            search_query = "select * from admin where admin_id like '%"+q+"%' or full_name like '%"+q+"%'"
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

#admin data section to update

def getrow(event):
    row_data = trv.identify_row(event.y)
    data = trv.item(trv.focus())
    txtvar_of_admnid.set(data['values'][0])
    txtvar_of_fullname.set(data['values'][1])
    txtvar_of_password.set(data['values'][2])


trv.bind("<Double-1>", getrow)

#start admin ID
admin_id_label = Label(admin_data_frame, text="Admin ID",font=('Microsoft YaHei UI Light ',10,'bold'))
admin_id_label.grid(row=0,column=0,padx=5,pady=3)

admin_id_entry = Entry(admin_data_frame,state='disabled',width=25,fg='#181823',border=1,bg="#ECF9FF",
                        font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_admnid)
admin_id_entry.grid(row=0,column=1,padx=5,pady=3)
#end admin ID

#start Full Name
admin_fullname_label = Label(admin_data_frame, text="Full Name",
                        font=('Microsoft YaHei UI Light ',10,'bold'))
admin_fullname_label.grid(row=1,column=0,padx=5,pady=3)

admin_fullname_entry = Entry(admin_data_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                        font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_fullname)
admin_fullname_entry.grid(row=1,column=1,padx=5,pady=3)
#end Full Name

#start Password
password_label = Label(admin_data_frame, text="Password",
                         font=('Microsoft YaHei UI Light ',10,'bold'))
password_label.grid(row=2,column=0,padx=5,pady=3)
dpassword_entry = Entry(admin_data_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                         font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_password)
dpassword_entry.grid(row=2,column=1,padx=5,pady=3)
#end Password

def clear():
    txtvar_of_admnid.set('')
    admin_fullname_entry.delete(0,END)
    dpassword_entry.delete(0,END)
    search_entry.delete(0, END)


def update():
    try:
        query = 'select * from admin where full_name=%s '
        mycursor.execute(query, (txtvar_of_admnid.get()))
        row_fullname= mycursor.fetchone()
        if txtvar_of_admnid.get() == '' or txtvar_of_fullname.get() == '' or txtvar_of_password.get() == '':
            messagebox.showerror('Eror', 'All fields are required')
        elif row_fullname is None:
            messagebox.showerror('Error', 'This Admin did not create yet')
        else:
            t1 = txtvar_of_fullname.get()
            t2 = txtvar_of_password.get()
            if messagebox.askyesno("Confirm", "Are you sure want to update"):
                update_email_query = "update admin set full_name=%s ,  pass=%s"
                mycursor.execute(update_email_query, (t1,t2))
                con_db.commit()
                reset()
                messagebox.showinfo('Done', 'Updated Successfully')
            else:
                return True
    except Exception as err:
        messagebox.showwarning('Error','DB exception: %s' % err)


def delete():
    try:
        if txtvar_of_admnid.get() == '' or txtvar_of_fullname.get() == '' or txtvar_of_password.get() == '':
            messagebox.showerror('Eror', 'All fields are required')
        elif messagebox.askyesno("Confirm", "Are you sure want to delete this record"):
            delete_lec_query = "delete from admin where admin_id = %s"
            mycursor.execute(delete_lec_query, (txtvar_of_admnid.get()))
            con_db.commit()
            reset()
            messagebox.showinfo('Done', 'Record is deleted')
        else:
            return True
    except Exception as err:
        messagebox.showwarning('Error','DB exception: %s' % err)



def insert():
    try:
        query = 'select * from admin where admin_id=%s '
        mycursor.execute(query, (txtvar_of_admnid.get()))
        row_admin_id = mycursor.fetchone()
        if txtvar_of_fullname.get() == '' or txtvar_of_password.get() == '':
            messagebox.showerror('Eror', 'All fields are required')
        elif row_admin_id is not None:
            messagebox.showerror("Error", 'This record is already exist')
        else:
            insert_lec_query = "insert into admin(full_name,pass)values values(%s,%s)"
            mycursor.execute(insert_lec_query, (txtvar_of_fullname.get(),txtvar_of_password.get()))
            messagebox.showinfo('Done', 'Record is inserted')
            con_db.commit()
            reset()
    except Exception as err:
        messagebox.showwarning('Error','DB exception: %s' % err)


update_btn = Button(admin_data_frame,width=20,text="Update",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=update)
update_btn.place(x=310,y=150)

update_btn = Button(admin_data_frame,width=20,text="Delete",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=delete)
update_btn.place(x=510,y=150)

update_btn = Button(admin_data_frame,width=20,text="Insert",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=insert)
update_btn.place(x=710,y=150)

update_btn = Button(admin_data_frame,width=20,text="Clear Fields",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=clear)
update_btn.place(x=910,y=150)


new_admin_window.mainloop()
