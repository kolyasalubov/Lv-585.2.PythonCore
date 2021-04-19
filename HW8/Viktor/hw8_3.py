class Human:
    def __init__(self, name):
        self.name = name
        print(f"Hello {self.name}")

    @staticmethod
    def species():
        print(f"All people are homosapiens")
    

h = Human("Viktor")
h.species()
