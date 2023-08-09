#pattern ex 1
n = 10
for i in range(0, n):
	for j in range(0, i+1):
		print("*", end=" ")
	print()
n = 10
for i in range(0, n):
	for j in range(0, n-i):
		print("*", end=" ")
	print()

#pattern ex 2
x = int(input("Enter number of rows: "))

for i in range(x):
    for j in range(i+1):
        print("* ", end="")
    print()

#pattern ex 3
x = int(input("Enter number of rows: "))
for i in range(x):
    for j in range(i+1):
        print(j+1, end=" ")
    print()