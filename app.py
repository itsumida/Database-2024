from flask import Flask, abort, g, redirect, render_template, request, url_for
import sqlite3

DATABASE = "database.db"

app = Flask(__name__)

students1 = []

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys=ON")
    return g.db 

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/students/<int:student_id>")
def student(student_id):
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM student WHERE id =?", [id])
    student = cursor.fetchone()
    if not student:
        abort(404)
    
@app.route("/questionnaire/page", methods = ["GET", "POST"])
def questionnaire():
    cursor = get_db().cursor()
    if request.method == "POST":
        try:
            form = request.form
            id = int(form.get("student_id"))  
            cursor.execute("BEGIN")
            cursor.execute("""
                 SELECT id
                 FROM student
                 WHERE id =?
                 LIMIT 1
             """, [id]) #have no idea what this code is about but needed it for the "already answered" file to appear
            if cursor.fetchone():
                cursor.execute("COMMIT")
                return render_template("questionnaire_already_answered.html")
        except (TypeError, ValueError, sqlite3.DatabaseError):
            abort(400)
        

         
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    teachers = cursor.execute("SELECT * FROM teacher")
    teachers = cursor.fetchall()
    courses = cursor.execute("SELECT * FROM course")
    courses = cursor.fetchall()
    return render_template("questionnaire.html", students = students, teachers = teachers, courses = courses)

@app.route("/summary/page")
def summary():
    cursor = get_db().cursor()
    cursor.execute("""
        SELECT A.id AS student_id_1, A.first_name AS student_first_name_1, A.last_name AS student_last_name_1, 
            C1.title AS student_pcourse_title_1,
            B.id AS student_id_2, B.first_name AS student_first_name_2, B.last_name AS student_last_name_2, 
            C2.title AS student_pcourse_title_2
        FROM pair p1
        JOIN pair p2 ON p1.student_id = p2.partner_id AND p1.partner_id = p2.student_id AND p1.student_id < p2.student_id
        JOIN student A ON p1.student_id = A.id
        JOIN student B ON p2.student_id = B.id
        JOIN course C1 ON A.pcourse_id = C1.id
        JOIN course C2 ON B.pcourse_id = C2.id;




        

        
        

    """)
    pairs = cursor.fetchall()
    popular_students = {}
    cursor.execute("SELECT DISTINCT class_id FROM student")
    class_ids = cursor.fetchall()
    for class_id in class_ids:
         cursor.execute("""
             SELECT s.first_name, s.last_name
             FROM student s
             WHERE s.class_id = ?
             ORDER BY (
                 SELECT COUNT(*)
                 FROM pair p
                 WHERE p.student_id = s.id
             ) DESC
             LIMIT 3
         """, (class_id['class_id'],))
         popular_students[class_id['class_id']] = cursor.fetchall()

    cursor.execute("""
         SELECT c.title, student.pcourse_id
         FROM course c, student
         JOIN student s ON c.id = student.pcourse_id
         GROUP BY c.title
         ORDER BY COUNT(*) DESC
     """)
    popular_courses = cursor.fetchall()

    return render_template("summary.html", pairs=pairs, popular_students=popular_students, popular_courses=popular_courses)

if __name__ == "__main__":
    app.run(debug=True)
  
            


    



    
# summary for app.py Zara version
# @app.route("/summary/page")
# def summary():
#     cursor = get_db().cursor()
    
#     cursor.execute("""
#         SELECT student.first_name AS student_first_name, 
#                student.last_name AS student_last_name, 
#                student.first_name AS partner_first_name, 
#                student.last_name AS partner_last_name, 
#                course.title AS course_title
#         FROM pair p, student, course
#         JOIN student s1 ON p.student_id = s1.id
#         JOIN student s2 ON p.partner_id = s2.id
#         JOIN course c ON student.pcourse_id = c.id
#     """)
#     pairs = cursor.fetchall()

#     popular_students = {}
#     cursor.execute("SELECT DISTINCT class_id FROM student")
#     class_ids = cursor.fetchall()
#     for class_id in class_ids:
#         cursor.execute("""
#             SELECT s.first_name, s.last_name
#             FROM student s
#             WHERE s.class_id = ?
#             ORDER BY (
#                 SELECT COUNT(*)
#                 FROM pair p
#                 WHERE p.student_id = s.id
#             ) DESC
#             LIMIT 3
#         """, (class_id['class_id'],))
#         popular_students[class_id['class_id']] = cursor.fetchall()

#     cursor.execute("""
#         SELECT c.title, student.pcourse_id
#         FROM course c, student
#         JOIN student s ON c.id = student.pcourse_id
#         GROUP BY c.title
#         ORDER BY COUNT(*) DESC
#     """)
#     popular_courses = cursor.fetchall()

#     return render_template("summary.html", pairs=pairs, popular_students=popular_students, popular_courses=popular_courses)

# if __name__ == "__main__":
#     app.run(debug=True)

#my prev code
# SELECT A.first_name, A.last_name, B.first_name, B.last_name
#         FROM student AS A
#         JOIN pair ON A.id = pair.partner_id
#         JOIN student AS B on B.id = pair.partner_id


# def questionnaire():
#     cursor = get_db().cursor()
#     if request.method == "POST":
#         form = request.form
#         id = int(form.get("student_id"))
#         teacher_id = int(form.get("teacher_id"))
#         pcourse_id = int(form.get("pcourse_id"))
#         partner1_id = int(form.get("partner1_id"))
#         partner2_id = int(form.get("partner2_id"))
#         partner3_id = int(form.get("partner3_id"))
#         try:
#             cursor = get_db().cursor()
#         cursor.execute("BEGIN")
#         cursor.execute("""
#                 SELECT id
#                 FROM student
#                 WHERE id =? AND pcourse_id =?
#                 LIMIT 1
#             """, [id, pcourse_id]) #have no idea what this code is about but needed it for the "already answered" file to appear
#             if cursor.fetchone():
#                 cursor.execute("COMMIT")
#                 return render_template("questionnaire_already_answered.html")
#         except (TypeError, ValueError, sqlite3.DatabaseError):
#             abort(400)

#         try:
#     cursor.execute("SELECT * FROM student")
#     students = cursor.fetchall()
#     teachers = cursor.execute("SELECT * FROM teacher")
#     teachers = cursor.fetchall()
#     courses = cursor.execute("SELECT * FROM course")
#     courses = cursor.fetchall()
#     return render_template("questionnaire.html", students = students, teachers = teachers, courses = courses)
# @app.route("/questionnaire/page", methods=['GET', 'POST'])

# def questionnaire():
#     cursor = get_db().cursor()
#     if request.method == "POST":
#         form = request.form
#         id = int(form.get("student_id"))
#         teacher_id = int(form.get("teacher_id"))
#         pcourse_id = form.get("pcourse_id")
#         partner1_id = (form.get("partner1_id"))
#         partner2_id = (form.get("partner2_id"))
#         partner3_id = (form.get("partner3_id"))
#         try:
#             cursor = get_db().cursor()
#             cursor.execute("BEGIN")
#             cursor.execute("""
#                 INSERT INTO student(id, pcourse_id)
#                 VALUES(?, ?) 
                
#             """, [id, pcourse_id]) #have no idea what this code is about but needed it for the "already answered" file to appear
#             student_id = cursor.fetchone()

#             cursor.execute("""
#                 INSERT INTO pair(student_id, partner_id, preference_rank)
#                 VALUES(student_id, partner1_id, 1, student_id, partner2_id, 2, student_id, partner3_id, 3))
#             """, [student_id, partner1_id, partner2_id, partner3_id])
#             cursor.execute("""INSERT INTO teacher(teacher_id) VALUES(?)""", [teacher_id])
#             cursor.execute()
#             if cursor.fetchone():
#                 cursor.execute("COMMIT")
#                 return render_template("questionnaire_already_answered.html")
#         except (TypeError, ValueError, sqlite3.DatabaseError):
#             abort(400)

        
#     cursor.execute("SELECT * FROM student")
#     students = cursor.fetchall()
#     teachers = cursor.execute("SELECT * FROM teacher")
#     teachers = cursor.fetchall()
#     courses = cursor.execute("SELECT * FROM course")
#     courses = cursor.fetchall()
#     return render_template("questionnaire.html", students = students, teachers = teachers, courses = courses)
