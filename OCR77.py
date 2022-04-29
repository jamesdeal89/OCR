
def OCR77():
    """what index is the first fibonachi sequence number to have 1000 digits?"""
    fibo = [1,1]
    position = 2
    while True:
        seq = fibo[position-1] + fibo[position-2]
        if len(str(seq)) == 1000:
            print(seq)
            print(position+1)
            input()
        fibo.append(seq)
        position += 1
        print(seq)
OCR77()

"""
teacher solution:
def finonachiSolver(num):
    """"takes a num value is is the index of the fibo number we want. input of 10 will give us the 10th term""""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num > 1:
        return fibonachiSolver(num-1) + fibonachiSolver(num-2)

print(fibonachiSolver(10))
"""