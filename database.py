import sqlite3

DB_NAME = "appointments.db"

def create_table():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("""
                   CREATE TABLE IF NOT EXISTS appointments(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       mobile TEXT NOT NULL,
                       service TEXT NOT NULL,
                       time TEXT NOT NULL
                   )
                   """)


def insert_appointment(name, mobile, service, time):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("""
                   INSERT INTO appointments(name, mobile, service, time)
                   VALUES (?, ?, ?, ?)
                   """,
                   (name, mobile, service, time)
                   )



def get_all_appointments():
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM appointments")
        return cursor.fetchall()


def get_appointment_by_id(appointment_id):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT *FROM appointments WHERE id = ?", (appointment_id,))
        return cursor.fetchone()


def search_appointments(keyword):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT *FROM appointments WHERE name LIKE ?", (f"%{keyword}%",))
        return cursor.fetchall()


def delete_appointment(appointment_id):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM appointments WHERE id= ?", (appointment_id,))
        return cursor.rowcount


def update_appointment(appointment_id, name,mobile,service,time):
    with sqlite3.connect(DB_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE appointments
            SET
                name = ?,
                mobile = ?,
                service = ?,
                time = ?
            WHERE id = ?
            """,(name,mobile,service,time,appointment_id))
        return cursor.rowcount