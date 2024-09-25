number1 = int(input("Enter first number: "))
number2 = int(input("Enter the second number: "))
choice = int(input("Enter Your Choice \n 1.Addition\n 2.Substraction\n 3.Multiplication \n 4.Division\n"))

if choice == 1:
    result = number1 + number2
    print(result)

elif choice == 2:
    result = number1 - number2
    print(result)

elif choice == 3:
    result = number1 * number2
    print(result)

elif choice == 4:
    result = number1 / number2
    print(result)

else:
    print("Invalid Choice")

