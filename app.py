from flask import Flask, abort, g, redirect, render_template, request, url_for
import sqlite3

DATABASE = "database.db"

app = Flask(__name__)

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
    

@app.route("/questionnaire/page", methods=['GET', 'POST'])

def questionnaire():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    teachers = cursor.execute("SELECT * FROM teacher")
    teachers = cursor.fetchall()
    courses = cursor.execute("SELECT * FROM course")
    courses = cursor.fetchall()
    return render_template("questionnaire.html", students = students, teachers = teachers, courses = courses)

            
    


    

@app.route("/summary/page")
def summary():
    return f"Not implemented"








