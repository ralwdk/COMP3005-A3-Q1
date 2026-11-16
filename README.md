COMP3005 Assignment 3 - Question 1



Overview



A Python program that connects to a PostgreSQL database and lets me view, add, update, and delete student records. It uses Psycopg 3.



Requirements

* Python 3
* PostgreSQL
* SSH access if connecting to a remote server



Install the Python packages from the project folder:

```powershell
python -m pip install -r requirements.txt
```



Database Setup

1. Create a database called `assignment3\_students` in PostgreSQL.
2. Open that database in pgAdmin's Query Tool.
3. Run `database.sql` once to create the `students` table and insert the three starting records.



Running the Program

The program uses connection settings from environment variables. By default, it connects to `127.0.0.1` on port `5433` through an SSH tunnel.



For a local PostgreSQL installation, open PowerShell in the project folder and run:

```powershell
$env:PGHOST = "127.0.0.1"
$env:PGPORT = "5432"
$env:PGDATABASE = "assignment3\_students"
$env:PGUSER = "postgres"
python app.py
```



Change the username or port if your PostgreSQL setup is different. The program asks for your PostgreSQL password when it starts.

For a remote server, first open an SSH tunnel in a separate terminal:

```powershell
ssh -L 5433:127.0.0.1:5432 student@YOUR\_VM\_IP
```



Replace `YOUR\_VM\_IP` with the server address and leave the tunnel open. In a new PowerShell window, use the default connection settings (or set `PGHOST`, `PGPORT`, `PGDATABASE`, and `PGUSER` to match the tunnel), then run:

```powershell
python app.py
```



The program displays the students, adds a test student, updates that student's email, and deletes the test student. It prints the records after each step.



Video Demonstration

Video link: \[https://youtu.be/Hs1cLS2ahnc]

The video shows the database setup and all four functions, including the changes in pgAdmin.



