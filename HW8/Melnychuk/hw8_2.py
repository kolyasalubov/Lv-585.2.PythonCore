class Human():
    def __init__(self, name):
        self.name = name

    def hello_message(self):
        return print(f"Hello {self.name}!")

    @classmethod
    def species_method(cls):
        return print("Your species Homosapiens"), cls

    @staticmethod
    def message():
        return print("Good luck!")


f = Human("Dima")
f.hello_message()
Human.species_method()
Human.message()