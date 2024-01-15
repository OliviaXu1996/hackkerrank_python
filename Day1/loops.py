
n = int(input())
i = 0

def loops(i, n):
    if n>=1 and n<=20:
        for i in range (n):       
            square = i**2
            print(square)
    else:
        print("invalid input")
        
loops(i, n)