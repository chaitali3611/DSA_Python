puramount = int(input("Enter the purchase amount: "))

if(puramount>5000):
    print("20percent discount")
    amount = (20/100)*puramount
    print(f"Total amount is {amount}")
    
elif(2000<puramount<5000):
    print("10percent discount")
    amount = (10/100)*puramount
    print(f"Total amount is {amount}")
    
else:
    print("No discount")
    print(f"Total amount is {puramount}")