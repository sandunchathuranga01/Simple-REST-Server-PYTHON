from flask import Flask, request, jsonify
from datetime import datetime
from db_utils import create_db_connection
from mysql.connector import Error

app = Flask(__name__)


# Root route to handle the base URL
@app.route('/')
def home():
    return "Welcome to the Student Management API"


# Favicon route to avoid 404 error
@app.route('/favicon.ico')
def favicon():
    return '', 204


@app.route('/addStudent/', methods=['POST'])
def add_student():
    if request.method == 'POST':
        msg = None
        try:
            post_data = request.get_json()
            name = post_data['name']
            age = post_data['age']
            reg_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            conn = create_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO students (name, age, reg_date) VALUES (%s, %s, %s)", (name, age, reg_date))
                conn.commit()
                msg = "Student added successfully"
                conn.close()
            else:
                msg = "Failed to connect to the database"
        except Error as e:
            msg = f"Error occurred: {str(e)}"
        return jsonify(msg=msg)


@app.route('/getAllStudent_Details/', methods=['GET'])
def get_all_students():
    try:
        conn = create_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()
            conn.close()
            return jsonify(students=students)
        else:
            return jsonify(msg="Failed to connect to the database")
    except Error as e:
        return jsonify(msg=f"Error occurred: {str(e)}")


@app.route('/updateStudent/<int:id>/', methods=['PUT'])
def update_student(id):
    if request.method == 'PUT':
        msg = None
        try:
            post_data = request.get_json()
            name = post_data['name']
            age = post_data['age']

            conn = create_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE students SET name=%s, age=%s WHERE id=%s", (name, age, id))
                conn.commit()
                msg = "Student updated successfully"
                conn.close()
            else:
                msg = "Failed to connect to the database"
        except Error as e:
            msg = f"Error occurred: {str(e)}"
        return jsonify(msg=msg)


@app.route('/deleteStudent/<int:id>/', methods=['DELETE'])
def delete_student(id):
    if request.method == 'DELETE':
        msg = None
        try:
            conn = create_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM students WHERE id=%s", (id,))
                conn.commit()
                msg = "Student deleted successfully"
                conn.close()
            else:
                msg = "Failed to connect to the database"
        except Error as e:
            msg = f"Error occurred: {str(e)}"
        return jsonify(msg=msg)


if __name__ == '__main__':
    app.run(debug=True)
