
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

#Example of how to add two dictories (customer record & address) and add two lists
customer_record = {
    "first_name": 'Megan',
    "last_name": 'Crowthers',
    "current_address": address,
    "previous_addresses":  [
        {
            "house_no": 112,
            "street":"Main Road",
            "area": "Wilby",   
            "postcode": "NN8 2UE"
        },
        {
            "house_no": "Flat 7, 2-4",
            "street":"Edith Street",
            "area": "Northampton",   
            "postcode": "NN1 2EP"
        },
    ]
}

#How to make a list look prettier from a layout 
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(customer_record)


#printing specific values from a dict/list
print(customer_record["first_name"])
print(customer_record["current_address"]["postcode"])
print(customer_record["previous_addresses"][0]["postcode"])

