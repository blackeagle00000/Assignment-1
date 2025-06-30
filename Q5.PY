def fibonacci():
    a = 0
    b = 1
    for _ in range(10):
        print(a)
        temp = a
        a = b
        b = temp + b

# Call the function
fibonacci()