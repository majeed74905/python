# Program 3: Polymorphism demonstration

class Student:
    def display(self):
        print("This is a UG Student.")

class PGStudent:
    def display(self):
        print("This is a PG Student.")

# Common function to demonstrate polymorphism
def show_info(obj):
    obj.display()

# Example usage
s1 = Student()
s2 = PGStudent()
show_info(s1)
show_info(s2)
