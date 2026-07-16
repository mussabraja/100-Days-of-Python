import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2

#TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"


operations = {
    "+": add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    n1 = int(input("Insert first number "))
    operation = input("What operation you want to perform?'\n' + '\n' - '\n' * '\n' / ' \n")
    n2 = int(input("Insert second number "))

    n3 = operations[operation](n1, n2)
    print(n3)

    previous_result = True
    while previous_result:
        previous_result = input("Do you want to continue with previous result").lower()
        if previous_result == 'no':
            previous_result = False
            calculator()
            return
        new_number = int(input("insert a number"))
        operation = input("What operation you want to perform?'\n' + '\n' - '\n' * '\n' / ' \n")
        n3 = operations[operation](n3,new_number)
        print(n3)

calculator()
