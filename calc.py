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
opt = input('Please select an option:')
num1 = float(input('please provide num1:'))
num2 = float(input('please provide num2:'))

if opt != '4' or '3' or '2' or '1':
    print("YOU DID NOT CHOOSE A INVALID OPTION!")

elif opt == '1':
    result = num1 + num2
    print("The result is: " + str(result))

elif opt == '2':
    result = num1 - num2
    print("The result is: " + str(result))

elif opt == '3':
    result = num1 * num2
    print("The result is: " + str(result))
    
elif opt == "4" and num2 == 0:
    print("You can not divide a number by zero")
    
else:
    result = num1 / num2
    print("Result is: " + str(result))

