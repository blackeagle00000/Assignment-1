n = [45, 455, 66, 777, 7778, 676]

if n[0] >= n[1] and n[0] >= n[2] and n[0] >= n[3] and n[0] >= n[4] and n[0] >= n[5]:
    result = n[0]
elif n[1] >= n[0] and n[1] >= n[2] and n[1] >= n[3] and n[1] >= n[4] and n[1] >= n[5]:
    result = n[1]
elif n[2] >= n[0] and n[2] >= n[1] and n[2] >= n[3] and n[2] >= n[4] and n[2] >= n[5]:
    result = n[2]
elif n[3] >= n[0] and n[3] >= n[1] and n[3] >= n[2] and n[3] >= n[4] and n[3] >= n[5]:
    result = n[3]
elif n[4] >= n[0] and n[4] >= n[1] and n[4] >= n[2] and n[4] >= n[3] and n[4] >= n[5]:
    result = n[4]
else:
    result = n[5]

print("Maximum value is:", result)