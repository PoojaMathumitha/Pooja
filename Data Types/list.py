x=[20,"pooja",174]
print(type(x))

x=[20,"pooja",174,"pooja"]
print(x)

x=[20,"pooja",174,"jupi",5]
print(x[2:])

x=[20,"pooja",174,"jupi",5]
print(x[:1])

x=[20,"pooja",174,"jupi",5]
print(x[1:6])

x=[20,"pooja",174,"jupi",5]
x.append(143)
print("after append:",x)

x=[20,"pooja",174]
y=[5,"jupi"]
x.extend(y)
print(x)

x=[20,"pooja",174,"jupi",5]
x.insert(2,143)
print(x)

life=["pooja",20,"jupi"]
life[1]="love"
print(life)

x=[20,'JUPI',174,"pooja",143]
del x[-1]
print(x)

x=[20,'JUPI',174,"pooja",143]
remove_element=x.pop(-2)
print(remove_element)
print(x)

numbers = [2, 3, 5, 2, 11, 2, 7]
count=numbers.count(12)
print("count of 12:",count)

numbers = [2, 3, 5, 2, 11, 2, 7]
count=numbers.count(11)
print("count of 11:",count)

numbers = [2, 3, 5, 2, 11, 2, 7]
numbers.sort()
print(numbers)

my_dict = {
  1: "Hello",
  (1, 2): "Hello Hi",
  3: [1, 2, 3]
}

print(my_dict)

my_dict = {
  1: "Hello",
  [1, 2]: "Hello Hi",
}

print(my_dict)

mine_dictionary ={
    "pooja": 20,
    "jupi": 5,
    "alphabets": 26,
    "numebers": "infinity",
}
print(mine_dictionary)
