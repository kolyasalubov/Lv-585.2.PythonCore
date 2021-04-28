import random

class Ghost():
    
    color = ["white","yellow","purple","red"]
    
    def __init__(self):
        self.color = random.choice(Ghost.color)
        