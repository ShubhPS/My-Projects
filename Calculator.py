import math
import random
import stat

answer = 0

def addition(x,y):
    answer = x + y
    print(f"{x}+{y} = {answer}")
def subtraction(x,y):
    answer = x - y
    print(f"={x}-{y} = {answer}")

def multiplication(x,y):
    answer = x * y
    print(f"{x}x{y} = {answer}")

def division(x,y):
    answer = x / y
    print(f"{x}/{y} = {answer}")

def exponent(x,y):
    answer = x ** y
    print(f"{x}^{y} = {answer}")

def absoluten(x):
    answer = abs(x)
    print(f"Absolute value of {x} = {answer}")

def fibonacci(x):
    a = 0
    b = 1
    if x < 0:
        print("Incorrect Input")
    elif x == 0:
        answer = a
    elif x == 1:
        answer = b
    else:
        for i in range(2, x+1):
            c = a + b
            a = b
            b = c
            answer = b

    print(f"The {x} term in Fibonacci Sequence = {answer}")
def armstrong(x):
    n = len(str(x))
    c = x
    arm = 0
    while (c > 0):
        a = int(c%10)
        arm += a**n
        c //= 10
    if(x==arm):
        print(f"{x} is an Armstrong Number")
    else:
        print(f"{x} is not an Armstrong Number")


def palindrome(x):
    y = str(x)[::-1]
    if(str(x) == y):
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

def randomisedfun(x,y):
    print("Fuck")


print(''' ▄████████    ▄████████  ▄█        ▄████████ ███    █▄   ▄█          ▄████████     ███      ▄██████▄     ▄████████
███    ███   ███    ███ ███       ███    ███ ███    ███ ███         ███    ███ ▀█████████▄ ███    ███   ███    ███
███    █▀    ███    ███ ███       ███    █▀  ███    ███ ███         ███    ███    ▀███▀▀██ ███    ███   ███    ███
███          ███    ███ ███       ███        ███    ███ ███         ███    ███     ███   ▀ ███    ███  ▄███▄▄▄▄██▀
███        ▀███████████ ███       ███        ███    ███ ███       ▀███████████     ███     ███    ███ ▀▀███▀▀▀▀▀  
███    █▄    ███    ███ ███       ███    █▄  ███    ███ ███         ███    ███     ███     ███    ███ ▀███████████
███    ███   ███    ███ ███▌    ▄ ███    ███ ███    ███ ███▌    ▄   ███    ███     ███     ███    ███   ███    ███
████████▀    ███    █▀  █████▄▄██ ████████▀  ████████▀  █████▄▄██   ███    █▀     ▄████▀    ▀██████▀    ███    ███
                        ▀                               ▀                                               ███    ████''')
should_end = False
while not should_end:
    print("\n\nOperation List: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponent\n6. Absolute value"
          "\n7. Fibonacci Sequence\n8. Armstrong Number\n9. Palindrome Number\n10. Random Bullshit!")
    choice = int(input("What do you want to perform? (Type number next to the operation) : \n"))


    if (choice==1): x =float(input("x : ")); y =float(input("y : ")) ; addition(x,y)
    elif (choice == 2): x =float(input("x : ")); y =float(input("y : ")) ; subtraction(x,y)
    elif (choice == 3): x =float(input("x : ")); y =float(input("y : ")) ; multiplication(x,y)
    elif (choice == 4): x =float(input("x : ")); y =float(input("y : ")) ; division(x,y)
    elif (choice == 5): x =float(input("x : ")); y = int(input("Power Of : ")) ; exponent(x,y)
    elif (choice == 6): x =float(input("x : ")); absoluten(x)
    elif (choice == 7): x = int(input("Which term of Sequence do you want to find : ")); fibonacci(x)
    elif (choice == 8): x = int(input("x : ")); armstrong(x)
    elif (choice == 9): x = int(input("x : ")); palindrome(x)
    elif (choice == 10): x = input("Minimum limit : "); y = input("Maximum limit : ") ; randomisedfun(x,y)


    else:
        print("Wrong input")


    cont = input("Do you want to continue? Yes or No : \n").lower()
    if cont == "no":
        should_end = True
        print("THANK YOU!!")