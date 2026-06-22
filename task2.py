def add():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("The sum is:",a+b)
def sub():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("The difference is:",a-b)
def mul():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("The product is:",a*b)
def div():
    try:
        a=int(input("Enter first number:"))
        b=int(input("Enter second number:"))
        print("The quotient is:",a/b)
        print("The remainder is:",a%b)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
while True:
    print("SIMPLE ARITHMATIC OPERATIONS")
    print("______________________________")
    print("Select the operation you want to perform")
    print("1.Addition - +")
    print("2.Subtraction - -")
    print("3.Multiplication - *")
    print("4.Division - / and %")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mul()
    elif choice==4:
        div()
    elif choice==5:
        break
    else:
        print("Invalid choice")
        