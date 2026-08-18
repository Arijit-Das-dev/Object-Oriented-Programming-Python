# Creating class blueprint
# This is a class or a blueprint of a student
class Student:

    name: str = 'Devid'
    dept: str = 'CSE'
    sec: str = 'X'
    age: int = 18
    is_student: bool = True

# creating objects of that student class
obj_1 = Student()   # object 1 -> Student class 
obj_2 = Student()   # object 2 -> Student class

# All the functionalities of that class
print(obj_1.name)
print(obj_1.dept)
print(obj_1.sec)
print(obj_1.age)
print(obj_1.is_student)