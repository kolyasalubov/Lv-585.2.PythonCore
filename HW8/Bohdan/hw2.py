class Human:
    def __init__(self, name):
        self.name = name

    def greetings(self):
        return print(f'Hi {self.name}!')

    def species_name(self):
        return 'Homosapiens'

    @staticmethod
    def static_met():
        return print('laziness turned a monkey into a human')


Human(input('Enter your name\n >>>')).greetings()
