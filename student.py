# Student Management System
"""

Use best practice to create a multilayers, scalable console application to manage ( Add, Delete,
Update, Search ) for students, Student has properties (Firstname, Lastname, DOB, Address, Phone,
Age, Gender).
The application will store students info into text file, and provide an interface to manage the DB, and
search by Firstname, Gender, and Age (Older than entered value)


Fields :- ['Firstname', 'Lastname', 'DOB', 'Address', 'Phone', 'Age', 'Gender']
1. Add new
2. Delete
3. Update
4. Search (by Firstname, Gender, and Age (Older than entered value))
"""

import csv
import datetime
from datetime import date

# Define global variables
student_fields = ['Firstname', 'Lastname', 'Address', 'Phone', 'Gender', 'DOB (dd-mm-yyyy)', 'Age']
student_database = 'students.csv'


def display_menu():
    print("--------------------------------------")
    print(" Welcome to Student Management System")
    print("---------------------------------------")
    print("1. Add new student")
    print("2. View all students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")

def view_students():
    global student_fields
    global student_database

    print("--- Student Records ---")

    with open(student_database, "r", encoding="utf-8") as f:
        index = 0
        reader = csv.reader(f)
        print("Index", end='\t |')
        for x in student_fields:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            index += 1
            print(index, end="\t |")
            for item in row:
                print(item, end="\t |")
            print("\n")

def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = validate_input(field)
        student_data.append(value)
        if(field == 'DOB (dd-mm-yyyy)'):
            student_data.append(calculate_age(datetime.datetime.strptime(value, '%d-%m-%Y')))
            break


    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    return

def search_student():
    global student_fields
    global student_database

    print("--- Search Student ---")
    Firstname = input("Enter Firstname to search (or '-' to skip): ")
    Gender = input("Enter Gender to search (or '-' to skip): ")
    Age = input("Enter Age to search older than entered value (or '-' to skip): ")

    with open(student_database, "r", encoding="utf-8") as f:
        Index = 0
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                Index += 1
                #['Firstname', 'Lastname', 'DOB', 'Address', 'Phone', 'Age', 'Gender']
                #if (Firstname in row[0] and Gender == row[6] and Age < row[5]):
                if ((Firstname == row[0] or Firstname == '-') and (Gender == row[6] or Gender == '-') and (Age < row[5] or Age == '-')):
                    print("----- Student Found -----")
                    print("Index: ", Index)
                    print("Firstname: ", row[0])
                    print("Lastname: ", row[1])
                    print("Address: ", row[2])
                    print("Phone: ", row[3])
                    print("Gender: ", row[4])
                    print("DOB: ", row[5])
                    print("Age: ", row[6])
        else:
            print("Result not found")


def update_student():
    global student_fields
    global student_database

    view_students()
    print("--- Update Student ---")
    Index = input("Enter Index to update: ")
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        Count = 0
        for row in reader:
            Count += 1
            if str(Count) == Index:
                print("Student Found: at index ",Index)
                student_data = []
                for field in student_fields:
                    value = validate_input(field)
                    student_data.append(value)
                    if(field == 'DOB (dd-mm-yyyy)'):
                        student_data.append(calculate_age(datetime.datetime.strptime(value, '%d-%m-%Y')))
                        break
                updated_data.append(student_data)
            else:
                updated_data.append(row)


    # Check if the record is found or not
    if Count >0:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Data not found in our database")



def delete_student():
    global student_fields
    global student_database

    view_students()
    print("--- Delete Student ---")
    Index = input("Enter Index to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        Count = 0
        for row in reader:
            Count += 1
            if str(Count) == Index:
                student_found = True
            else:
                updated_data.append(row)                

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Index ", Index, "deleted successfully")
    else:
        print("Index not found in our database")

def validate_input(field="", text = ""):
    display = ("Enter " + field + ": ", text)[len(text) > 0]


    if(field == 'Firstname' or field == 'Lastname'):
        value = input(display)
        if not value.isalpha():
            print ("--> Invalid " + field)
            return validate_input(field)
        else:
            return value
    elif(field == 'DOB (dd-mm-yyyy)'):
        value = input(display)
        try:
            data = datetime.datetime.strptime(value, '%d-%m-%Y')
        except:
            print ("--> Invalid " + field)
            return validate_input(field)
        return value;
    elif(field == 'Age'):
        value = input(display)
        if not value.isnumeric():
            print ("--> Invalid " + field)
            return validate_input(field)
        else:
            return value
    else:
        value = input(display)
        return value

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))



while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
        input("--- Press enter to continue ---")
    elif choice == '2':
        view_students()
        input("--- Press enter to continue ---")
    elif choice == '3':
        search_student()
        input("--- Press enter to continue ---")
    elif choice == '4':
        update_student()
        input("--- Press enter to continue ---")
    elif choice == '5':
        delete_student()
        input("--- Press enter to continue ---")
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")