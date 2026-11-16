import math

print('Yashika Bhargava')
print('o-----')
print(' ||||')
print('*' * 10)

patient_name = 'John Smith'
patient_age = 20
is_new_patient = True


name = input('What is your name? ')
color = input('What is your favorite color?')

print (name + ' Likes ' + color )


weight = input('Enter your weight(In Pounds): ')
weight_in_kg = float(weight) * 0.45359237

print('Your weight in kgs is: ' + str(weight_in_kg))


# formatted Strings

first_name = 'Yashika'
last_name = 'Bhargava'
msg = f'{first_name} [{last_name}]'
print(msg)
print(len(first_name))
print(first_name.lower())
print(first_name.upper())
print(first_name.title())
print(first_name.find('a'))
print(first_name.replace('a', 'A'))
print('ashi' in first_name)

# A function is generic meaning it doesn't belong to a particular object, wherin
# functions that belongs to a particular object are called methods (eg. upper(), lower() etc are methods used for string object)


# Arithmetic operators
x = 10
x **= 3  # exponentiation has highest precedence
print(x)

x /= 4 # this returns the output of float type
print(x)

x /= 4 # this returns the output of int type
print(x)

x *= 3
print(x)

x = x + 3
print(x)

x -= 3
print(x)


# Math Functions

x = 2.9
y = -9.8
print(round(x))  #Rounds off the number
print(abs(y)) # Returns the positive absolute number

print(math.floor(x))
print(math.ceil(x))





