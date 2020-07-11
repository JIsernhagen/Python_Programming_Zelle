def toNumbers(strList):
    for i, n in enumerate(strList):
        strList[i] = int(n)
    return strList

def main():
    l = ['1','2','3','4','5','6','7','8','9','10']
    print(toNumbers(l))

main()