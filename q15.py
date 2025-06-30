num=int(input("Enter number of layers: "))
for i in range(1, num+1):
    a="  "*(num-i)
    b="* "*(2*i-1)
    print(a + b)