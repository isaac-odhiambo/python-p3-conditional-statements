#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower()== 'admin' and password == '12345':
                return 'Access granted'
    else:
        return 'Access denied'
    
   

def hows_the_weather(temperature):
    if temperature <= 33:
        return "It's brisk out there!"
    elif 33 <= temperature <= 55:
        return "It's a little chilly out there!"
    elif 55 <= temperature <= 75:
        return "It's perfect out there!"
    elif 65 <= temperature <= 85:
        return "It's getting warm out there."
    else:  # For temperatures above 90
        return "It's too dang hot out there!"
    
    



    

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    pass

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:  # Check to avoid division by zero
            return num1 / num2
        else:
            print ("Error: Division by zero!")
            return None
    else:
        print ("Invalid operation!")
        return None
    
    