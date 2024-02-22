# -------------------------------------------------------------------------------------------------------------------- #
# Tite: Assignment06
# Desc: This assignment demonstrates using functions
# With structured error handling
# Change Log: (Who, When, What)
# RRoot,1/1/2030,Created Script
# Jordan Sellers,2/20/24,Created Script
# -------------------------------------------------------------------------------------------------------------------- #
import json

# Define the data constants
MENU: str = '''
---- Course Registration Program -----
  Select from the following menu:
    1. Register a student for a course
    2. Show current data
    3. Save data to a file
    4. Exit the program
--------------------------------------
'''
FILE_NAME: str = "Enrollments.json"

# Define the data variables
menu_choice: str = ''
students: list = []


class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    Change Log (Who, When, What)
    Jordan Sellers,2/20/24,Created Script
    """

    @staticmethod
    def read_data_from_file(file_name: list, student_data: list):
        try:
            file = open(FILE_NAME, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!")
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            IO.output_error_messages("There was a problem with writing to the file.\n"
                                     "Please check the file is not open by another program", e)


class IO:
    """
    A collection of presentation lay functions that manage user input and output

    Change Log (Who, When, What)
    Jordan Sellers,2/20/24,Created class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """Display a custom error message to the user

        Change Log (Who, When, What)
        Jordan Sellers,2/20/24,Created Function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("--- Technical Error Message ---")
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def output_menu(menu: str):
        """Display the menu to the user

        Change Log (Who, When, What)
        Jordan Sellers,2/20/24,Created Function

        :return: None
        """
        print()
        print(MENU)
        print()

    @staticmethod
    def input_menu_choice():
        """Get the user's menu choice

        Change Log (Who, When, What)
        Jordan Sellers,2/20/24,Created Script

        :return: a string with the user's menu choice
        """
        menu_choice = "0"
        try:
            menu_choice = input("Please select from the menu: ")
            if menu_choice not in ("1", "2", "3", "4"):
                raise Exception("Please select 1, 2, 3, or 4!")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):
        """Display students registered for a course
        
        Change Log (Who, When, What)
        Jordan Sellers,2/20/24,Created Script
        
        :return: None
        """
        print()
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        print()

    @staticmethod
    def input_student_data(student_data: list):
        """Allow user to input new student registration info

        Change Log (Who, When, What)
        Jordan Sellers,2/20/24,Created Function

        :return: A table containing each student's first name, last name, and course
        """
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
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
            IO.output_error_messages("-- Technical Error Message --", e)
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            IO.output_error_messages("-- Technical Error Message --", e)
        return student_data


# Main body of script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:
    IO.output_menu(menu=MENU)
    input_menu_choice = IO.input_menu_choice()

    if input_menu_choice == "1":
        IO.input_student_data(student_data=students)
        continue

    elif input_menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue
    elif input_menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue
    elif input_menu_choice == "4":
        break
