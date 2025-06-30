numbers = [10, 3, 5, 7, 2, 9, 8, 4]
target = int(input("Enter a target number: "))

for first in numbers:
    second = target - first
    if second in numbers and second != first:
        print(f"The target {target} is the sum of {first} and {second}.")
        break