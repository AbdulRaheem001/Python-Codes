
            #Calculator

def Add(num1,num2):
    sum=num1+num2
    print("-> ",num1," + ",num2," = ",sum)
def Subtraction(num1,num2):
    if(num1>num2):
        Subt=num1-num2
    else:
        Subt=num2-num1
    print("-> ",num1," - ",num2," = ",Subt)
def Multiplacation(num1,num2):
    Multi=num1*num2
    print("-> ",num1," * ",num2," = ",Multi)
def Division(num1,num2):
    Divi=num1/num2
    print("-> ",num1," / ",num2," = ",Divi)

num1=int(input("Enter First number  :: "))
num2=int(input("Enter Second number :: "))

choice=int(input("Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplacation\nPress 4 for Division \n"))

if(choice==1):
    print("Addition function is calling ")
    Add(num1,num2)
elif(choice==2):
    print("Subtraction function is calling ")
    Subtraction(num1,num2)
elif(choice==3):
    print("Multiplacation function is calling ")
    Multiplacation(num1,num2)
elif(choice==4):
    print("Division function is calling ")
    Division(num1,num2)
else:
    print("You enter an invalied number")
