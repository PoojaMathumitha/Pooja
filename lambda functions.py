# lambda sample program
a=lambda : print("i love python")
a()

#ex 2
user=lambda name : print("hey,i am",name)
user("PoojaMathumitha")

#using filter function
my_list=[1,2,3,4,5,6,7,8,9,10]
new_list=list(filter(lambda a : (a%2!=0),my_list))
print("a=",new_list)

numbers = [1, 2, 3, 4, 5, 6, 7]
even_numbers = filter(lambda x: (x%2 == 0), numbers)
even_numbers = list(even_numbers)
print("even numbers",even_numbers)

#random list using filter function
random_list = [1, 'a', 0, False, True, '0',-1]
filtered_iterator = filter(None, random_list)
filtered_list = list(filtered_iterator)
print(filtered_list)

#map function using lambda
my_list=[1,2,3,4,5]
final_list=list(map(lambda x : x*x,my_list))
print("x=",final_list)

#ex2
num1=[2,4,6,8]
num2=[1,3,5,7]
final_list=list(map(lambda x,y : x+y,num1,num2))
print("z=",final_list)

#reduce function in lambda
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
product= reduce((lambda x, y: x * y), li)
print("z=",product)

