# Take two number from the user, store them in variables x and y respectively.
# Swap the values present inside x and y and display the results

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

num1 = x
x = y
y = num1

print(x)
print(y)