import alcohol
import averageMark

def getInput():
    print("1: meet dronkenheid  \n2: bereken gemiddelde \n3: option \n4: option \n")
    number = None
    while number is None:
        try:
            number = int(input("voer het nummer van een optie in:"))
            return number
        except ValueError:
            print("Voer alstublieft een nummer in.")

def option1():
    drunkenness = alcohol.getDrunkenness()
    if drunkenness <= 0.5:
        print("Nuchter")
    elif drunkenness <= 1:
        print("Spraakzaam")
    elif drunkenness <= 2:
        print("Los")
    elif drunkenness <= :
        print("Aangeschoten")
    elif drunkenness <= :
        print("zat")
    elif drunkenness <= :
        print("Laveloos")
    print(drunkenness)

def option2():
    average = averageMark.getAverage()
    if average is not None:
        print(average)

def option3():
    print("option3")

def option4():
    print("option4")

options = {1 : option1,
           2 : option2,
           3 : option3,
           4 : option4,
}

#get the users choice
number = getInput()
    
print("\n")

#catch exception when user enters unsupported input

try:
    options[number]()
except KeyError:
    print("invalid input")
