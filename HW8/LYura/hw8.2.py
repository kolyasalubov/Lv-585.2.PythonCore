class Human:
  def __init__(self):
    self.name = input("Put your name here: ")

  def instance(self):
    print(f"You are welcome {self.name}!")

  @classmethod
  def classmet(cls):
      print("And you are Homosapiens")
      cls.static()

  @staticmethod
  def static():
      print("Good Buye")
 
man = Human()
man.instance()
man.classmet()
