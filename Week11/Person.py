class Person:
    def __init__(self, p_name, p_age, p_height):
        print("Constructing the person object")
        self.__name = p_name
        self.__age = p_age
        self.__height = p_height
        self.public_prop = "I'm public"

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, new_height):
        self.__height = new_height

    def __del__(self):
        print("The garbage collector is automatically destroying the person object")

person1 = Person("Mark", 20, 1.67)
print(f"The name of the person is {str(person1.name)}\nAge: {int(person1.age)}\nHeight: {float(person1.height)}")

person1.name = "Alfred"
print(f"The name of the person is {str(person1.name)}") 