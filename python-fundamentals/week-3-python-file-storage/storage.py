def load_students():
    student_dict = {}
    try:
        with open("grade-report.txt", "r") as file:
            for line in file:
                name, grade = line.rstrip("\n").split(",")
                grade = int(grade)
                student_dict[name] = grade
        return student_dict
    except FileNotFoundError:
        return student_dict

def save_students(student_dict):
    with open("grade-report.txt", "w") as file:
        for name in student_dict:
            file.write(name + "," + str(student_dict[name]) + "\n")