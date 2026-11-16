import os
from getpass import getpass
import psycopg


# Connect to PostgreSQL using configurable connection settings.
# Defaults use the SSH tunnel for the OpenStack VM.
# Other users can override these settings with environment variables.
def connect():
    password = os.environ.get("PGPASSWORD") or getpass("PostgreSQL password: ")

    return psycopg.connect(
        host=os.environ.get("PGHOST", "127.0.0.1"),
        port=int(os.environ.get("PGPORT", "5433")),
        dbname=os.environ.get("PGDATABASE", "assignment3_students"),
        user=os.environ.get("PGUSER", "postgres"),
        password=password
    )


# Fetch and print all students
def getAllStudents(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students ORDER BY student_id;")
        for row in cur.fetchall():
            print(row)


# Insert a new student and return their ID
def addStudent(conn, first_name, last_name, email, enrollment_date):
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s)
            RETURNING student_id;
            """,
            (first_name, last_name, email, enrollment_date)
        )
        new_id = cur.fetchone()[0]
    conn.commit()
    print(f"Added student (ID: {new_id})")
    return new_id


# Update a student's email by ID
def updateStudentEmail(conn, student_id, new_email):
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE students SET email = %s WHERE student_id = %s;",
            (new_email, student_id)
        )
        rows_affected = cur.rowcount
    conn.commit()
    print(f"Updated {rows_affected} row(s)")


# Delete a student by ID
def deleteStudent(conn, student_id):
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM students WHERE student_id = %s;",
            (student_id,)
        )
        rows_affected = cur.rowcount
    conn.commit()
    print(f"Deleted {rows_affected} row(s)")


def main():
    try:
        with connect() as conn:
            print("--- Initial students ---")
            getAllStudents(conn)

            print("\n--- Adding student ---")
            new_id = addStudent(conn, "Maya", "Patel", "maya.patel@gmail.com", "2023-09-03")
            getAllStudents(conn)

            print("\n--- Updating email ---")
            updateStudentEmail(conn, new_id, "mpatel99@gmail.com")
            getAllStudents(conn)

            print("\n--- Deleting student ---")
            deleteStudent(conn, new_id)
            getAllStudents(conn)

    except psycopg.Error as e:
        print(f"Database error: {e}")


if __name__ == "__main__":
    main()