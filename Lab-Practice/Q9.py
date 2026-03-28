salary = float(input("Enter your salary: "))
creditscore = int(input("Enter your credit score: "))

if salary>25000 and creditscore >700:
    print("Eligible for loan")
    
else:
    print("Not eligible for loan")