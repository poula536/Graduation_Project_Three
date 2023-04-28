create database facerecognation_attendance_System;
use facerecognation_attendance_System;

create table lecturer(
    full_name varchar(30) not null,
    email varchar(50),
    pass varchar(40) not null,
    department_name varchar(20) not null,
    constraint lecturer_pk primary key (email)
);


alter table lecturer add column department_name varchar(30) not null references department (dep_name) ;
alter table lecturer add constraint lect_dept_fk foreign key (department_name) references department(dep_name);
select * from lecturer;

create table admin(
	 full_name varchar(30) not null,
	 pass int,
     constraint admin_pk primary key (pass)
);
insert into admin values('poula mansour','320200029'),
						('abanoub maher','320200156'),
						('basil essam','320200028');
create table student
(
fname varchar(25),
lname varchar(25),
student_id int ,
constraint student_pk primary key (student_id)
);
alter table student add column department_name varchar(30) not null references department (dep_name);
#alter table student drop constraint student_dept_fk foreign key(department_id) references department(department_id);
alter table student drop column department_id int not null;
delete from student where student_id like '%320%'
select * from student;
create table course
(
course_name varchar(30) not null,
course_id int ,
lecturer_email varchar(50),
constraint course_pk primary key (course_id),
dept_name varchar(30) references department (dep_name)
);
alter table course add column student_id int;
alter table course add constraint course_student_fk foreign key (student_id) references student(student_id);
alter table course add column acadymic_year varchar(25) not null;
alter table course add column smaster varchar(25) not null;
create table department
(
dep_name varchar(30) not null,
department_id int ,
constraint department_pk primary key (department_id)
);
select * from department;
delete from department where department_id between 1 and 3
alter table department add constraint depname_pk primary key(dep_name);
insert into department values('علوم حاسب'),
							('نظم ومعلومات'),
                            ('اداره اعمال');
                            
						                    
                                                       
create table alldata
(
acadymic_year varchar(25) not null,
lec_email varchar(50),
stu_id int references student (student_id),
course_id int references course (course_id),
constraint alldata_pk primary key (stu_id),
constraint alldata_lect_fk foreign key(lec_email) references lecturer(email)
);
drop table alldata;
alter table alldata add column lec_email varchar(50);
alter table alldata add constraint alldata_lect_fk foreign key(lec_email) references lecturer(email);
insert into alldata (acadymic_year,lec_email,stu_id,course_id)values ('18/10/2000','poula@gmail.com',320200029,11);
update alldata set acadymic_year = '18/10/2000' where lec_email = 'poula@gmail.com';

select * from student;
insert into student values('poula','mansour',320200029,'علوم حاسب');
select * from course;

create table attendance_sheet
(
attendance_num int ,
date_time date not null,
course_id int references course(course_id),
statut int not null,
constraint attendancesheet_pk primary key(attendance_num)
);


create table face_record
(
 face_id varchar(50),
 constraint facerecord_pk primary key (face_id),
 atten_num int references attendance_sheet(attendance_num)
);


create table capture_photo
(
stu_id int references student(student_id) ,
face_id varchar(50) references face_record (face_id),
constraint capturephoto_pk primary key (stu_id)
);

#query to show table course and department
select co.course_name ,dep.dep_name from course co right outer join department dep on dep.dep_name= co.dept_name
union
select co.course_name ,dep.dep_name from course co right outer join department dep on dep.dep_name= co.dept_name; 

#insert into course (course_name ,course_id ,dept_name,acadymic_year,smaster) values( 'bussiness ' ,16,'اداره اعمال','22/23','first');

#query to show table lecturer that didn't have a course 
select distinct co.course_id , co.course_name, co.lecturer_email ,co.dept_name , lec.full_name , lec.email , lec.department_name
from course co right outer join lecturer lec on lec.email = co.lecturer_email and co.dept_name =  lec.department_name;

select  co.course_id , co.course_name, co.lecturer_email ,co.dept_name , lec.full_name , lec.email
from course co right outer join lecturer lec on lec.email = co.lecturer_email 
union
select  co.course_id , co.course_name, co.lecturer_email ,co.dept_name , lec.full_name , lec.email
from course co left outer join lecturer lec on lec.email = co.lecturer_email ;

select  co.course_id , co.course_name, co.lecturer_email ,co.dept_name , lec.full_name , lec.email
from course co  join lecturer lec on lec.email = co.lecturer_email ;

#query to show table course and student
select  co.course_id ,co.course_name , co.student_id ,co.dept_name , co.acadymic_year , co.smaster, stu.fname , stu.lname ,stu.student_id
from course co right outer join student stu on co.student_id = stu.student_id
union all
select  co.course_id ,co.course_name,co.student_id , co.dept_name , co.acadymic_year , co.smaster, stu.fname , stu.lname ,stu.student_id
from course co left outer join student stu on co.student_id = stu.student_id;

select * from course;
update course set lecturer_email = 'asmaa@gmail.com' where course_name ='bussiness ';

select  co.course_id , co.course_name, co.lecturer_email ,co.dept_name , lec.full_name , lec.email
from course co left outer join lecturer lec on lec.email = co.lecturer_email ;

select * from lecturer;