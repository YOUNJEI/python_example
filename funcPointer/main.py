def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

if __name__ == '__main__':
    funcList = []

    funcList.append(plus)
    funcList.append(minus)
    funcList.append(mul)

    for func in funcList:
        print(func(10, 20))

