# Program 6: Check positive, negative, or zero

for i in range(5):
    num = int(input("Enter a number: "))
    if num > 0:
        print(num, "is Positive")
    elif num < 0:
        print(num, "is Negative")
    else:
        print(num, "is Zero")
