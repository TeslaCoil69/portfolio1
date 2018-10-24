##get user input, two seperate numbers, making sure that the inputs are both numbers
##get a user operator to perform the task
##run the operation
##check if value is both discernable and reverse solve it
##if good print, if not give error

#setting up variables
ope = "eazy"
oper= "+"
num = 0
num2= 0
q=0
g= 0

def apply_operator():
    if oper == "/":
        return num / num2
    elif oper == "+":
        return num + num2
    elif oper == "-":
        return num - num2
    elif oper == "*":
        return num * num2

def getInput():
    global num
    global num2
    global oper
    num = int(input("Enter a number greater than 1: "))
    num2 = int(input("Enter a number greater than 1: "))
    oper = input("Choose a math operation (+, -, *,/): ")
    if ope == '/' or ope == '*' or ope == '+' or ope == '-' :
        oper = ope
def output(g):
    print(g)   
def operate():
    q= apply_operator()
    print(q)
    return q
def check():
    if g == isinstance(g, int):
        return True
def main():
    getInput()
    g = operate()
    if check()== True:
        output(gwhile 1:
    main()
