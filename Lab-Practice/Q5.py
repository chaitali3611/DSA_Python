units = int(input("Enter the electricity units: "))

if 0<=units<=100: 
    print("Rate of the unit is 5rs: ")
    bill = units * 5
    print(f"Total electricity bill is {bill}")
    
elif 100<units<=200:
    print("Rate of the unit is 7rs: ")
    bill = units * 7
    print(f"Total electricity bill is {bill}")
    
else:
    print("Rate of the unit is 10rs: ")
    bill = units * 10
    print(f"Total electricity bill is {bill}")
