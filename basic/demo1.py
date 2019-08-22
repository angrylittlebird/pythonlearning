def x():
    pass

def variable_type():
    a: int = 1
    b: float = 1.1
    c: str = "abc"
    d: bool = False
    print(a, b, c, d)


def operation():
    a = 321
    b = 123
    c = False
    print(a / b)
    print(a // b)
    print(a * b)
    print(a ** b)
    print(c is False)
    print(a is 321)
    print(0 and 10)
    print(3 and 5)


def testSomeThing():
    a = input('a= ')
    print('type', type(a))
    print('type', type(int(a)))


def testForIn():
    for i in range(1, 9):
        print(i)
    for i in range(1, 9, 3):
        print(i)


def ninenine():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d*%d=%d ' % (j, i, i * j), end='\t')
        print()


def printTriangle(row: int):
    for i in range(row):
        for _ in range(0, i + 1):
            print('*', end='')
        print()

    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(' ', end='')
            else:
                print('*', end='')
        print()

    total_item_count = 2 * row - 1
    for i in range(row):
        cur_row_stars = 2 * i + 1
        start_print_stars = (total_item_count - cur_row_stars) / 2
        for j in range(total_item_count):
            if j >= start_print_stars and j < start_print_stars + cur_row_stars:
                print('*', end='')
            else:
                print(' ', end='')
        print()


# 这里的 if 分支本身也是可执行代码，只不过加了个if条件
if __name__ == '__main__':
    variable_type()
    operation()
    # testSomeThing()
    testForIn()
    ninenine()
    printTriangle(4)

# 可执行代码块，在导入时会直接执行
if __name__:
    print(__name__)
else:
    pass
