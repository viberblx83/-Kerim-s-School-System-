students = {}
classes = set()

def create_class(class_name):
    if class_name not in classes:
        classes.add(class_name)
        students[class_name] = []

def delete_class(class_name):
    if class_name in classes:
        classes.remove(class_name)
        del students[class_name]

def create_student(class_name, name, surname, age, grade):
    if class_name in classes:
        students[class_name].append({"name": name, "surname": surname, "age": age, "grade": grade})

def delete_student(class_name, student_name):
    if class_name in classes:
        for student in students[class_name]:
            if student["name"] == student_name:
                students[class_name].remove(student)

def update_student(class_name, old_student_name, new_student):
    if class_name in classes:
        for i in range(len(students[class_name])):
            if students[class_name][i]["name"] == old_student_name:
                students[class_name][i] = new_student

def read_class_info(class_name):
    if class_name in classes:
        print(f"Class: {class_name}")
        for student in students[class_name]:
            print(f"Name: {student['name']}, Surname: {student['surname']}, Age: {student['age']}, Grade: {student['grade']}")

def main():
    while True:
        print("\n1. Create Class\n2. Delete Class\n3. Create Student\n4. Delete Student\n5. Update Student\n6. Read Class Info\n7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            class_name = input("Enter the class name: ")
            create_class(class_name)
            print(f"Class '{class_name}' created.")

        elif choice == "2":
            class_name = input("Enter the class name to delete: ")
            delete_class(class_name) 
            print(f"Class '{class_name}' deleted.")

        elif choice == "3":
            class_name = input("Enter the class name: ")
            name = input("Enter student name: ")
            surname = input("Enter student surname: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            create_student(class_name, name, surname, age, grade)
            print(f"Student '{name}' added to class '{class_name}'.")

        elif choice == "4":
            class_name = input("Enter the class name: ")
            student_name = input("Enter student name to delete: ")
            delete_student(class_name, student_name)
            print(f"Student '{student_name}' deleted from class '{class_name}'.")

        elif choice == "5":
            class_name = input("Enter the class name: ")
            old_student_name = input("Enter the name of the student to update: ")
            name = input("Enter new student name: ")
            surname = input("Enter new student surname: ")
            age = int(input("Enter new student age: "))
            grade = input("Enter new student grade: ")
            new_student = {"name": name, "surname": surname, "age": age, "grade": grade}
            update_student(class_name, old_student_name, new_student)
            print(f"Student '{old_student_name}' updated in class '{class_name}'.")

        elif choice == "6":
            class_name = input("Enter the class name: ")
            read_class_info(class_name)

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

