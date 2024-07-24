from db_utils import create_db_connection

def create_student_table():
    connection = create_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT NOT NULL,
                reg_date DATETIME NOT NULL
            );
        ''')
        connection.commit()
        connection.close()

create_student_table()
