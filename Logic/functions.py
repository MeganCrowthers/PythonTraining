import utils
#This shows you how to create a function and call in
def my_print():
    #pass - this is used to ignore - basically...
    print("Hello")

my_print()

#How to create a function and pass data through 
def my_print2(Message):
    print("_,_,_")
    print(Message)
    print("_,_,_")
    
my_print2("Heeeeey")



print(utils.calculator(12,1000)) #looking at function in utils file
print(utils.calculator(17,1000,"divide"))








