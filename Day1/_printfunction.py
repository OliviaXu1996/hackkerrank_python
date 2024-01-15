n = int(input())
def print_str(n):
    if n>=1 and n<=150:
        m = n+1
        for i in range(1, m):
            print(i, end="")
    else:
        print("Invalid input!")

print_str(n)