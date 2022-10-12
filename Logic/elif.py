##elif is a way of grouping IF statements together - you can break out of if statement once true 

from ast import Or

#Python thought our num was a 'str' and not 'int' so we have forced the output to be an int
num = int(input("Please input a number"))
print(num)

if num == 20:
    print("You have input 20")
elif num < 20:
    print("You have input less than 20")
elif num > 20 and num < 30:
    print("Your number is between 20 and 30") 
#before the below was above line 13. As this is an elif statement, any inputs more than 20 will always display "You have less than 20" due to elif stopping when statement reaches true"
elif num > 20:
    print("You have input more than 20")

#if statement within an if statement (nested if)
if num == 20:
    print("You have input 20")
elif num > 20:
    print("You have input over 20")
    if num > 25:
        print("You have input over 25")
    else:
        print("You have given a number between 20 & 25")
else:
    print("Your number is below 20")