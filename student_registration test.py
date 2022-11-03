from hw import *

# creating objects of the class vehicle by getting inputs from the user
bus = Vehicle()
bus.set_name(input("Enter name of the bus: "))
bus.set_fare(int(input("Enter the it's fare: ")))
print("-" * 70)

car = Vehicle()
car.set_name(input("Enter name of the car: "))
car.set_fare(int(input("Enter the it's fare: ")))

print("-" * 70)
# creating another object to test our add function
sum_fare = car + bus
print("Sum of the fares:", sum_fare)

print("-" * 70)
# check greater than and less than function we over-ride

print("***Check greater than***")
if bus > car:
    print("Fare of", bus.name, "is greater than of", car.name)
else:
    print("Fare of", car.name, "is greater than of", bus.name)

print("-" * 70)
print("***Check less than***")
if bus < car:
    print("Fare of", bus.name, "is less than of", car.name)
else:
    print("Fare of", car.name, "is less than of", bus.name)
