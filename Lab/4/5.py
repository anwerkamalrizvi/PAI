""" You are tasked with developing a software system to manage vehicle rentals for a car rental
company. The company offers different types of vehicles for rent, including cars, SUVs, and trucks.
Each vehicle has attributes like the make, model, rental price, and availability status. done
• Design a class hierarchy to represent different types of vehicles (e.g., Car, SUV, Truck). done
• Implement methods within each vehicle class to check availability, calculate the total
rental cost for a given period, and display vehicle details. Ensure that the availability
status changes when a vehicle is rented or returned. done
• Create a class for managing rental reservations (e.g., RentalReservation) that connects a
customer to a rented vehicle. This class should include details like the rental start date,
end date, and the customer renting the vehicle.
• Design a customer class (e.g., Customer) to store information about renters, including
name, contact information, and rented vehicles. Implement a method to display a
customer's rental history.
• Demonstrate polymorphism by creating a function or method that can display the details
of any vehicle (Car, SUV, Truck) or rental reservation (RentalReservation).
• Incorporate encapsulation principles to protect sensitive information like rental prices
and customer contact details. """
print(f"\n\t\tCar Rental System\n")

class Vehicle:
    make = "XYZ"
    model = 2025
    rentalPrice = 10000.0
    availablity = "N/A"

    def __init__(self,make,model,rP,a):
        self.make  = make
        self.model = model
        self.rentalPrice = rP
        self.availablity = a

    def displayFunction(self):
        print(f"\nMake: {self.make}\nModel: {self.model}\nrental price: {self.rentalPrice}\navailable? {self.availablity}")

class Car(Vehicle):
    def rent(self):
        if(self.availablity=="Yes"):
            print(f"Car { self.make} has been rented")
            self.availablity = "No"
        else:
            print(f"Car already rented.")
            return
        
    def withdrawRent(self):
        if(self.availablity=="No"):
            print(f"Car {self.make} has been returned")
            self.availablity = "Yes"
        else:
            print(f"Car already NOT rented yet?.")
            return

    def setPrice(self,given):
        self.rentalPrice = given
        print(f"Car {self.make} of model {self.model} price is set to {self.rentalPrice}")

class SUV(Vehicle):
    def rent(self):
        if(self.availablity=="Yes"):
            print(f"SUV {self.make} has been rented")
            self.availablity = "No"
        else:
            print(f"SUV already rented.")
            return
        
    def withdrawRent(self):
        if(self.availablity=="No"):
            print(f"SUV {self.make} has been returned")
            self.availablity = "Yes"
        else:
            print(f"SUV already NOT rented yet?.")
            return

    def setPrice(self,given):
        self.rentalPrice = given
        print(f"SUV {self.make} of model {self.model} price is set to {self.rentalPrice}")

    def display(self):
        self.displayFunction()

"""• Create a class for managing rental reservations (e.g., RentalReservation) that connects a
customer to a rented vehicle. This class should include details like the rental start date,
end date, and the customer renting the vehicle.
"""
class RentalReservation(Car,SUV):
    rentalStartDate = "11/09/2001"
    rentalEndDate = "09/11/2001"
    customerName = "Unknown"
    
    def __init__(self,rS,rE,cN):
        self.rentalStartDate = rS
        self.rentalEndDate = rE
        self.customerName = cN 

    """def __del__ ():
        print(f"")
    """
    def changeDate(self,date):
        self.rentalStartDate = date

    def changeEndDate(self,endDate):
        self.rentalEndDate = endDate

    def changeCustomerName(self,c):
        self.customerName = c

    def display(self):
        print(f"Car Rent start date: {self.rentalStartDate}\nCar Rent end date {self.rentalEndDate}\nCustomer is: {self.customerName} \n")
        return super().display()

class Customer:
    name = "Unknown"
    __contact = "N/A"
    rentedVehicles = []

    def __init__(self, name, contact):
        self.name = name
        self.__contact = contact
        self.rentedVehicles = []

    def addRental(self, vehicle):
        self.rentedVehicles.append(vehicle)

    def displayHistory(self):
        print(f"\nCustomer: {self.name}")
        print(f"Contact: {self.__contact}")
        if len(self.rentedVehicles) == 0:
            print("No rental history yet.")
        else:
            print("Rental History:")
            for i, v in enumerate(self.rentedVehicles, 1):
                print(f"{i}. {v.make} ({v.model})")

    def changeContact(self, newContact):
        self.__contact = newContact

    def getContact(self):
        return self.__contact


class Truck(Vehicle):
    def rent(self):
        if(self.availablity=="Yes"):
            print(f"Truck {self.make} has been rented")
            self.availablity = "No"
        else:
            print(f"Truck already rented.")
            return
        
    def withdrawRent(self):
        if(self.availablity=="No"):
            print(f"Truck {self.make} has been returned")
            self.availablity = "Yes"
        else:
            print(f"Truck already NOT rented yet?.")
            return

    def setPrice(self,given):
        self.rentalPrice = given
        print(f"Truck {self.make} of model {self.model} price is set to {self.rentalPrice}")


def showDetails(obj):
    print("\n--- Details ---")
    if isinstance(obj, Vehicle):
        obj.displayFunction()
    elif isinstance(obj, RentalReservation):
        obj.display()
    elif isinstance(obj, Customer):
        obj.displayHistory()
    else:
        print("Unknown object type.")


    



a = Car("Toyota",2015,5500,"Yes")
a.displayFunction()
a.rent()
a.displayFunction()
a.rent()
a.displayFunction()
a.withdrawRent()
a.displayFunction()
a.setPrice(6000)
a.displayFunction()

s = SUV("Honda",2012,7500,"No")
s.displayFunction()
s.rent()
s.withdrawRent()
s.displayFunction()

r = RentalReservation("12/5/2025","15/5/2025","Qaari")
r.display()
r.make = "Kia Sportage"
r.model = 2023
r.display()
r.changeCustomerName("Cherry BOOM")
r.availablity ="Yes"
r.display()

c = Customer("Laghari", "lagharibhaagobhai@runtime.com")
t = Truck("Toyota Revo Rocco", 2024, 19000, "Yes")
t.displayFunction()
t.rent()
t.withdrawRent()
t.setPrice(19860)
t.displayFunction()

r2 = RentalReservation("05/10/2025", "10/10/2025", "Haji Sahib")
r2.make = "Toyota Revo Rocco"
r2.model = 2024
r2.display()

c.addRental(t)
c.displayHistory()
showDetails(c)
showDetails(t)
showDetails(r2)
