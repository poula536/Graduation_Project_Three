import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox , filedialog
import pymysql
import csv
import os

con_db = pymysql.connect(host='localhost', user='root', password='123456789')
mycursor = con_db.cursor()
query = 'use facerecognation_attendance_System'
mycursor.execute(query)
show_attendance_sheet_query=" select distinct shee.stud_name,shee.date_time,shee.attend_course_name,stu.fullname,stu.student_id , stu.acadymic_year, stu.semester from attendance_sheet shee  join student stu on left(shee.stud_name,5) = left(stu.fullname,5)  order by semester asc"

attendance_sheet_window = Tk()
attendance_sheet_window.title("Attendance Sheet")
attendance_sheet_window.geometry("1450x720+40+40")
attendance_sheet_window.config(bg="#ECF9FF")
attendance_sheet_window.resizable(False,False)
img_logo =tkinter.PhotoImage(file='logo.png',master=attendance_sheet_window)
attendance_sheet_window.iconphoto(False,img_logo)


atten_list_frame = LabelFrame(attendance_sheet_window,text="Attendance List")
search_frame = LabelFrame(attendance_sheet_window,text="Search")
#atten_data_frame = LabelFrame(attendance_sheet_window,text="Student Data")

atten_list_frame.pack(fill="both",expand="yes",padx=20,pady=10)
search_frame.pack(fill="both",expand="yes",padx=20,pady=10)
#atten_data_frame.pack(fill="both",expand="yes" ,padx=20,pady=10)


def backfw_btn():
    attendance_sheet_window.withdraw()
    import dashboard_admin
    dashboard_admin.admin_dashboard_window.deiconify()

bfw_btn = tkinter.PhotoImage(file='backfw.png',master=attendance_sheet_window)
back_forward_btn = Button(atten_list_frame,cursor='hand2',image=bfw_btn,bd=0,
                          bg="#ECF9FF",activebackground="#ECF9FF",height=60,width=60,command=backfw_btn)
back_forward_btn.place(x=10,y=5)
mydata = []
def showdata(row):
    global mydata
    mydata = list(row)
    my_var.set(str(len(mydata)))
    trv.delete(*trv.get_children())
    for i in row:
        trv.insert('','end',values=i)
    

trv = ttk.Treeview(atten_list_frame, columns=(1,2,3,4,5,6),show="headings",height="7")
trv.pack()

#styling the head of table
s = ttk.Style(trv)
s.theme_use('clam')
s.configure('Treeview.Heading', background="green3")


trv.column(1, anchor=CENTER)
trv.heading(1, text="student name")

trv.column(2, anchor=CENTER)
trv.heading(2, text="date_time")

trv.column(3, anchor=CENTER)
trv.heading(3, text="attend_course_name")

trv.column(4, anchor=CENTER)
trv.heading(4, text="student_id")

trv.column(5, anchor=CENTER)
trv.heading(5, text="acadymic_year")

trv.column(6, anchor=CENTER)
trv.heading(6, text="semester")
#student list section

def exportfile():
    if len(mydata) < 1:
        messagebox.showerror('Error', 'There is now data to export')
        return False
    else:
        file = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV",
                                            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
        with open(file, mode='w', encoding="utf-8") as myfile:
            file_writer = csv.writer(myfile, delimiter=",")
            for i in mydata:
                file_writer.writerow(i)
        messagebox.showinfo('Data Exported',
                            'Your data has been exported to ' + os.path.basename(file) + ' succesfully.')

def importfile():
    mydata.clear()
    file = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                        filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")))
    with open(file) as myfile:
        csvread = csv.reader(myfile,delimiter=",")
        for i in csvread:
            mydata.append(i)
    showdata(mydata)



def savefile():
        try:
            if messagebox.askyesno("Confirmation", "Are you sure you wnat to save to database"):
                for i in mydata:
                    stud_name = i[0]
                    date_time = i[1]
                    attend_course_name = i[2]
                    query = "insert into attendance_sheet(stud_name,date_time,attend_course_name) values(%s,%s,%s)"
                    mycursor.execute(query, (stud_name, date_time, attend_course_name))
                con_db.commit()
                reset()
                messagebox.showinfo("Data Saved", "Data has been saved to database")
            else:
                return False
        except Exception as err:
            messagebox.showerror("Error","%s" %err)


# make export and import and save buttons
exp_btn = Button(atten_list_frame,width=20,text="Export File CSV",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=exportfile)
exp_btn.place(x= 420, y=210)

imp_btn = Button(atten_list_frame,width=20,text="Import File CSV",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=importfile)
imp_btn.place(x= 620, y=210)

save_btn = Button(atten_list_frame,width=20,text="Save Data ",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=savefile)
save_btn.place(x= 820, y= 210)

#عدد الحضور 

attendees_labl = Label(atten_list_frame,fg="#12B371",text="The number of attendees:",font=('Microsoft YaHei UI Light ',15,'bold'))
attendees_labl.place(x=100,y=210)
my_var = tk.StringVar()
my_var.set(str(len(mydata)))
my_label = tk.Label(atten_list_frame, textvariable=my_var,fg="#12B371",font=('Microsoft YaHei UI Light ',25,'bold'))
my_label.place(x=220, y=250)

#show the table of the lecturer
try:
    mycursor.execute(show_attendance_sheet_query)
    row = mycursor.fetchall()
    showdata(row)
except Exception as err:
    messagebox.showwarning('Error', 'DB exception: %s' % err)

#reset btn
def reset():
    try:
        mycursor.execute(show_attendance_sheet_query)
        row = mycursor.fetchall()
        showdata(row)
    except Exception as err:
        messagebox.showwarning('Error', 'DB exception: %s' % err)

#search section

#get data
txtvar_of_stud_name = StringVar(master=attendance_sheet_window)
txtvar_of_date_time = StringVar(master=attendance_sheet_window)
txtvar_of_attend_course_name = StringVar(master=attendance_sheet_window)
txtvar_of_student_id= StringVar(master=attendance_sheet_window)
txtvar_of_acadymic_year= StringVar(master=attendance_sheet_window)
txtvar_of_semester= StringVar(master=attendance_sheet_window)
#search for record
#txtvar_of_search = StringVar()
def search():
    q = search_entry.get()
    if q =='':
        messagebox.showerror('Error','Enter name to search')
    else:
        try:
            search_query = "select shee.stud_name,shee.date_time,shee.attend_course_name,stu.student_id , stu.acadymic_year, stu.semester from attendance_sheet shee join student stu on left(shee.stud_name,5) = left(stu.fullname,5) and stu.student_id like '%"+q+"%' order by semester asc"
            mycursor.execute(search_query)
            row = mycursor.fetchall()#list of rows
            showdata(row)
        except Exception as err:
            messagebox.showwarning('Error', 'DB exception: %s' % err)

search_labl = Label(search_frame,text="Search",font=('Microsoft YaHei UI Light ',10,'bold'))
search_labl.pack(side=tkinter.LEFT,padx=10)
search_entry = Entry(search_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                     font=('Microsoft YaHei UI Light ',15))
search_entry.pack(side=tkinter.LEFT, padx=20)

serch_btn = Button(search_frame,text="Search",activebackground="#ECF9FF",bd=0,cursor="hand2",
                   width=10,pady=5,background="#57a1f8",fg="white",
                   font=('Microsoft YaHei UI Light ',10,'bold'),command=search)
serch_btn.pack(side=tkinter.LEFT , padx=6)

reset_btn = Button(search_frame,text="Reset",activebackground="#ECF9FF",bd=0,cursor="hand2",
                   width=10,pady=5,background="#57a1f8",fg="white",
                   font=('Microsoft YaHei UI Light ',10,'bold'),command=reset)
reset_btn.pack(side=tkinter.LEFT,padx=6)

#student data section to update

def getrow(event):
    row_data = trv.identify_row(event.y)
    data = trv.item(trv.focus())
    txtvar_of_stud_name.set(data['values'][0])
    txtvar_of_date_time.set(data['values'][1])
    txtvar_of_attend_course_name.set(data['values'][2])
    txtvar_of_student_id.set(data['values'][3])
    txtvar_of_acadymic_year.set(data['values'][4])
    txtvar_of_semester.set(data['values'][5])

trv.bind("<Double-1>", getrow)

'''''''''
#start Lecturer ID
stud_id_label = Label(atten_data_frame,text="Student ID",font=('Microsoft YaHei UI Light ',10,'bold'))
stud_id_label.grid(row=0,column=0,padx=5,pady=3)

stud_id_entry = Entry(atten_data_frame,state="disabled" ,width=25,fg='#181823',border=1,bg="#ECF9FF",
                        font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_stud_name)
stud_id_entry.grid(row=0,column=1,padx=5,pady=3)
#end Lecturer ID

#start Full Name
stud_fullname_label = Label(atten_data_frame, text="Full Name",
                        font=('Microsoft YaHei UI Light ',10,'bold'))
stud_fullname_label.grid(row=1,column=0,padx=5,pady=3)
stud_fullname_entry = Entry(atten_data_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                        font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_date_time)
stud_fullname_entry.grid(row=1,column=1,padx=5,pady=3)
#end Full Name

#start Email
acadymicyear_label = Label(atten_data_frame, text="Acadymic Year",
                        font=('Microsoft YaHei UI Light ',10,'bold'))
acadymicyear_label.grid(row=2,column=0,padx=5,pady=3)
acadymicyear_entry = Entry(atten_data_frame,width=25,fg='#181823',border=1,bg="#ECF9FF",
                        font=('Microsoft YaHei UI Light ',11),textvariable=txtvar_of_attend_course_name)
acadymicyear_entry.grid(row=2,column=1,padx=5,pady=3)
#end Email

#start Password
semester_label = Label(atten_data_frame, text="Semester",
                         font=('Microsoft YaHei UI Light ',10,'bold'))
semester_label.grid(row=3,column=0,padx=5,pady=3)
semester_combobox = ttk.Combobox(atten_data_frame, width=31, textvariable=txtvar_of_student_id)

semester_combobox['values'] = ('first','second')

semester_combobox.grid(row=3,column=1,padx=5,pady=3)
#end Password

#

dept_combobox = ttk.Combobox(atten_data_frame, width=15, textvariable=txtvar_of_acadymic_year)

password_label = Label(atten_data_frame, text="Department",
                         font=('Microsoft YaHei UI Light ',10,'bold'))
password_label.grid(row=0,column=2,padx=5,pady=3)
# Adding combobox drop down list
dept_combobox['values'] = (' علوم حاسب',
                          ' نظم ومعلومات',
                          ' اداره اعمال',
                          )

dept_combobox.grid(row=0,column=3,padx=5,pady=3)
'''''
'''''''''
#
def clear():
    txtvar_of_stuid.set('')
    stud_fullname_entry.delete(0,END)
    acadymicyear_entry.delete(0,END)
    txtvar_of_semester.set('')
    txtvar_of_department.set('')
    search_entry.delete(0, END)


def update():
    try:
        query = 'select * from student where student_id=%s '
        mycursor.execute(query, (txtvar_of_stuid.get()))
        row_studid = mycursor.fetchone()
        if txtvar_of_full_name.get() == '' or txtvar_of_acadymic.get() == '' or txtvar_of_semester.get() == '' or txtvar_of_department.get() == '':
            messagebox.showerror('Eror', 'All fields are required')
        elif row_studid is None:
            messagebox.showerror('Error', 'This Student not in the system')
        else:
            t1 = txtvar_of_full_name.get()
            t2 = txtvar_of_acadymic.get()
            t3 = txtvar_of_semester.get()
            t4 = txtvar_of_department.get()
            t5 = txtvar_of_stuid.get()
            if messagebox.askyesno("Confirm", "Are you sure want to update"):
                update_query = "update student set fullname=%s , acadymic_year=%s , semester=%s , department_name=%s where student_id =%s"
                mycursor.execute(update_query, (t1,t2,t3,t4,t5))
                con_db.commit()
                reset()
                messagebox.showinfo('Done', 'Updated Successfully')
            else:
                return True
    except Exception as err:
        messagebox.showwarning('Error','DB exception: %s' % err)


def delete():
    try:
        if txtvar_of_stuid.get() == '' or txtvar_of_full_name.get() == '' or txtvar_of_acadymic.get() == '' or txtvar_of_semester.get() == '' or txtvar_of_department.get() == '':
            messagebox.showerror('Eror', 'All fields are required')
        elif messagebox.askyesno("Confirm", "Are you sure want to delete this record"):
            delete_query = "delete from student where student_id = %s"
            mycursor.execute(delete_query, (txtvar_of_stuid.get()))
            con_db.commit()
            reset()
            messagebox.showinfo('Done', 'Record is deleted')
        else:
            return True
    except Exception as err:
        messagebox.showwarning('Error','DB exception: %s' % err)



def insert():
    try:
        query = 'select * from student where student_id=%s '
        mycursor.execute(query, (txtvar_of_stuid.get()))
        row_stu_id = mycursor.fetchone()
        if txtvar_of_stuid.get() == '' or txtvar_of_full_name.get() == '' or txtvar_of_acadymic.get() == '' or txtvar_of_semester.get()== '' or txtvar_of_department.get() == '':
            messagebox.showerror('Eror', 'All fields are required')
        elif row_stu_id is not None:
            messagebox.showerror("Error", 'This record is already exist')
        else:
            insert_query = "insert into student(student_id,fullname,acadymic_year,semester,department_name) values(%s,%s,%s,%s,%s)"
            mycursor.execute(insert_query, (
                txtvar_of_stuid.get(), txtvar_of_full_name.get(), txtvar_of_acadymic.get(),txtvar_of_semester.get(),
                txtvar_of_department.get()))
            messagebox.showinfo('Done', 'Record is inserted')
            con_db.commit()
            reset()
    except Exception as err:
        messagebox.showwarning('Error','DB exception: %s' % err)


update_btn = Button(stud_data_frame,width=20,text="Update",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=update)
update_btn.place(x=310,y=150)

update_btn = Button(stud_data_frame,width=20,text="Delete",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=delete)
update_btn.place(x=510,y=150)

update_btn = Button(stud_data_frame,width=20,text="Insert",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=insert)
update_btn.place(x=710,y=150)

update_btn = Button(stud_data_frame,width=20,text="Clear Fields",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=clear)
update_btn.place(x=910,y=150)

'''''


attendance_sheet_window.mainloop()
