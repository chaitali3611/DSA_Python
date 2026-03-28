
balance = int(input("Enter the balance: "))
amount = int(input("Enter the amount: "))

if(amount<=balance):
    print("Transaction successful...")
    print(f"Remaining balane is {balance - amount}")
    
else:
    print("Insufficient Balance")