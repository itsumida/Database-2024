@app.route("/summary/page")
def summary():
    cursor = get_db().cursor()
    
    cursor.execute("""
        SELECT s1.first_name AS student_first_name, 
               s1.last_name AS student_last_name, 
               s2.first_name AS partner_first_name, 
               s2.last_name AS partner_last_name, 
               c.title AS course_title
        FROM pair p
        JOIN student s1 ON p.student_id = s1.id
        JOIN student s2 ON p.partner_id = s2.id
        JOIN course c ON s1.course_id = c.id
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
        SELECT c.title
        FROM course c
        JOIN student s ON c.id = s.course_id
        GROUP BY c.title
        ORDER BY COUNT(*) DESC
    """)
    popular_courses = cursor.fetchall()

    return render_template("summary.html", pairs=pairs, popular_students=popular_students, popular_courses=popular_courses)

if __name__ == "__main__":
    app.run(debug=True)
