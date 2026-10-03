import csv
while True:
    print("\n1. Enter Student Data")
    print("2. Calculate Results and Grades")
    print("3. View Class Summary Report")
    print("4. Exit")

    choice = input("Apna option select karein (1/2/3/4): ")

    if choice == "1":
        students_data = [["Name", "Math", "Science", "English"]]
        while True:
            name = input("Enter student name (or type 'done' to finish): ")
            if name.lower() == "done":
                break
            math = input(f"Enter {name}'s Math marks: ")
            science = input(f"Enter {name}'s Science marks: ")
            english = input(f"Enter {name}'s English marks: ")
            students_data.append([name, math, science, english])

        with open("students.csv", "w", newline="") as f:
            csv.writer(f).writerows(students_data)
        print("Student data saved to students.csv.")

    elif choice == "2":
        # Code for calculating results and grades goes here
        pass

    elif choice == "3":
        # Code for viewing class summary report goes here
        pass

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid option selected! Please 1, 2, 3, or 4 enter karein.")
students_data = [
    ["Name", "Math", "Science", "English"],
    ["Ali", 88, 92, 85],
    ["Sara", 72, 68, 75],
    ["Usman", 95, 98, 91],
    ["Ayesha", 64, 70, 68],
    ["Zain", 45, 50, 52],
    ["Fatima", 92, 88, 95],
    ["Hamza", 78, 82, 74],
    ["Hira", 55, 60, 58],
    ["Bilal", 84, 79, 88],
    ["Sana", 91, 94, 90]
]

with open("students.csv", "w", newline="") as f:
    csv.writer(f).writerows(students_data)

results = [["Name", "Math", "Science", "English", "Average", "Grade"]]
total_marks = 0
top_name = ""
top_avg = 0

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name = row[0]
        m, s, e = float(row[1]), float(row[2]), float(row[3])
        avg = round((m + s + e) / 3, 2)
        
        if avg >= 85: grade = "A"
        elif avg >= 70: grade = "B"
        elif avg >= 50: grade = "C"
        else: grade = "F"
        
        results.append([name, m, s, e, avg, grade])
        total_marks += avg
        
        if avg > top_avg:
            top_avg = avg
            top_name = name

with open("student_results.csv", "w", newline="") as f:
    csv.writer(f).writerows(results)

class_avg = round(total_marks / (len(results) - 1), 2)

with open("summary.txt", "w") as f:
    f.write(f"==============================\n    CLASS SUMMARY REPORT      \n==============================\n")
    f.write(f"Class Average : {class_avg}\nTop Student   : {top_name} ({top_avg})\n")

print("\nData processing complete! Aap kya dekhna chahte hain?")
print("1. Original Students Data (students.csv)\n2. Calculated Results and Grades (student_results.csv)\n3. Class Summary Report (summary.txt)")

choice = input("Apna option select karein (1/2/3): ")

if choice == "1":
    with open("students.csv", "r") as f:
        for row in csv.reader(f): print(row)
elif choice == "2":
    with open("student_results.csv", "r") as f:
        for row in csv.reader(f): print(row)
elif choice == "3":
    with open("summary.txt", "r") as f:
        print(f.read())
else:
    print("Invalid option selected! Please 1, 2, ya 3 enter karein.")