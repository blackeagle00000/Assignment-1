text = input("Enter a string: ")
count = 0

for i in text:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' \
    or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        count = count + 1

print("Number of vowels:", count)