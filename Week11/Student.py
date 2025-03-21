from Person import Person

class Student(Person):
    def __init__(self, p_name, p_age, p_height, p_major):
        super().__init__(p_name, p_age, p_height)
        self.__major = p_major
        print("Now this object is a object for a student")

    @property
    def major(self):
        return self.__major
    
    @program.setter
    def program(self, new_major):
        self.__major = new_major

print("This time it's a Student object")
student1 = Student("Renan", 33, 1.67, "T177")
print(f"Student name: {str(student1.name)}\nAge: {int(student1.age)}\nHeight: {float(student1.height)}\nProgram: {str(student1.major)}")