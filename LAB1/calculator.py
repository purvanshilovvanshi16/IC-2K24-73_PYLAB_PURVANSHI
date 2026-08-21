
x=int(input("enter the value of x: ") )
x=5
match x:
    case 0:
        a=int(input("enter number 1: "))
        b=int(input("enter number 2: "))
        sum=a+b
        print("sum : ",sum)
    case 1:
        a=int(input("enter number 1: "))
        b=int(input("enter number 2: "))
        diff=a-b
        print("difference : ",diff) 
    case 2:
        a=int(input("enter number 1: "))
        b=int(input("enter number 2: "))
        pro=a*b 
        print("product: ",pro) 
    case 3:
        a=int(input("enter number 1: "))
        b=int(input("enter number 2: "))
        div=a/b 
        print("quotient: ",div)
    case 4:
        print("exit")  
        break   
    case _:
            print("Invalid choice! Please try again.")         