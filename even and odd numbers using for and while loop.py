# Program 5: Even and Odd numbers using for and while

print("Using for loop:")
for i in range(1, 101):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

print("\nUsing while loop:")
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
    i += 1
