class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_grade(self):
        if self.marks >= 80:
            print(self.name + " got Grade A")
        elif self.marks >= 60:
            print(self.name + " got Grade B")
        else:
            print(self.name + " got Grade C")


# Create objects
s1 = Student("Ali", 85)
s2 = Student("Sara", 55)

# Call method
s1.show_grade()
s2.show_grade()

