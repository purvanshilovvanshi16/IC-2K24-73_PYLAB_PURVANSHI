while True:
        print("\n 0. Check Armstrong Number")
        print("1. Check Palindrome Number")
        print("2. Print Fibonacci series")
        print("3. Print Pattern ")
        print("4. Print Prime Series")
        print("5. Check Perfect Number")
        print("6. Exit")
        x=int(input("enter your choice"))

        match x:
            case 0:
                print("check a number is Armstrong or not.")
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
            case 1:
                print("check a number is palindrome or not.")
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
            case 2:
                num=int(input("enter the num till series will print: "))
                a=0
                b=1
                for i in range(num):
                    print(a,end=" ")
                    c=a+b
                    a=b
                    b=c
            case 3:
                #right angle triangle
                n=int(input("enter the number of rows: "))
                for i in range(1,n+1):
                    for j in range(i):
                        print("*",end=" ")
                    print( )    

                #number pattern
                n=int(input("enter the number of rows: "))
                for i in range(1,n+1):
                    for j in range(i):
                        print(i,end=" ")
                    print( ) 

                #pyramid
                n=int(input("enter the number of row: "))    
                for i in range(1,n+1):
                    for j in range(n-i):
                        print(" ",end=" ")
                    for k in range(2*i-1):
                        print("*",end=" ")    
                    print()
                        
            case 4:
                x=int(input("enter the num to check prime number: "))
                for i in range (2,x):
                    if x % i==0:
                        print(x,"is not a prime number")
                        break
                    else:
                        print(x,"is a prime number") 
            case 5:
                x =int (input("enter number to check perfect num: "))
                sum=0
                for i in range(1,x):
                    if x % i ==0:
                            sum+=i
                if sum==x:
                    print(x,"is a perfect number")
                else:
                    print(x,"is not a perfect square")    

                s=int(input("enter the starting value"))       
                e=int(input("enter the ending value"))  
                for x in range(s,e):
                    sum=0     

                    for i in range(1,x):
                        if x % i ==0:
                            sum+=i
                    if sum==x:
                        print(x)
            case 6:
                print("press enter to exit")
                break
            
            case _:
                print("Invalid choice! Please enter a number from 1 to 9.")
            
            
            
            
