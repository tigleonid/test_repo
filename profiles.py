# Class definition for Profile

class Profile:
    def __init__(self, name, age, grades, status):
        self.name = name
        self.age = age
        self.grades = grades
        self.status = status

    def display_profile(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Grades: {self.grades}')
        print(f'Status: {self.status}')
