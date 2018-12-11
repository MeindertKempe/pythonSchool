def getDrinkNumber(alcohol):
    isint = 0
    while isint == 0:
        try:
            number = int(input("Hoeveel " + alcohol + " heb je op?:"))
            isint = 1
        except ValueError:
            print("Voer alstublieft een nummer in.")
    return number

def getDrunkenness():

    #Get number of drinks a person has drunk
    glasses = getDrinkNumber("glazen met alcohol")
    #strongbeer = getDrinkNumber("sterk bier")

    #beer = getDrinkNumber("beer")
    #beer = getDrinkNumber("beer")

    #Get the amount of time it has taken to drink this
    isint = 0
    while isint == 0:
        try:
            time = float(input("Over hoeveel uur heeft u dit op?:"))
            while time == 0:
                time = float(input("De tijd kan geen 0 zijn\nOver hoeveel uur heeft u dit op?:"))
            isint = 1
        except ValueError:
            print("Voer alstublieft een getal in.")
    
    #Define the strength of each drink
    standardStrength = 1

    #Calculate the total strength
    
    total = standardStrength*glasses
    
    #no longer needed
    #number = normalbeer + strongbeer + shotje + wine
    drunkenness = total/time
    return drunkenness

#
#
#
#
#
#
#
