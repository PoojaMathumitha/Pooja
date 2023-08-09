name="POOJA MATHUMITHA"
print(name)

#assigning string characters in python
hey="welcome"
print(hey[2])

hey="welcome"
print(hey[-2])

hey="welcome"
print(hey[1:6])

#check whether it is immutable
#hey="welcome"
#hey[1]="o"
#print(hey)

#can change the variable
hey="welcome"
hey="welcome guys"
print(hey)

#making quotes
hey="""welcome you fo this occation
Have a wonderful moment together"""
print(hey)

#compare two strings
hey ="welcome"
hello ="how are you"
hi ="welcome"
print(hey==hi)
print(hey==hello)

#join two strings
hey ="hello "
hi ="everyone"
result =hey+hi
print(result)

#iterate
hey ="welcome"
for letter in hey:
    print(letter)

#count the string
hey ="welcome all"
print(len(hey))

#check whether it is or not
print('at' in 'battle')

print("po" in "jupiter")

#find operation
hey ="welcome you all"
capitalize_string=hey.capitalize()
print(capitalize_string)
