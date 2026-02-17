class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        return self.grades.append(grade)

    def display_info(self):
        info = f'name: {self.name}\n age: {self.age}\n grades: {self.grades}'
        print(info)
        return info
    
    def average_grade(self):
        sum = 0
        grade_len = len(self.grades)

        for grade in self.grades:
            sum += grade
        avg = sum / grade_len
        return avg
    

ken = Student('Ken Thompson', 37)
ken.add_grade(85)
ken.add_grade(92)
ken.add_grade(88)
ken.display_info()
print(ken.average_grade())