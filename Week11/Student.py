from Person import Person

class Student(Person):
    def __init__(self, p_name, p_age, p_height, p_program):
        super().__init__(p_name, p_age, p_height)
        self.__program = p_program
        print("Now this object is a object for a student")

    @property
    def program(self):
        return self.__program
    
    @program.setter
    def program(self, new_program):
        self.__program = new_program

student1 = Student("Renan", 33, 1.67, "T177")
print(f"Student name: {str(student1.name)}\nAge: {int(student1.age)}\nHeight: {float(student1.height)}\nProgram: {str(student1.program)}")