# Simple version
total = 0
count = 0

print("Enter item prices (enter 0 to stop):")

while True:
    price = float(input(f"Item {count + 1}: ₹"))
    
    if price == 0:
        break
    
    total += price
    count += 1

print(f"\nTotal items: {count}")
print(f"Total bill: ₹{total:.2f}")