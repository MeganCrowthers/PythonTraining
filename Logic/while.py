#while True:
    #print("Hello World")
#the above statement will run forever! "CONTROL + C"

#num = 0
#while num <= 10:
#    print("Number is: " + str(num)) 
#    num += 1

num = 0
while num <= 10:
    num += 1
    if (num %2) == 0:
        continue
    print("Number is: " + str(num)) 

while True:
    u_input = input()
    if u_input == "q":
        break
    print("You Typed " + u_input)
