test = int(input())

for ptr in range(test):
    str = input()
    strLen = len(str)

    lenList = []
    strList = []

    lenList.append(strLen)
    strList.append(str)

    alignMax = max(lenList)
print(alignMax)

for secndPtr in range(test):
    print(lenList)
    print(strList)