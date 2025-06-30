num = int(input("Enter a number: "))
temp_num = num

while temp_num > 10:
    total = 0
    while temp_num > 0:
        digit = temp_num % 10
        total += digit ** 2
        temp_num = temp_num // 10
    temp_num = total

if temp_num == 1:
    print("The number is a happy number.")
else:
    print("The number is not a happy number.")









