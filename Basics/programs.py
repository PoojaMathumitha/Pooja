#basic program
x="pooja"
print(x)

#simple calculation
#addition
x=23
y=45
z=x+y
print(z)

#sub
x=12
y=5
z=x-y
print(z)

#swapping
x=20
y=40
x,y=y,x
print("x=",x)
print("y=",y)

#type
z=1
print(type(z))

z=6/2
print(z)
print(type(z))

#x=5.5/2
#print(x)


#tuple to list
x=("pooja",174,20)
x=list(x)
print(x)
#list to tuple
z=["pooja",174,20]
z=tuple(z)
print(z)

a=(20,10,100,30)
print(a[:])
x=a[:]
print("x=",x)

z=["pooja",174,20]
print(174 in z)

z=["pooja",174,20]
print("jupi" in z)

#z=["pooja",174,20]
#z[10]
#print(z)

x="pooja"+" "+"mathumitha"
print(x)

x=("pooja"+" ")*10
print(x)

x=["pooja"]+[5]
print(x)

x=[1,3,5,7,9]
y=[2,4,6,8,10]
x.extend(y)
x.sort()
print(x)