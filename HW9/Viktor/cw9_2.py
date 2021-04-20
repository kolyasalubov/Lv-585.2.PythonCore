import random

class Ghost(object):
    
    color = random.choice(["white","yellow","purple","red"])
    
    def __init__(self):
        Ghost.color = random.choice(["white","yellow","purple","red"])
        