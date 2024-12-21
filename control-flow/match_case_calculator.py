num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2 
    case "*":
        result =  num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")   
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.") 

print ("The result is:",result)                