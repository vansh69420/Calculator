from art import logo
#Addition
def add(n1,n2):
    return n1 + n2

#subtract
def sub(n1,n2):
    return n1 - n2


#Multiply
def mult(n1,n2):
    return n1 * n2

#Division 
def div(n1,n2):
    return n1 // n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : div
}
def calculator():
    print(logo)
    num1 = float(input("Enter the first number : "))
    
    
    for symbol in operations:
        print(symbol)
    
    continue_solution = True
    while continue_solution:
        
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("Enter the second number : "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        if input(f"Type 'y' to continue with {answer}, or 'n' to start the new calculator : ") == 'y':
            num1 = answer
        else:
            continue_solution = False
            
            calculator()

calculator()
            
        

        
