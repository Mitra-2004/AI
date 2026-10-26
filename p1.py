#Design and implement a simple reflex agent for the Vacuum Cleaner World and analyze its rational behavior in a given environment.
rooms = { 'A' : 'Dirty' , 'B' : 'Dirty' , 'C' :'Dirty'}
location = "A"

while "Dirty" in rooms.values():
    print("Location :" , location )

    if rooms[location] == "Dirty":
        print("Cleaning room " , location )
        rooms[location] = "Clean"

    elif location == "A" :
        location = "B"

    elif location == "B" :
        location = "C"

    else :
        location = "A"

print("All rooms are cleaned !")