class Employee():
    """
    Class Empoyee return numbers of employees and information about name and salay
    """

    counter = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def number_of_employees(cls):
        return print(f"Working people: {Employee.counter}")

    def info(self):
        print(f"Name: {self.name}; Salary: {self.salary}")

e1 = Employee("John", 2000)
e2 = Employee("Ron", 2200)
e3 = Employee("Jack", 3000)

e1.info()
e2.info()
e3.info()
Employee.number_of_employees()

print(Employee.__base__)

print(Employee.__base__())

print(Employee.__dict__)

print(Employee.__name__)

print(Employee.__module__)

print(Employee.__doc__)
