#palindrome (string)
my_string=str(input("enter a string:"))
rev_string=reversed(my_string)
if list(my_string)==list(rev_string):
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")

#palindrome(number)
num=int(input("enter a number:"))
temp=num
rev=0
while temp!=0:
    rev=(rev*10)+(temp%10)
    temp=temp//10
if(num==rev):
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")
