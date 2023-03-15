# imports



# global vars



# functions

def print_menu():
    spacer = "-----------------"
    print(spacer)
    print('Calc 3000')
    print(spacer)
    print('[1] sum two numbers')
    print('[2] subtract two numbers')
    print('[3] multipy two numbers')
    print('[4] divide two numbers')

# plain instruction
print_menu()

opt = input("Please select an option: ")

if opt not in ('4' ,'3' ,'2' ,'1'):
    print("Invalid option")

else:
    num1 = float(input("Please choose first number: "))
    num2 = float(input("Please choose second number: "))

    if opt == '1':
        result = num1 + num2
        print("Result is: " + str(result))

    elif opt == '2':
        result = num1 - num2
        print("Result is: " + str(result))

    elif opt == '3':
        result = num1 * num2
        print("Result is: " + str(result))

    elif opt == '4':
        
        if num2 == 0:
            print("You cannot divide by zero!")

        else:
            result = num1 / num2
            print("Result is: " + str(result))
