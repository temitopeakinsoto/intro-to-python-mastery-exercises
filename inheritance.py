class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number

    def __str__(self):
        return f"Hello, I am {self.name} {self.surname} with NIN: {self.number})"


class Student(Person):

    def __init__(self, name, surname, number, occupation):
        super().__init__(name, surname, number)
        self.occupation = occupation

    def __str__(self):
        return f'{super().__str__()} and I am a {self.occupation}'

print(Person("Temitope", "Akin", 123))
print(Student("Temitope", "Akin", 123, "Software Developer"))
