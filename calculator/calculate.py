import math as mt
def add(number1, number2):
    return  number1 + number2
def subtract(number1, number2):
    return(number1, number2)
def multiplication(number1, number2):
    return number1 * number2

def main():
    while True:
        print("\nSelect: \n1. For addition\n2.For subtraction\n3. For multiplication\n0.To exit")
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
        elif choice == 0:
            break
    
if __name__ == '__main__':
    main()