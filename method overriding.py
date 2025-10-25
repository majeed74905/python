# Program 4: Method overriding

class Vehicle:
    def display(self):
        print("This is a vehicle.")

class Car(Vehicle):
    def display(self):
        print("This is a car.")

# Example usage
v = Vehicle()
c = Car()
v.display()
c.display()
