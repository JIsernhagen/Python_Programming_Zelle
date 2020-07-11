def sumList(num):
    s=0
    for n in num:
       s+=n
    return s

def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sumList(l))

main()