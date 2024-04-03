# Author: diego donado
# File Name: assign.py
# Description: This Python application allows users to input student names and GPAs to determine if they qualify for academic honors.
def main():
    print("Welcome to the Student Qualification App!")
    print("To quit, enter 'ZZZ' for the last name.")

    while True:
        last_name = input("\nEnter the student's last name: ")
        if last_name == 'ZZZ':
            print("Exiting the program...")
            break

        first_name = input("Enter the student's first name: ")
        gpa = float(input("Enter the student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} is on the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} doesn't qualify for any honors.")

if __name__ == "__main__":
    main()
