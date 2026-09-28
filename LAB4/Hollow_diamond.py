n = int(input("Enter an odd number: "))

for i in range(n // 2 + 1):
    spaces = n // 2 - i
    stars = 2 * i + 1

    print(" " * spaces, end="")

    if stars == 1:
        print("*")
    else:
        print("*" + " " * (stars - 2) + "*")

for i in range(n // 2 - 1, -1, -1):
    spaces = n // 2 - i
    stars = 2 * i + 1

    print(" " * spaces, end="")

    if stars == 1:
        print("*")
    else:
        print("*" + " " * (stars - 2) + "*")