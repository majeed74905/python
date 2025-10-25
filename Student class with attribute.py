# Program 2: Student and PGStudent class

class Student:
    def __init__(self, ug_degree):
        self.ug_degree = ug_degree

class PGStudent(Student):
    def __init__(self, ug_degree, pg_degree):
        super().__init__(ug_degree)
        self.pg_degree = pg_degree

    def display(self):
        print(f"UG Degree: {self.ug_degree}, PG Degree: {self.pg_degree}")

# Example usage
p = PGStudent("B.Sc Computer Science", "M.Sc Computer Science")
p.display()
