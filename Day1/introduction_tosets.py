def average(array):
    # your code goes here
    mylist = list(dict.fromkeys(array))
    sum_list = sum(mylist)
    res = sum_list / (len(mylist))
    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)