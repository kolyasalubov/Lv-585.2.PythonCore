class Employee:
    """
    Class employee return numbers of employees and information about name and salary
    """
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def number_of_employees(cls):
        return print(f'Working people: {Employee.counter}')

    def info(self):
        print(f'{self.name} : {self.salary}')


def output():
    Employee.number_of_employees()
    e1.info()
    e2.info()
    e3.info()
    e4.info()
    e5.info()
    print('', Employee.__base__, Employee.__base__(), Employee.__dict__, Employee.__name__,
          Employee.__module__, Employee.__doc__, sep='\n===============================\n')


e1 = Employee('Sam', 3500)
e2 = Employee('Ron', 4000)
e3 = Employee('Michel', 3850)
e4 = Employee('Tomas', 3450)
e5 = Employee('Jack', 4320)


output()
