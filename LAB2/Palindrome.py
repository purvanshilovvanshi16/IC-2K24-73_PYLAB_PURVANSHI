num=int(input("enter the number to check: "))
original_num=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if original_num==reverse:
    print("the number is palindrome")
else:
    print("the number is not a palindrome number")        

 #program for checking a string is a palindrome or not 

s = input("Enter a string: ")

reverse = ""

for i in range(len(s) - 1, -1, -1):
    reverse += s[i]

if s == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")