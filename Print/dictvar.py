
#Below is a Dict (Dictionary) which is multiple lines of data - kay value pair. Left hand side is key and right handside is value  
address = {
"house_no": 31,
"street":"Elizabeth Way",
"area": "Earls Barton",   
"postcode": "NN6 0HP"
 
}
#Example of how to print a dict
print(address)

#Example of how to print specific values in a dict 
print(address["house_no"])
print(address["street"])
print(address["area"])
print(address["postcode"])

#Example of how to print 2 specific values in a dict 
print(address["house_no"], address["street"])

#Example of how to add a new key value pair 
address["soverign"]="Wellingborough"
print(address)

#Example of how to remove a key value pair 
address.pop("soverign")
print(address)
