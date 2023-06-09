create database facerecognation_attendance_System;
use facerecognation_attendance_System;

create table lecturer(
	lec_id int AUTO_INCREMENT,
    full_name varchar(30) not null,
    email varchar(50) unique not null,
    pass varchar(40) not null,
    department_name varchar(20) not null,
    constraint lecturer_pk primary key (lec_id)
);

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
constraint student_pk primary key (student_id),
lecturer_id int references lecturer (lecturer_ID) 
);


create table course
(
course_name varchar(30) not null,
course_id int ,
constraint course_pk primary key (course_id),
dept_id int references department (department_id)
);

create table department
(
dep_name varchar(30) not null,
detartment_id int ,
constraint department_pk primary key (detartment_id)
);


create table alldata
(
acadymic_year varchar(25) not null,
lec_id int references lecturer (lecturer_ID),
stu_id int references student (student_id),
course_id int references course (course_id),
constraint alldata_pk primary key (stu_id)
);


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

select * from lecturer where email ='poula@gmail.com' and pass ='1234'

select full_name from lecturer where email='poula@gmail.com'
