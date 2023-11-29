print("")
a=input("User Data For Evaluation")
print("",a)
print("__________________________")

x = int(input("Enter Your Salary In Euro: "))
y = (input("Enter you country you want to move: "))

if (y == "Canada"):
    x*1.5
    if(x>56000):
        print("You will be rich in Canada with a salary of",x,"CAD")
    elif(x<56000):
        ("You will be poor in Canada with a salary of",x,"CAD")

if (y == "USA"):
    x*1.1
    if(x>45000):
        print("You will be rich in USA with a salary of",x,"USD")
    elif(x<45000):
        ("You will be poor in USA with a salary of",x,"USD")

if (y == "UK"):
    x*.86
    if(x>45423):
        print("You will be rich in UK with a salary of",x,"Pounds")
    elif(x<45423):
        ("You will be poor in UK with a salary of",x,"Pounds")

if (y == "Cambodia"):
    x*4522
    if(x>7649856):
        print("You will be rich in Cambodia with a salary of",x,"Riel")
    elif(x<7649856):
        ("You will be poor in Cambodia with a salary of",x,"Riel")