def getAverage():

    #initialise variables
    #variable 
    go = 1
    
    total = 0
    number = 0
    average = 0
    mark = 0
    weight = 0
    
    while go:

        #
        print("Enter calc at any time to calculate result.")
        mark = input("Enter mark: ")
            
        if mark.lower() == "calc":
            pass
        else: 
            weight = input("Enter mark weight: ")
            
        try:
            float(mark)
            float(weight)
            isfloat = 1  
        except ValueError:
            isfloat = 0
        
        #
        if mark.lower() == "calc" or weight.lower() == "calc":
            go = 0
        elif isfloat and weight != 0:
            #
            total += float(mark)*float(weight)
            number += float(weight)
        elif not isfloat:
            print("Voer een getal in!\n")

    try:
        average = total/number
    except ZeroDivisionError:
        print("Geen getallen in gevoerd")
        average = None
    return average

