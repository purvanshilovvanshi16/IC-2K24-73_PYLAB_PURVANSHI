n = int(input("Enter the number of rows: "))

# Increasing section
for i in range(1, n + 1):
    # Left stars
    for j in range(i):
        print("*", end="")
    
    # Middle spaces
    for j in range(2 * (n - i)):
        print(" ", end="")
    
    # Right stars
    for j in range(i):
        print("*", end="")
    
    print()

# Decreasing section
for i in range(n - 1, 0, -1):
    # Left stars
    for j in range(i):
        print("*", end="")
    
    # Middle spaces
    for j in range(2 * (n - i)):
        print(" ", end="")
    
    # Right stars
    for j in range(i):
        print("*", end="")
    
    print()