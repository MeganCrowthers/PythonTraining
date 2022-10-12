num = input("Enter a number")
print(num)

if num == "20":
    print("You have input 20")
else:
    print("You havent input 20") 

numover20 = True if int(num) > 20 else False
print(numover20)