# Program 7: Count number categories

pos = neg = zero = 0

for i in range(5):
    num = int(input("Enter a number: "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1

print("Positive numbers:", pos)
print("Negative numbers:", neg)
print("Zeros:", zero)
