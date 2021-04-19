class Car:
    def __init__(self, name, kind, model):
       self.name = name
       self.kind = kind
       self.model = model
 
    def start(self):
        print (f"We start the engine {self.name}")
 
    def stop(self):
        print (f"Turn off the engine {self.name}")


t1 = Car("Audi","R","8")
t1.start()
t2 = Car("BMW","Mini Hatch","F55")
t2.stop()
