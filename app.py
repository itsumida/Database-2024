from flask import Flask, g, render_template
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
    

@app.route("/questionnaire/page")
def questionnaire():
    return f"Not implemented"

@app.route("/summary/page")
def summary():
    return f"Not implemented"



