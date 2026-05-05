class Person:
    age: int

    # The constructor
    def __init__(self, first_name, last_name, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def set_age(self, age: int):
        self.age = age

    def set_first_name(self, first_name: str):
        self.first_name = first_name

    def greeting(self):
        print('\n')
        print(f'Hello, my name is {self.first_name} {self.last_name}! I\'m {self.age} years old!')

abc = Person("Daniel", "Morrison", 24)
abc.greeting()

xyz = Person("Jane", "Doe", 22)
xyz.greeting()