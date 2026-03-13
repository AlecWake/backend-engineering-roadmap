from storage import save_students, load_students

def add_student(student_dict):
    name = input("\nStudent Name: ")
    try:
        grade = int(input("Student Grade: "))
        student_dict[name] = grade
        save_students(student_dict)
    except ValueError:
        print("Improper grade input, cant cast to int.")

def delete_student(student_dict):
    name = input("\nStudent to delete: ")
    try:
        del student_dict[name]
        save_students(student_dict)
    except KeyError:
        print("name not found...")

def update_grade(student_dict):
    name = input("\nStudent Name: ")
    if name in student_dict:
        try:
            new_grade = int(input("New student Grade: "))
            student_dict[name] = new_grade
            save_students(student_dict)
        except ValueError:
            print("Improper grade input, cant cast to int.")
    else:
        print("name not found...")

def print_grades(student_dict):
    print("\n")
    if student_dict == {}:
        print("No grades in Log...")
    else:
        for student in student_dict:
            print("Name:", student, "Grade:", student_dict[student])

def menu_loop(student_dict):
    loop_con = True
    while loop_con:
        option = input(
            "1.) Add a student\n"
            "2.) Update a students grade\n"
            "3.) Delete a student\n"
            "4.) Print all grades\n"
            "5.) Quit the program\n"
            "Enter option: "
        )

        if option == "1":
            add_student(student_dict)
        elif option == "2":
            update_grade(student_dict)
        elif option == "3":
            delete_student(student_dict)
        elif option == "4":
            print_grades(student_dict)
        elif option == "5":
            loop_con = False
            print("exiting...")
        else:
            print("Incorrect option input, try again...\n")
        print("\n")
        
def main():
    student_dict = load_students()
    menu_loop(student_dict)

main()