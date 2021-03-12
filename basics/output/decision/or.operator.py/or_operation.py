print("What type of adventure should I have?")
type= input() 

# Determine what message to display
if  (type == "scary") or (type == "short") :
    print("\nEntering the dark forest!")
elif ( (type == "safe") or (type == "long") ):
    print("\nTaking the safe route!")
else:
    print("\nNot sure which route to take.")
