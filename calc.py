# imports



# global vars



# functions

def print_menu():
    spacer = "-----------------"
    print(spacer)
    print('Calc 3000')
    print(spacer)
    print('[+] sum two numbers')
    print('[-] subtract two numbers')
    print('[*] multipy two numbers')
    print('[/] divide two numbers')

# plain instruction
print_menu()

num1 = float(input("Please choose first number: "))
opt = input("Please select an option: ")
num2 = float(input("Please choose second number: "))

if opt not in ('+' ,'-' ,'*' ,'/'):
    print("INVALID OPTION!")

else:

    if opt == '+':
        result = num1 + num2
        print("Result is: " + str(result))

    elif opt == '-':
        result = num1 - num2
        print("Result is: " + str(result))

    elif opt == '*':
        result = num1 * num2
        print("Result is: " + str(result))

    elif opt == '/':
        
        if num2 == 0:
            print("YOU CANNOT DIVIDE BY ZERO!")

        else:
            result = num1 / num2
            print("Result is: " + str(result))
