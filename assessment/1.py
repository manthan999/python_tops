import datetime

students = {}   
attendance_records = {}  

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_student():
    roll = input("Enter roll number: ").strip()
    if roll in students:
        print("Roll number already exists!")
        return
    name = input("Enter student name: ").strip()
    course = input("Enter course: ").strip()
    students[roll] = {'name': name, 'course': course}
    print(f"Student {name} added.")

def mark_attendance():
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    if not validate_date(date_str):
        print("Invalid date format!")
        return
    if date_str in attendance_records:
        print("Attendance for this date already recorded!")
        return

    attendance_records[date_str] = {}
    print("Marking attendance for date:", date_str)
    for roll, info in students.items():
        ans = input(f"Is {info['name']} (roll {roll}) present? (y/n): ").strip().lower()
        present = (ans == 'y')
        attendance_records[date_str][roll] = present
    print("Attendance marked for", date_str)

def generate_report_student():
    roll = input("Enter roll number for report: ").strip()
    if roll not in students:
        print("No student with that roll number!")
        return
    total_days = 0
    days_present = 0
    for date, rec in attendance_records.items():
        if roll in rec:
            total_days += 1
            if rec[roll]:
                days_present += 1
    if total_days == 0:
        print("No attendance records for this student.")
        return
    days_absent = total_days - days_present
    pct = (days_present / total_days) * 100
    status = "Defaulter" if pct < 75 else "OK"
    info = students[roll]
    print(f"Report for {info['name']} (roll {roll}, course {info['course']})")
    print(f"Total days: {total_days}")
    print(f"Days present: {days_present}")
    print(f"Days absent: {days_absent}")
    print(f"Attendance %: {pct:.2f}")
    print(f"Status: {status}")

def generate_report_class():
    print("Class Report")
    print("{:<10} {:<15} {:<10} {:<12} {:<12} {:<10} {:<10}".format(
        "Roll", "Name", "Course", "DaysPresent", "DaysAbsent", "%Att", "Status"))
    for roll, info in students.items():
        total_days = 0
        days_present = 0
        for date, rec in attendance_records.items():
            if roll in rec:
                total_days += 1
                if rec[roll]:
                    days_present += 1
        if total_days == 0:
            pct = 0.0
        else:
            pct = (days_present / total_days) * 100
        days_absent = total_days - days_present
        status = "Defaulter" if pct < 75 else "OK"
        print("{:<10} {:<15} {:<10} {:<12} {:<12} {:<10.2f} {:<10}".format(
            roll, info['name'], info['course'], days_present, days_absent, pct, status))

def menu():
    while True:
        print("\nMenu:")
        print("1. Add student")
        print("2. Mark attendance")
        print("3. Student report")
        print("4. Class report")
        print("5. Exit")
        choice = input("Enter choice (1-5): ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            mark_attendance()
        elif choice == '3':
            generate_report_student()
        elif choice == '4':
            generate_report_class()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    print("Welcome to EduTrack Attendance System")
    menu()