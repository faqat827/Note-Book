import csv

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
    writer = csv.writer(f)
    writer.writerows(students_data)

results = []
total_class_marks = 0
top_student_name = ""
top_student_avg = 0

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        name = row["Name"]
        math = float(row["Math"])
        science = float(row["Science"])
        english = float(row["English"])
        
        average = round((math + science + english) / 3, 2)
        
        if average >= 85:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "F"
            
        results.append({
            "Name": name,
            "Math": math,
            "Science": science,
            "English": english,
            "Average": average,
            "Grade": grade
        })
        
        total_class_marks += average
        if average > top_student_avg:
            top_student_avg = average
            top_student_name = name

with open("student_results.csv", "w", newline="") as f:
    fields = ["Name", "Math", "Science", "English", "Average", "Grade"]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(results)

class_average = round(total_class_marks / len(results), 2)

with open("summary.txt", "w") as f:
    f.write("==============================\n")
    f.write("    CLASS SUMMARY REPORT      \n")
    f.write("==============================\n")
    f.write(f"Class Average : {class_average}\n")
    f.write(f"Top Student   : {top_student_name} ({top_student_avg})\n")

# --- USER SELECTION MENU ---
print("\nData processing complete! Aap kya dekhna chahte hain?")
print("1. Original Students Data (students.csv)")
print("2. Calculated Results and Grades (student_results.csv)")
print("3. Class Summary Report (summary.txt)")

choice = input("Apna option select karein (1/2/3): ")

if choice == "1":
    print("\n--- Original Students Data ---")
    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

elif choice == "2":
    print("\n--- Student Results & Grades ---")
    with open("student_results.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(dict(row))

elif choice == "3":
    print("\n--- Class Summary Report ---")
    with open("summary.txt", "r") as f:
        print(f.read())

else:
    print("Invalid option selected! Please 1, 2, ya 3 enter karein.")