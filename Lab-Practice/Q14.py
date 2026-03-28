# Simple while loop version
num = int(input("Enter a number: "))
factorial = 1
temp = num

while num > 0:
    factorial *= num
    num -= 1

print(f"{temp}! = {factorial}")