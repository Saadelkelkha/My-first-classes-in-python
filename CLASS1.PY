class Employer():
    def __init__(self, number, name, sales, bonushrs, basesalary=0):
        # Initialize the Employer object with the provided parameters
        self.number = number
        self.name = name
        self.sales = sales
        self.bonushrs = bonushrs
        self.basesalary = basesalary
    
    def info(self):
        # Display information about the employee
        print("The employee number is {}. Name is {}. Base salary is {}. Sales are {}.".format(self.number, self.name, self.basesalary, self.sales))
    
    # The following method is commented out because it's not implemented in the code
    # def calculateNetSalary():

# Create instances of the Employer class
emp1 = Employer(1, "Saad", 20000, 42)
emp2 = Employer(2, "kbour", 1000, 65, 60000)

# Display information about each employee
emp1.info()
emp2.info()
