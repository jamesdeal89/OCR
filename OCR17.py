import operator

def OCR17():
    """Write a program that takes a symbol (+,-,* or /) and a natural number (>0) 
    and makes a table like below for the operation from 0 to n"""
    def findOp(string):
        if string == "+":
            return operator.add
        elif string == "-":
            return operator.sub
        elif string == "*":
            return operator.mul
        elif string == "/":
            return operator.div

    while True:
        table = []
        method = input("what method?:")
        if method == "+" or method == "-" or method == "*" or method == "/":
            while True:
                try:
                    number = int(input("up to what number?:"))
                except (TypeError, ValueError):
                    print("please input only digits")
                else:
                    for value1 in range(number):
                        for value2 in range(number):
                            table.append(findOp(method)(value1, value2))
                    print(table)
                        

        else:
            print("please enter only +,-,* or /")

OCR17()