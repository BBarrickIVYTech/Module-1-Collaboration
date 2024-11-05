# Author: Benjamin Barrick
# File Name: student_honors_app.py
# Description: This program accepts student names and GPAs, and checks if the student qualifies
#              for the Dean's List (GPA >= 3.5) or the Honor Roll (GPA >= 3.25).
#              Input 'ZZZ' as the last name to stop the program.

def main():
    while True:
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ").strip()
        
        if last_name.upper() == 'ZZZ':
            print("Exiting program.")
            break
        
        first_name = input("Enter the student's first name: ").strip()
        try:
            gpa = float(input("Enter the student's GPA: ").strip())
        except ValueError:
            print("Invalid GPA. Please enter a number.")
            continue
        
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")
main()
