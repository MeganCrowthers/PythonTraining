#dog names is a list 
dog_names = ["Aria","Martha","Lola"]

#print variable as it is 
print(dog_names)

#printing a specific item in the list (Starts with 0)
print(dog_names[0])
print(dog_names[1])
print(dog_names[2])

#printing entire list without brackets
print(dog_names[0],dog_names[1],dog_names[2])

#print LENGTH of list (number of items)
print(len(dog_names))

#print LAST items in list 
print(dog_names[len(dog_names)-1])

#add new name to list and print  
dog_names.append("Jasper")
print(dog_names)

#remove specific name from list and print  
dog_names.remove("Lola")
print(dog_names)

#remove the first item from list and print 
dog_names.pop(0)
print(dog_names)
#This can be used to remove any item in list, but must know which item

#How to a list within a list 
fave_foods = [
    "Chips",
    "Crisps",
    "Passion Fruit",
    "Coffee",
    [
        "Sponge Cake",
        "Carrot Cake",
        "Chocolate Cake",
        "Velvet Cake",
    ]
]

#print a specific value within 2 lists 
print(fave_foods[4][2])