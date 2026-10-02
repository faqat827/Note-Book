import csv

with open("contacts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "phone", "city"])
    writer.writerow(["Ali Khan", "03001234567", "Lahore"])
    writer.writerow(["Sara Ahmed", "03119876543", "Karachi"])
    writer.writerow(["Usman Malik", "03215554433", "Lahore"])
    writer.writerow(["Ayesha Bibi", "03337778899", "Islamabad"])
    writer.writerow(["Zain Raza", "03451112233", "Karachi"])

print("contacts.csv file ban gayi hai!\n")

target_city = input("Enter city name: ")

print(f"\n--- Contacts in {target_city} ---")

with open("contacts.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name = row[0]
        phone = row[1]
        city = row[2]
        if city.lower() == target_city.lower():
            print(f"Name: {name} | Phone: {phone}")