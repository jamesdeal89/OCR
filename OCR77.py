
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
    