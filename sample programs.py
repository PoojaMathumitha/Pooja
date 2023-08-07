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

#for loop example
a=["orange","green","red"]
b=["book","chair","phone"]
for i in a:
    for j in b:
        print(i,j)

        