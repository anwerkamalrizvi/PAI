"""Create a class called "Employee" with properties "name" and "salary". Add a method called
"calculateBonus" that calculates a bonus amount based on the employee's salary. Managers get a
bonus equal to 20% of their salary, while developers get a bonus equal to 10% of their salary.
Then, create two subclasses called "Manager" and "Developer" that inherit from the Employee
class. The Manager class should have a method called "hire" that logs a message indicating that
the manager is hiring someone, while the Developer class should have a method called
"writeCode" that logs a message indicating that the developer is writing code. Finally, create a
subclass called "SeniorManager" that inherits from the Manager class and that should have the
"calculateBonus" method to give senior managers a bonus equal to 30% of their salary."""

class Employee:
    name = "Unknown"
    salary = 0.0
    def __init__(self,n=None,s=None):
        self.name = n if n is not None else Employee.name
        self.salary = s if s is not None else Employee.salary

    def calculateBonus(self,totalBonusForThatEmployee):
        self.salary = self.salary*totalBonusForThatEmployee
        print(f"Bonus of {(totalBonusForThatEmployee*100) - 100}% is added sucessfully!")

    def display(self):
        print(f"Name:{self.name}\nSalary:{self.salary}")

class Manager(Employee):
    def hire(self):
        print(f"Manager is hiring someone. \n")
    def calculateBonus(self,get):
        super().calculateBonus(get)
        
    """def display(self):
        super().display()
        print(f"")"""
class Developer(Employee):
    def writeCode(self):
        print(f"Developer is writing code \n")
    def calculateBonus(self):
        super().calculateBonus(1.1)
class SeniorManager(Manager):
    def calculateBonus(self):
        super().calculateBonus(1.3)
print(f" ")
d = Developer()
d.name = "Pasha"
d.salary = 6854.25
d.writeCode()
d.display()
d.calculateBonus()
d.display()
print(f"")
m = Manager()
m.name = "Aenn"
m.salary = 250000
m.hire()
m.display()
m.calculateBonus(1.2)
m.display()
print(f"")
s = SeniorManager()
s.name = "Baqar"
s.salary = 315000
s.display()
print(f"After calculation of bonus is:")
s.calculateBonus()
s.display()