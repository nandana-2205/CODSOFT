def add(a,b):
    print("The sum is:",a+b)
def sub(a,b):
    print("The difference is:",a-b)
def mul(a,b):
    print("The product is:",a*b)
def div(a,b):
    try:
        print("The quotient is:",a/b)
        print("The remainder is:",a%b)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
while True:
    print("SIMPLE ARITHMATIC OPERATIONS")
    print("-----------------------------")
    print("Select the operation you want to perform")
    print("1.Addition (+)")
    print("2.Subtraction (-)")
    print("3.Multiplication (*)")
    print("4.Division (/ and %) ")
    print("5.End")
    choice=input("Enter your operation choice: ")
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    if choice=='1' or choice=='+':
        add(a,b)
    elif choice=='2' or choice=='-':
        sub(a,b)
    elif choice=='3' or choice=='*':
        mul(a,b)
    elif choice=='4' or choice=='/':
        div(a,b)
    elif choice=='5' or choice.upper()=='END':
        break
    else:
        print("Invalid operation. Please try again. ")
        