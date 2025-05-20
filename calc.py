def add ( num1, num2):
    return num1 + num2
def subtract( num1, num2):
    return num1- num2
def multiply (num1 , num2):
    return num1*num2
def divide (num1, num2):
    return num1/num2
num1 = input ('first no. : ')
num2 = input('second no. : ')
operation =input ('enter operation')

if operation == 'add':
    print (add(num1, num2))

elif operation =='subtract':
    print(subtract(num1, num2))
elif operation == 'multiply':
    print (multiply (num1, num2))
elif operation == 'divide':
    print (divide (num1, num2))
else :
    print ('Invalid input')