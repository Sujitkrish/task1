# - Define a Student class with attributes: name, roll_number, marks.
# - Add a method to calculate grade based on marks.
# - Create multiple student objects and print their grades.

class Student:
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
    def grade (self):
        if (self.marks < 30):
            return "F"
        elif (self.marks > 30 and self.marks <= 60):
            return "B"
        elif (self.marks > 60 and self.marks <= 100):
            return "A"
bhuvi = Student("Bhuvi",1,80)
print(f"Your Grade is :{bhuvi.grade()}")
sujit = Student("Sujit",2,60)
print(f"{sujit.name}Your Grade is :{sujit.grade()}")


        
