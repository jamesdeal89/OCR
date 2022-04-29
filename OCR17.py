def OCR17():
    """Write a program that takes a symbol (+,-,* or /) and a natural number (>0) 
    and makes a table like below for the operation from 0 to n"""
    while True:
        operator = input("what operator?:")
        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            while True:
                try:
                    number = int(input("up to what number?:"))
                except (TypeError, ValueError):
                    print("please input only digits")
        else:
            print("please enter only +,-,* or /")

OCR17()