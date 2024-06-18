#MO2 Case Study, GPA program
#Christopher Emmons
#MO2 GPA Assignment
#This app will accept user input of students names, their GPA, and if 
#they are on the Deans List or Honor Roll

#Header
def main():

#declare variables
    studentGPA = 0.00
    deansListMin = 3.50
    honorRollMin = 3.25

#input student last name
#include end operator ZZZ
    lastName = (input("Enter your Last Name or ZZZ to quit: "))
    while lastName == 'ZZZ':
        print("Operation Ended. Thank you.")
        return

#Input Student first name
    firstName = (input("Enter your First Name: "))

#input student GPA
    studentGPA = float(input("Enter student's GPA: "))

#if statements for Deans list and Honor Roll
    if studentGPA >= deansListMin:
        print(f"{lastName} {firstName} has made the Dean's List")
    elif studentGPA >= honorRollMin:
        print(f"{lastName} {firstName} has made the Honor Roll")
    else:
        print(f"{lastName} {firstName} has not made Dean's List or Honor Roll")

if __name__ == "__main__":
    main()
