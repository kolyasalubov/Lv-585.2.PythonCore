class Employee:
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter +=1
    
    @classmethod
    def countEmpoloyees(cls):
        print(f"We have {Employee.counter} in the company")

    def displayInformation(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    
emp1 = Employee("Oleg", 350)
emp2 = Employee("Vova", 5000)   

emp1.displayInformation()
emp2.displayInformation()
Employee.countEmpoloyees()

help()