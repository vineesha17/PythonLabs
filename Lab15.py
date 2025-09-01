import sqlite3

# Connect to database
conn = sqlite3.connect("student_record.db")
cursor = conn.cursor()

# Create student table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        Enrollment INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Create student_subject table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_subject (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Enrollment INTEGER,
        Subject TEXT NOT NULL,
        Mark INTEGER NOT NULL,
        FOREIGN KEY (Enrollment) REFERENCES student(Enrollment)
    )
''')


def add_student():
    enrollment = int(input("Enter Enrollment No: "))
    name = input("Enter Student Name: ")
    try:
        cursor.execute("INSERT INTO student (Enrollment, name) VALUES (?, ?)", (enrollment, name))
        conn.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("Enrollment already exists!")


def enroll_subjects():
    enrollment = int(input("Enter Enrollment No: "))
    n = int(input("How many subjects to enroll? "))
    for _ in range(n):
        subject = input("Enter Subject: ")
        mark = int(input(f"Enter marks for {subject}: "))
        cursor.execute("INSERT INTO student_subject (Enrollment, Subject, Mark) VALUES (?, ?, ?)",
                       (enrollment, subject, mark))
    conn.commit()
    print("Subjects added successfully!")


def view_all():
    cursor.execute('''
        SELECT student.Enrollment, student.name, student_subject.Subject, student_subject.Mark
        FROM student
        JOIN student_subject ON student.Enrollment = student_subject.Enrollment
    ''')
    records = cursor.fetchall()
    print("\nAll Student Records with Subjects:")
    for row in records:
        print(row)


def update_marks():
    enrollment = int(input("Enter Enrollment No: "))
    subject = input("Enter Subject: ")
    new_mark = int(input("Enter new mark: "))
    cursor.execute('''
        UPDATE student_subject
        SET Mark = ?
        WHERE Enrollment = ? AND Subject = ?
    ''', (new_mark, enrollment, subject))
    conn.commit()
    print("Mark updated successfully!")


def delete_subject():
    enrollment = int(input("Enter Enrollment No: "))
    subject = input("Enter Subject to delete: ")
    cursor.execute("DELETE FROM student_subject WHERE Enrollment = ? AND Subject = ?", (enrollment, subject))
    conn.commit()
    print("Subject deleted successfully!")


def high_scorers():
    cursor.execute('''
        SELECT student.name, student_subject.Subject, student_subject.Mark
        FROM student
        JOIN student_subject ON student.Enrollment = student_subject.Enrollment
        WHERE student_subject.Mark > 90
    ''')
    high_scores = cursor.fetchall()
    print("\nStudents with Marks > 90:")
    for record in high_scores:
        print(record)


def average_marks():
    cursor.execute("SELECT AVG(Mark) FROM student_subject")
    avg = cursor.fetchone()[0]
    print(f"\nAverage mark across all subjects: {avg:.2f}")


# ----------------- MENU -----------------
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Enroll Student in Multiple Subjects")
    print("3. View All Records")
    print("4. Update Marks")
    print("5. Delete Subject Record")
    print("6. Show High Scorers (>90)")
    print("7. Show Average Marks")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        enroll_subjects()
    elif choice == "3":
        view_all()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_subject()
    elif choice == "6":
        high_scorers()
    elif choice == "7":
        average_marks()
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")


conn.close()
