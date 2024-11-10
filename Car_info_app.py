# Author: Benjamin Barrick
# File Name: Car_Info.py
# Description: This program captures and displays information about a car by creating a Vehicle superclass and an Automobile subclass. 
#               The user inputs details about the car, which are then stored and printed in a readable format.

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

def main():
    print("Enter information for your car.")
    
    vehicle_type = "car" 
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")
    
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    print("\nHere is the information about your car:")
    car.display_info()

if __name__ == "__main__":
    main()
