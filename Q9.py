a = float(input("Enter the numerator: "))
b = float(input("Enter the denominator: "))

if b == 0:
    print("Error: Cannot divide by zero")
else:
    result = a / b
    print(f"Result: {result}")