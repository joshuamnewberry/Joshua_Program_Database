class Student:
    def __init__(self, name:str, classes:list=None, grades:list=None) -> None:
        if type(grades) != list or type(classes) != list  or type(name) != str:
            raise TypeError
        self.classes = classes
        self.grades = grades
        self.name = name
    
    def __str__(self) -> str:
        return self.name
    
    def add_grade(self, grade:float) -> None:
        if type(grade) != float and type(grade) != int:
            raise TypeError
        self.grades.append(grade)
    def remove_grade(self, grade:float) -> None:
        if type(grade) != float and type(grade) != int:
            raise TypeError
        if grade in self.grades:
            self.grades.remove(self.grades.index(grade))
        else:
            print(str(grade) + "not in grade list")
    
    def add_class(self, classes:str) -> None:
        if type(classes) != str:
            raise TypeError
        self.classes.append(classes)
    
    def remove_class(self, classes:str) -> None:
        if type(classes) != str:
            raise TypeError
        if classes in self.classes:
            self.classes.remove(classes)
        else:
            print(str(classes) + "Not in class list")
    
    def get_classes(self) -> list:
        return self.classes
    
    def get_grades(self) -> list:
        return self.grades
    
    def get_avg_grades(self) -> float:
        return float(sum(self.grades) / len(self.grades))

class Teacher:
    def __init__(self, name:str, students:list, classes:list) -> None:
        if type(students) != list or type(classes) != list or type(name) != str:
            raise TypeError
        self.students = students
        self.classes_taught = classes
        self.name = name
    
    def __str__(self) -> str:
        return self.name
    
    def add_class_taught(self, classes) -> None:
        if type(classes) != str:
            raise TypeError
        self.classes_taught.append(classes)
    
    def remove_class_taught(self, classes) -> None:
        if type(classes) != str:
            raise TypeError
        if classes in self.classes:
            self.classes.remove(classes)
        else:
            print(classes + "Not in class list")
    
    def add_student(self, student:Student) -> None:
        if type(student) != Student:
            raise TypeError
        self.students.append(student)
    
    def remove_student(self, student:Student) -> None:
        if type(student) != Student:
            raise TypeError
        self.students.remove(student)
    
    def get_classes_taught(self) -> list:
        return self.classes_taught
    
    def get_students(self) -> list:
        return self.students

class Department:
    def __init__(self, name:str, classes: list, teachers: list) -> None:
        if type(classes) != list or type(teachers) != list or type(name) != str:
            raise TypeError
        self.classes = classes
        self.teachers = teachers
        self.name = name
    
    def __str__(self) -> None:
        return self.name

    def add_teacher(self, teacher: Teacher) -> None:
        if type(teacher) != Teacher:
            raise TypeError
        self.teachers.append(teacher)

    def remove_teacher(self, teacher: Teacher) -> None:
        if type(teacher) != Teacher:
            raise TypeError
        if teacher in self.teachers:
            self.teachers.remove(teacher)
        else:
            print(teacher + "not in teacher list")
        
    def add_class(self, classes: str) -> None:
        if type(classes) != str:
            raise TypeError
        self.classes.append(classes)

    def remove_class(self, classes: str) -> None:
        if type(classes) != str:
            raise TypeError
        if classes in self.classes:
            self.classes.remove(classes)
        else:
            print(classes + "Not in class list")
            
    def get_classes(self):
        return self.classes
    
    def set_classes(self, new_classes: list):
        self.classes = new_classes
        
    def get_teachers(self):
        return self.teachers
    
    def set_teachers(self, new_teachers: list):
        self.teachers = new_teachers

class School:
    def __init__(self, departments: list = [], students: list = []):
        self.departments = departments
        self.students = students
    
    def add_department(self, department: Department) -> None:
        if type(department) != Department:
            raise TypeError
        self.departments.append(department)
    
    def remove_department(self, department: Department) -> None:
        if type(department) != Department:
            raise TypeError
        if department in self.departments:
            self.departments.remove(department)
        else:
            print(str(department) + "Not in class list")
    
    def add_student(self, student: Student) -> None:
        if type(student) != Student:
            raise TypeError
        self.students.append(student)
    
    def remove_student(self, student: Student) -> None:
        if type(student) != Student:
            raise TypeError
        if student in self.students:
            self.students.remove(student)
        else:
            print(str(student) + "not in student list")

    def get_departments(self):
        return self.departments

    def set_departments(self, new_departments: list):
        self.departments = new_departments

    def get_students(self):
        return self.students
    
    def set_students(self, new_students: list):
        self.students = new_students
