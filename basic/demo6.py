def value_type():
    # 值类型不可变
    a = 1
    aa = a
    b = 'str'
    bb = b
    c = (1, 2)
    cc = c
    print("int".center(10, '*'))
    print(a, id(a))
    a += 1
    print(a, id(a))
    print(aa, id(aa))
    print("is", a is aa)

    print("str".center(10, '*'))
    print(b, id(b))
    b = 'str' * 2
    print(b, id(b))
    print(bb, id(bb))

    print("tuple".center(10, '*'))
    print(c, id(c))
    c *= 2
    print(c, id(c))
    print(cc, id(cc))


def reference_type():
    list = [1, 3]
    listlist = list
    set = {1, 2}
    setset = set
    dict = {"a": 1}
    dictdict = dict

    print("list".center(10, '*'))
    print(list, id(list))
    list *= 2  # 这里的id为发生变化，说明内部并不是 走的 list = list * 2 的逻辑，很有可能是走的 list += list 的逻辑吧。
    #  至少可以确定 这种+=,*=简化的写法都是直接在当前内存地址中操作
    print(list, id(list))
    list = list * 2  # 这里的id发生了变化，倒是符合逻辑
    print(list, id(list))
    print(listlist, id(listlist))

    print("set".center(10, '*'))
    print(set, id(set))
    set.remove(1)
    print(set, id(set))
    print(setset, id(setset))
    print(set is setset)

    print("dict".center(10, '*'))
    print(dict, id(dict))
    dict.clear()
    print(dict, id(dict))
    print(dictdict, id(dictdict))


def is_demo():
    set1 = {1, 2, 3}
    set2 = {1, 3, 3, 2}
    print("==", set1 == set2) # set 本来就是无序的
    print("is", set1 is set2)

    tuple1 = (1,2,3)
    tuple2 = (1,3,2)
    print("==",tuple1 == tuple2)
    print("is",tuple1 is tuple2)


def for_else_demo():
    a = [['apple','orange','banana','grape'],(1,2,3)]
    for x in a:
        for y in x:
            print(y,end=' ')
        print()
    else:
        print("all is done.")


def main():
    value_type()
    reference_type()
    # 其实引用类型和值类型外在的特质就是：当两个值类型的变量指向同一内存地址的时候，其中一个值类型的变量被赋予新的值并不会影响另一个变量的变化，
    # 而在两个指向相同地址的引用类型变量中修改其中一个变量的某些值，那么另一个引用类型的变量值也相应改变
    # 原因：值类型的变量是不可变的，当值类型的变量发生改变时，其实是让该变量指向了新的内存地址，而非改变该内存地址中的值，
    # 而引用类型的变量是可变的，即当改变该变量中的某些值的时候，修改的就是该变量所指向的内存地址中的值（当然如果变量整体进行赋值操作，那么就会指向内存中的其它地址了）
    is_demo()
    for_else_demo()



if __name__ == '__main__':
    main()
