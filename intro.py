print("hello world")

#comment line

#create variable
name = "Aaron"
last_name='Pride'
age = 31
total = 60.12
found = False


# print each variable, save and run script

print(name)
print(last_name)
print(age)
print(total)
print(found)

#concatinate

print(name+' '+last_name)

#math
print(1+2)
print(2*3)
print(4-5)
print(5/6)

# error
# print('name'+2)  can not combine string and number

# conditional statment (if else elif or and not statmnet)

if age > 100:
    print('you are not 100 years old yet keep going!')
    #print('inside the if')
#print('im outside the if statment') 
elif age == 100:
    print('you are a century old!')
else:
    print('bought that time')

#functions

def say_hello():
    print('hello there')

def say_hi(name):
    print('hi ' + name)

def get_day():
    return "monday"

#call function
say_hello()
say_hi(name+last_name)

day = get_day()
print('today is ' + day)

