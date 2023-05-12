import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox , filedialog
import pymysql
import csv
import os

con_db = pymysql.connect(host='localhost', user='root', password='123456789')
mycursor = con_db.cursor()
query = 'use facerecognation_attendance_System'
mycursor.execute(query)
show_attendance_sheet_query=" select distinct stu.fullname,shee.date_time,shee.attend_course_name,DATE(shee.arrivaldate),stu.student_id , stu.acadymic_year, stu.semester from attendance_sheet shee  join student stu on left(shee.stud_name,5) = left(stu.fullname,5)  order by semester asc"

attendance_sheet_window = Tk()
attendance_sheet_window.title("Attendance Sheet")
attendance_sheet_window.geometry("1450x720+40+40")
attendance_sheet_window.config(bg="#ECF9FF")
attendance_sheet_window.resizable(False,False)
img_logo =tkinter.PhotoImage(file='logo.png',master=attendance_sheet_window)
attendance_sheet_window.iconphoto(False,img_logo)


atten_list_frame = LabelFrame(attendance_sheet_window,text="Attendance List")
#search_frame = LabelFrame(attendance_sheet_window,text="Search")
#atten_data_frame = LabelFrame(attendance_sheet_window,text="Student Data")

atten_list_frame.pack(fill="both",expand="yes",padx=20,pady=10)
#search_frame.pack(fill="both",expand="yes",padx=20,pady=10)
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
    trv.delete(*trv.get_children())
    for i in row:
        trv.insert('','end',values=i)

trv = ttk.Treeview(atten_list_frame, columns=(1,2,3,4,5,6,7),show="headings",height="10")
trv.place(x=5,y=80)
yscrollbar = ttk.Scrollbar(atten_list_frame,orient="vertical",command=trv.yview)
yscrollbar.pack(side=RIGHT,fill='y')
#styling the head of table
s = ttk.Style(trv)
s.theme_use('clam')
s.configure('Treeview.Heading', background="green3")


trv.column(1, anchor=CENTER)
trv.heading(1, text="student name")

trv.column(2, anchor=CENTER)
trv.heading(2, text="time")

trv.column(3, anchor=CENTER)
trv.heading(3, text="attend_course_name")

trv.column(4, anchor=CENTER)
trv.heading(4, text="attendance date")

trv.column(5, anchor=CENTER)
trv.heading(5, text="student_id")

trv.column(6, anchor=CENTER)
trv.heading(6, text="acadymic_year")

trv.column(7, anchor=CENTER)
trv.heading(7, text="semester")

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
                    query = "insert into attendance_sheet(stud_name,date_time,attend_course_name,arrivaldate) values(%s,%s,%s,now())"
                    mycursor.execute(query, (stud_name, date_time, attend_course_name))
                messagebox.showinfo("Data Saved", "Data has been saved to database")
                con_db.commit()
                reset()
            else:
                return False
        except Exception as err:
            messagebox.showerror("Error","%s" %err)


# make export and import and save buttons
exp_btn = Button(atten_list_frame,width=20,text="Export File CSV",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=exportfile)
exp_btn.place(x= 220, y=470)

imp_btn = Button(atten_list_frame,width=20,text="Import File CSV",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=importfile)
imp_btn.place(x= 450, y=470)

save_btn = Button(atten_list_frame,width=20,text="Save Data ",cursor='hand2',fg='white',background="#57a1f8",bd=0,activebackground="#ECF9FF",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=savefile)
save_btn.place(x= 680, y= 470)





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

reset_btn = Button(atten_list_frame,text="Reset",activebackground="#ECF9FF",bd=0,cursor="hand2",
                   width=20,background="#57a1f8",fg="white",
                   font=('Microsoft YaHei UI Light ',11,'bold'),command=reset)
reset_btn.place(x= 920, y= 470)
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

'''''''''
def search():
    q = search_entry.get()
    if q =='':
        messagebox.showerror('Error','Enter name to search')
    else:
        try:
            search_query = "select shee.stud_name,shee.date_time,shee.attend_course_name,DATE(shee.arrivaldate),stu.student_id , stu.acadymic_year, stu.semester from attendance_sheet shee join student stu on left(shee.stud_name,5) = left(stu.fullname,5) and stu.student_id like '%"+q+"%' order by semester asc"
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
'''''''''


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


attendance_sheet_window.mainloop()
