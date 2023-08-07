#factorial
fact=1
num=int(input("enter a number:"))
if num<0:
    print("the factorial does not exists in negative")
elif num==0:
    print("tha factorial of 0 is 1")
else:
    print("the factorial of",num,"is fact")