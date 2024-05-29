# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Bao Truong,5/28/2024, Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# This class handles printing: inputs, outputs, and error messages
class IO:
    
    # Function that prints out errors
    @staticmethod
    def output_error_messages(message: str, e: Exception = None):
        print(message)
        print(e.__doc__)
        print(e.__str__())

    # Function that prints out the menu text
    @staticmethod
    def output_menu(menu: str):
        print(menu, "\n")

    # Function that takes in user input for menu choice.
    @staticmethod
    def input_menu_choice():
        try:
            menu_choice = input("Select a menu option: \n")
            if menu_choice not in ("1", "2", "3", "4"):
                raise Exception("Please enter 1, 2, 3 or 4.")
        except Exception as e:
            IO.output_error_messages("-Technical Error-", e)
        return menu_choice


    # Function that prints out student data
    @staticmethod
    def output_student_courses(students: list):
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        
    # Function that takes in user input for Student data
    @staticmethod
    def input_student_data(students: list):
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("-Technical Error-", e)
        except Exception as e:
           IO.output_error_messages("-Technical Error-", e)
        return students



# This class handles reading and writing to json files.
class FileProcessor:

    # Function for reading from json file
    @staticmethod
    def read_data_from_file(file_name: str, students: list):
        try:
            with(file_name, "r") as file:
                students = json.load(file)
        except FileNotFoundError as e:
            IO.output_error_messages("-Technical Error-", e)
        except Exception as e:
            IO.output_error_messages("-Technical Error-", e)
        return students

    # Function for writing data to json file
    @staticmethod
    def write_data_to_file(file_name: str, students: list):
        try:
            with open(file_name, "w") as file:
                json.dump(students, file)
            for student in students:
                print(f'Student {student["FirstName"]} '
                f'{student["LastName"]} is enrolled in {student["CourseName"]}')   
        except Exception as e:
            IO.output_error_messages("-Technical Error-", e)

# Main Program Routine
if __name__ == "__main__":
    students = FileProcessor.read_data_from_file(FILE_NAME, students)
    
    while (True):
        IO.output_menu(MENU)
        menu_choice = IO.input_menu_choice()
        if menu_choice == "1":
            IO.input_student_data(students)

        elif menu_choice == "2":
            IO.output_student_courses(students)

        elif menu_choice == "3":
            FileProcessor.write_data_to_file(FILE_NAME, students)

        elif menu_choice == "4":
            print("Program Ended")
            break
    
