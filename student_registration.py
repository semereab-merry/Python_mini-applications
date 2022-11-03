class Vehicle:
    """information about vehicle, compares the fares of each instance of vehicle"""

    # initializing
    def __init__(self, fare=0):
        self.name = ""
        self.fare = fare

    # setter and getter
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_fare(self, fare):
        self.fare = fare

    def get_fare(self):
        return self.fare

    # over-riding add function to display the sum of fares of two objects of the class
    def __add__(self, other):
        new_fare= self.fare + other.fare
        return new_fare

    # over-riding add function that return True if the fare of the self vehicle is greater than the other vehicle's
    def __gt__(self, other):
        if self.fare > other.fare:
            return True
        return False

    # over-riding add function that return True if the fare of the self vehicle is less than the other vehicle's
    def __lt__(self, other):
        if self.fare < other.fare:
            return True
        return False

    # over-tiding str function to print the fare of each instance of Vehicle class with a description
    def __str__(self):
        return "{} has fare of {}".format(self.get_name(), self.get_fare())
