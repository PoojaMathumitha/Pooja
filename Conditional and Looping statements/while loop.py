#while loop 1
i=1
while i<=5:
    print(i)
    i=i+1

#while loop 2
i=1
n=12
while i<=10:
    print(n,"*",i,"=",n*i)
    i=i+1

#while loop using list
x=[1,2,3,4,5]
i=4
while i<len(x):
    x[0]=x[0]+100
    x[1]=x[1]+100
    x[2]=x[2]+100
    x[3]=x[3]+100
    x[4]=x[4]+100
    i=i+1
    print(x)

#while loop
x=1
while x<3:
    print(x)
    x=x+1
else:
    print("hello")

# reverse the no using while loop
n = 100
while n >= 0:
    print(n, end=" ")
    n = n - 1

# ex while loop
n=int(input("enter a number:"))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("reverse of no is",rev)
        