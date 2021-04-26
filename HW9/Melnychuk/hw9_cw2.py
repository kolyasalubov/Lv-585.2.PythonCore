class Ghost(object):
    def __init__(self, color = ""):
        import random
        self.color = random.choice(["white", "yellow", "purple", "red"])
        

ghost = Ghost()

print(ghost.color)

