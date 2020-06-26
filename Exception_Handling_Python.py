import sys

def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Please enter a valid number")
        except EOFError:
            sys.exit(0)
        except Exception:   # this could be "except:" -> This is wildcard exception, and catches any kind of exception.
            print("This catches all the exceptions so should be placed at the end of the exception blocks.")
        finally:
            print("This always executes")

Status = True
while Status:

    number1 = getint("Please enter first number: ")
    number2 = getint("Please enter second number: ")

    try:
        print("{} divided bytes {} is {}".format(number1,number2,number1/number2))
        Status = False
    except ZeroDivisionError:
        print("Can not divide by zero")
    else:
        print("Division performed successfully")



'''def factorial(n):
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)


    try:
        print(factorial(1233))
    except RecursionError:
        print("Please use smaller number")
    
    print("Program Terminating")'''