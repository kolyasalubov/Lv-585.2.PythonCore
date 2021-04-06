mystr = str(input("Put your string here: "))

def calc_characters(mystr):
    counter = 0
    mylist = list(mystr)

    for i in mylist:
        counter = counter + 1
    print(int(counter))
calc_characters(mystr)
