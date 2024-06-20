import math as mt
def add(number1, number2):
    return  number1 + number2
def subtract(number1, number2):
    return(number1, number2)
def multiplication(number1, number2):
    return number1 * number2
def division(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return 'Division by Zero not allowed!'
def square(number):
    return number ** 2

def squareroot(number):
    return mt.sqrt(number)


def main():
    while True:
        print("\nSelect: \n1. For addition\n2.For subtraction\n3. For multiplication\n0.To exit")
        print("4.For Division\n5.For square\n6.For square root")
        choice = int(input("Choice: "))
        if choice == 1:
            num1 = int(input("Enter the first number: "))
            num2 = int(input('Enter the second number: '))
            print(f"The sum of {num1} and {num2} = {add(num1, num2)}")
        elif choice == 2:
            num1 = int(input("Enter the first number: "))
            num2 = int(input('Enter the second number: '))
            print(f"The difference of {num1} and {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            num1 = int(input("Enter the first number: "))
            num2 = int(input('Enter the second number: '))
            print(f"\n**The product of {num1} and {num2} = {multiplication(num1, num2)}")
        elif choice == 4:
            num1 = int(input("Enter the first number: "))
            num2 = int(input('Enter the second number: '))
            print(f"\n**The division of {num1} and {num2} = {division(num1, num2)}")
        elif choice == 5:
            num = int(input('Enter a number to get the square: '))
            print(f'The square of {num} = {square(num)}')

        elif choice == 0:
            break
    
if __name__ == '__main__':
    main()