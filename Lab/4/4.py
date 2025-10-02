"""A university is deciding to upgrade its system. In order to upgrade, you need to implement the
following scenario: Note the following:
• The class student has a function that displays information about the student i.e. id and
name.
• Class marks is derived from class student and has a function that displays all the marks
obtained in the courses by the students. i.e. marks_algo, marks_dataScience,
marks_calculus.
• Class result is derived from class marks. This class has a function that calculates the total
marks and then calculates the average marks. It then displays both the total and the
average marks.
In the main function you are required to do the following:
• Create an object of the result class.
• Then display the student details, the marks obtained in each courses and the total and the
average marks."""

class Student:
    studentID = "24K0000"
    studentName = "Unknown"

    def __init__(self,stdID=None,stdName=None):
        self.studentName = stdName if stdName is not None else Student.studentName
        self.studentID = stdID if stdID is not None else Student.studentID

    def display(self):
        print(f"(Student class)\nStudent Name: {self.studentName}\nStudent ID: {self.studentID}")

class Marks(Student):
    marks_algo = 0
    marks_dataScience = 0
    marks_calculus = 0
    def __init__(self,stdName=None,stdID=None,mAlg=None,mDS=None,mCal=None):
        super().__init__(stdID,stdName)
        self.marks_algo = mAlg if mAlg is not None else Marks.marks_algo
        self.marks_calculus = mCal if mCal is not None else Marks.marks_calculus
        self.marks_dataScience = mDS if mDS is not None else Marks.marks_dataScience

    def display(self):
        print(f"")
        super().display()
        print(f"\n(Marks function)\nMarks in Algorithms: {self.marks_algo}\nMarks in Calculus: {self.marks_calculus}")
        print(f"Marks in Data Science: {self.marks_dataScience}")

class Result(Marks):
    totalMarks = 0
    avgMarks = 0
    def calculateTotalMarks(self):
        self.totalMarks = self.marks_dataScience + self.marks_algo + self.marks_calculus
        print(f"Total marks have been updated of this student {self.studentName}")
        return self.totalMarks

    def calculateTotalAvg(self):
        self.avgMarks = self.totalMarks/3
        print(f"Total average marks of {self.studentName} have been calculated of this student, use display  of result func to display marks")
 
    def display(self):
        print(f"\n(Result function)\nTotal Marks is: {self.totalMarks}")
        print(f"Total Average Marks is: {self.avgMarks}\n\n")
        super().display()

Student().display()
#Marks().display()
Result().display()
print(f"")
std1 = Result()
std1.studentName = "Anwer"
std1.studentID = "24K-0033"
"""Student().studentID = "24K-0006"
Student().studentName = "Baqar Laghari"""

std1.marks_algo = 64
std1.marks_calculus = 65
std1.marks_dataScience = 81
std1.calculateTotalMarks()
std1.calculateTotalAvg()
std1.display()

std2 = Result()
std2.studentName = "Baqar Laghari"
std2.studentID = "24K-0006"
std2.marks_algo = 80
std2.marks_calculus = 97
std2.marks_dataScience = 69
std2.calculateTotalMarks()
std2.calculateTotalAvg()
std2.display()