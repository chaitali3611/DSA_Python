num1, num2 = map(float, input("Enter two numbers: ").split())

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        sum = num1 + num2
        print(f"Sum is {sum}")
        
    elif choice == "2":
        sub = num1 - num2
        print(f"Subtraction (num1 - num2) is {sub}")
        
    elif choice == "3":
        break
        
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")