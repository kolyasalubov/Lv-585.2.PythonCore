# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings


def are_you_playing_banjo(name):
    if name [0] =="r" or name [0] =="R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"