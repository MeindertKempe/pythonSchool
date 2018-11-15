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
        print("Nuchter \n Bij uitkomst van 0,5 of kleiner zijn de effecten van alcoholische middedlen zo minimaal dat ze verwaarloosbaar zijn.")
    elif drunkenness <= 1:
        print("Spraakzaam\ n bij uitkomst 0,5 tot 1 voel je je ontspannen en minder verlegen \n en je krijgt een lekker warm gevoel.")  
    elif drunkenness <= 3.5:
        print("Los \nbij uitkomst 1,1 tot 3,5 verandert je stemming en je gedrag.\nJe krijgt minder remmingen en je geheugen wordt minder. ")
    elif drunkenness <= 7.5:
        print("Aangeschoten \nBij uitkomst 3,6 tot 7,5 je emotioneler,\nje overschat jezelf, je kunt situaties minder goed beoordelen en je reactievermogen loopt terug. \nJe gaat dubbelzien en zweten. En? grote kans dat je misselijk wordt. \n Vanaf dit punt is het zeker niet meer verantwoord om te gaan rijden")
    elif drunkenness <= 13:
        print("zat bij uitkomst 7,6 tot 13  raken al je zintuigen verdoofd. \nAlles wat je hoort en ziet dringt nauwelijks tot je door. ")
    elif drunkenness >= 13.1:
        print("Laveloos alles boven de 13,1 vertraagt je ademhaling en je polsslag zo erg dat je kans hebt bewusteloos te raken.\nJe kunt ook in een coma raken en zelfs doodgaan omdat je ademhaling stopt.")
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
