class Vehicle:
    seatingCap = 1
    charges = seatingCap * 100
    def __init__(self,charges=None,seatingCap=None):
        self.charges = charges if charges is not None else Vehicle.charges
        self.seatingCap = seatingCap if seatingCap is not None else Vehicle.seatingCap
    def display(self):
        print(f"Total seating capacity is: {self.seatingCap}\nTotal Bus fare is: {self.charges}")
    
class Bus(Vehicle):
    def __init__(self,charges =None,seatingCap=None):
        self.seatingCap = seatingCap if seatingCap is not None else Vehicle().seatingCap
        self.charges = charges * 1.1 if charges is not None else Vehicle().charges * 1.1

    def display(self):
        print(f"Total seating capacity is: {self.seatingCap}\nTotal Bus fare after maintence cost is: {self.charges}")

#Vehicle.display(self=0)
Vehicle().display()
Vehicle(120,1).display()

Bus().display()
Bus(120,1).display()