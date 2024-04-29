PRAGMA foreign_keys = ON;

CREATE TABLE teacher(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULL
);


CREATE TABLE class(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR(255) NOT NULL,
teacher_id INTEGER NOT NULL, 
FOREIGN KEY (teacher_id) REFERENCES teacher(id),
UNIQUE(name)
);


CREATE TABLE course(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
title VARCHAR(255) NOT NULL,
UNIQUE(title)
);


CREATE TABLE student(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULL,
class_id INTEGER NOT NULL,
pcourse_id INTEGER NOT NULL,
FOREIGN KEY (class_id) REFERENCES class(id),
FOREIGN KEY (pcourse_id) REFERENCES course(id)
);


CREATE TABLE pair(
student_id INTEGER NOT NULL,
partner_id INTEGER NOT NULL,
preference_rank INTEGER NOT NULL,
PRIMARY KEY (student_id, partner_id),
FOREIGN KEY(student_id) REFERENCES student(id),
FOREIGN KEY(partner_id) REFERENCES student(id)
);


INSERT INTO teacher VALUES (1, 'Anderson', 'Barber');
INSERT INTO teacher VALUES (2, 'Jade', 'Clark');
INSERT INTO teacher VALUES (3, 'Nicholas', 'Brown');
INSERT INTO teacher VALUES (4, 'Ellen', 'Smith');
INSERT INTO teacher VALUES (5, 'David', 'Cole');


INSERT INTO class VALUES (1, '1A', 1);
INSERT INTO class VALUES (2, '1B', 4);
INSERT INTO class VALUES (3, '1C', 3);


INSERT INTO course VALUES (1, 'Math');
INSERT INTO course VALUES (2, 'Language');
INSERT INTO course VALUES (3, 'Science');
INSERT INTO course VALUES (4, 'Art');
INSERT INTO course VALUES (5, 'Gym');


INSERT INTO student VALUES (1, 'Sara', 'Rusolli', 1, 1);
INSERT INTO student VALUES (2, 'Elian', 'Ryan', 1, 2);
INSERT INTO student VALUES (3, 'Sara', 'Reneth', 1, 3);
INSERT INTO student VALUES (4, 'Sara', 'Ruso', 1, 4);
INSERT INTO student VALUES (5, 'Shakhlo', 'Rustam', 1, 4);
INSERT INTO student VALUES (6, 'Gani', 'Ahmad', 1, 3);
INSERT INTO student VALUES (7, 'Seva', 'Nur', 1, 1);
INSERT INTO student VALUES (8, 'Sevinch', 'Ali', 1, 4);
INSERT INTO student VALUES (9, 'Tursun', 'Ayatilla', 1, 2);
INSERT INTO student VALUES (10, 'Husni', 'Munavvar', 1, 1);


INSERT INTO student VALUES (11, 'Ingrid', 'Johannessen', 2, 1);
INSERT INTO student VALUES (12, 'Olav', 'Eriksen', 2, 2);
INSERT INTO student VALUES (13, 'Runar', 'Kirke', 2, 3);
INSERT INTO student VALUES (14, 'Hinata', 'Naruto', 2, 4);
INSERT INTO student VALUES (15, 'Himari', 'Hoshiko', 2, 4);
INSERT INTO student VALUES (16, 'Doroteya', 'Dmitri', 2,5);
INSERT INTO student VALUES (17, 'Zasha', 'Olezka',2, 2);
INSERT INTO student VALUES (18, 'Maryam', 'Ahmed', 2, 1);
INSERT INTO student VALUES (19, 'Sofia', 'Jabir', 2, 1);
INSERT INTO student VALUES (20, 'Kristina ', 'Joranger', 2, 1);


INSERT INTO student VALUES (21, 'Kari', 'Aagard', 3, 1);
INSERT INTO student VALUES (22, 'Anna', 'Frozen', 3, 2);
INSERT INTO student VALUES (23, 'Baker', 'Hansen', 3, 3);
INSERT INTO student VALUES (24, 'Lars', 'Joakim', 3, 4);
INSERT INTO student VALUES (25, 'Agatha', 'Bjork', 3, 4);
INSERT INTO student VALUES (26, 'Amida', 'Akito', 3,3);
INSERT INTO student VALUES (27, 'Sakura', 'Goku',3, 2);
INSERT INTO student VALUES (28, 'Nydalen', 'Gata', 3, 1);
INSERT INTO student VALUES (29, 'Sofia', 'Jabir', 3, 1);
INSERT INTO student VALUES (30, 'Kakashi ', 'Levi', 3, 1);


INSERT INTO pair VALUES (1, 21, 1);
INSERT INTO pair VALUES (1, 16, 2);
INSERT INTO pair VALUES (1, 11, 3);
INSERT INTO pair VALUES (2, 22, 1);
INSERT INTO pair VALUES (2, 27, 2);
INSERT INTO pair VALUES (2, 28, 3);
INSERT INTO pair VALUES (3, 15, 1);
INSERT INTO pair VALUES (3, 11, 2);
INSERT INTO pair VALUES (3, 6, 3);




