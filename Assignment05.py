# ------------------------------------------------------------------------------------------ #
# Title: Assignment 05
# Desc: Course Registration Script Using Error Handling and Dictionaries
# Change Log: (Who, When, What)
#   <WBuendia>,<19 May 2025>,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Program's Constants
FILE_NAME: str = 'Enrollments.json'
MENU: str = '''
---------- Course Registration Program -----------
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
'''

# Define the Program's Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
file: None
menu_choice: str = ""
student_data: dict = {}
students: list[dict[str, str | float]] = []

# File is Read into a List of Dictionary Rows + Error Handling
try:

    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

# Main Loop
while True:

    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()

    # Adding Data to the Table + Error Handling
    if menu_choice == "1":
        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("What is the course name? ")
            if not course_name:
                raise ValueError("Course name cannot be empty.")

            # Save the data to the file
            student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "Course": course_name}
            students.append(student_data)
            print(f"Student {student_first_name} {student_last_name} has registered for {course_name}")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

    # Display the Tables Current Data
    elif menu_choice == "2":
        # Show current data
        if not students:
            print("No registrations to display.")
        else:
            print("\nCurrent Student Registrations:")
            for row in students:
                print(f"{row['FirstName']}, {row['LastName']}, {row['Course']}")
            print()

    # Dictionary Rows are Saved to a .json File + Error Handling
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            continue
        except TypeError as e:
            print("Please ensure that the data is in a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

    # Exit the Loop and End the Program
    elif menu_choice == "4":
        break
    else:
        print("Please enter a numerical value between 1-4. . . .")