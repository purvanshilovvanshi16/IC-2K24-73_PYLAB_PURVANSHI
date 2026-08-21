x = int(input("Enter a number: "))

original = x
digits = len(str(x))
sum = 0

while x> 0:
    digit = x % 10
    sum += digit ** digits
    x //= 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong numbers are:")

for x in range(start, end + 1):
    original = x
    digits = len(str(x))
    total = 0

    while x > 0:
        digit = x % 10
        total += digit ** digits
        x //= 10

    if total == original:
        print(original)    