
passcode = "chaishu"

for i in range (1, 4):
    password = input("Enter password: ")
    if password==passcode:
        print("Access Granted")
        break
    else:
        print("Access Denied")