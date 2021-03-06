#import nessecary functions
import alcohol
import averageMark

#Define input function
def getInput():
    #Ask for option
    print("1: meet dronkenheid  \n2: bereken gemiddelde \n")
    number = None
    #Try to get input, if the user does not enter a number, print message and try again
    while number is None:
        try:
            number = int(input("voer het nummer van een optie in:"))
            return number
        except ValueError:
            print("Voer alstublieft een nummer in.")

#Define the different options
def option1():
    #Get drunkenness and depending on number print output
    drunkenness = alcohol.getDrunkenness()
    print("")
    if drunkenness <= 0.5:
        print("Nuchter \nBij uitkomst van 0,5 of kleiner zijn de effecten van \nalcoholische middelen zo minimaal dat ze verwaarloosbaar zijn.")
    elif drunkenness <= 1:
        print("Spraakzaam \nbij uitkomst 0,5 tot 1 voel je je ontspannen en minder verlegen \nen je krijgt een lekker warm gevoel.")  
    elif drunkenness <= 3.5:
        print("Los \nbij uitkomst 1,1 tot 3,5 verandert je stemming en je gedrag.\nJe krijgt minder remmingen en je geheugen wordt minder. ")
    elif drunkenness <= 7.5:
        print("Aangeschoten \nBij uitkomst 3,6 tot 7,5 je emotioneler,\nje overschat jezelf, je kunt situaties minder goed beoordelen en je reactievermogen loopt terug. \nJe gaat dubbelzien en zweten en grote kans dat je misselijk wordt. \nVanaf dit punt is het zeker niet meer verantwoord om te gaan rijden")
    elif drunkenness <= 13:
        print("zat \nbij uitkomst 7,6 tot 13  raken al je zintuigen verdoofd. \nAlles wat je hoort en ziet dringt nauwelijks tot je door. ")
    elif drunkenness >= 13.1:
        print("Laveloos \nalles boven de 13,1 vertraagt je ademhaling en je polsslag zo erg dat je kans hebt bewusteloos te raken.\nJe kunt ook in een coma raken en zelfs doodgaan omdat je ademhaling stopt.")
    
    print("\nGlazen per uur: " + str(drunkenness))

def option2():
    average = averageMark.getAverage()
    if average is not None:
        print(average)


options = {1 : option1,
           2 : option2
}

#get the users choice
number = getInput()
    
print("\n")

#catch exception when user enters unsupported input
try:
    options[number]()
except KeyError:
    print("invalid input")
