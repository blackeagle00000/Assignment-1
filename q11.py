name = input("Enter your name: ")
age = input("Enter your age (press Enter to skip): ")

if age == "":
    age = 25
else:
    age = int(age)

print("Hello, " + name + "! You are " + str(age) + " years old.")