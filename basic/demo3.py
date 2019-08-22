import sys


def str_demo():
    str = 'hello, world!'
    print(len(str))
    print(str.capitalize())
    print(str.upper())
    print(str.lower())
    print(str.find("llo", 0, 5))
    print(str.find("ss"))
    print(str.index("llo"))
    # print(str.index("ss"))  # ValueError: substring not found
    print(str.startswith('he'))
    print(str.endswith('ld'))
    print(str.center(50, '*'))
    print(str.rjust(50, '*'))
    print(str[0:2])
    print(str[0:])
    print(str[:-1])
    print(str[2::2])
    print(str[::2])
    print(str[::-2])  # 这里的负号代表反着切，值代表隔几个字符
    print(str.isalpha())
    print(str.isnumeric())
    print(str.isalnum())
    print(str.strip())


def list_demo():
    list1 = [1, 3, 5, 7, 100]
    print(list1)
    list2 = list1 * 5
    print(list2)
    print(len(list1))
    print(list1[0:2])
    print(list1[0:])
    print(list1[:-1])
    print(list1[1::2])
    print(list1[::-1])

    list1.append(101)
    print(list1)
    list1.insert(1, 2)
    print(list1)
    list1 += [102, 'a']
    print(list1)

    list1.remove(3)
    print(list1)
    if 'a' in list1:
        list1.remove('a')
    print(list1)
    del list1[-1]
    print(list1)
    list1.clear()
    print(list1)


def sort_list():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    print(list2)
    list3 = sorted(list1, reverse=True)
    print(list3)
    list4 = sorted(list1, key=lambda x: len(x))
    # list4 = sorted(list1, key=len)
    print(list4)
    # 给list1发消息，直接在list1上进行排序
    list1.sort(reverse=True)
    print(list1)


def generate_list():
    f = [i for i in range(10)]
    print(f)
    print(type(f))
    f = [x + y for x in 'ABCDE' for y in '12345']
    print(f)
    print(sys.getsizeof(f))
    # 创建生成器对象
    f = (x + y for x in 'ABCDE' for y in '12345')
    print(sys.getsizeof(f))
    list1 = []
    for value in f:  # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
        list1.append(value)
    print(list1)

    list1 = list(range(1, 10))
    print(list1)


def tuple_demo():
    t = ('骆昊', 38, True, '四川成都')
    print(t)
    print(t[-1])
    for item in t:
        print(item)
    # t[0] = 'a'    #TypeError: 'tuple' object does not support item assignment
    # print('a',t[0])

    tuple_list = list(t)
    print(tuple_list)
    tuple_list.append(False)
    print(tuple_list)
    list_tuple = tuple(tuple_list)
    print(list_tuple)


def set_demo():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    set2 = set(range(10))
    print(set2)
    set1.add(3)
    print(set1)
    set1.update([1, 5])
    print(set1)
    set2.discard(1)
    print(set2)
    # set2.remove(1) #KeyError: 1
    if 1 in set2:
        set2.remove(1)
    pop = set2.pop()
    print(pop)
    print(set2)
    set2.add(1)
    print(set2)
    set2.add(10)
    print(set2) # python 中的set 默认是 从小到大排序

    #交集，并集，差集，对称差运算
    set11 = {1,3,5}
    set22 = {2,4,5,6}
    print(set11 & set22)
    print(set11.intersection(set22))
    print(set11) # set11 本身无变化
    print(set11 | set22)
    print(set11.union(set22))
    print(set11 - set22)
    print(set11.difference(set22))
    print(set11 ^ set22)
    print(set11.symmetric_difference(set22))
    #子集，超集
    set33 = {1,5}
    print(set33 < set11)
    print(set33.issubset(set11))
    print(set33 < set33)
    print(set33 <= set33)
    print((set11 | set22) >= set11)

def dict_demo():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(scores)
    print(scores['白元芳'])
    # print(scores['abc']) #KeyError: 'abc'
    print(scores.get('白元芳'))
    print(scores.get('abc'))
    for key in scores:
        print("key:%s,value:%d"% (key,scores[key]))

    scores['白元芳'] = 80
    print(scores)
    scores['python'] = 90
    print(scores)
    print(scores.get('武则天',100))

    scores.pop('骆昊')
    print(scores)
    scores.popitem()
    print(scores)

    scores.clear()
    print(scores)



if __name__ == '__main__':
    str_demo()
    print('===========list demo=============')
    list_demo()
    print('===========sort list=============')
    sort_list()
    print('===========generate_list=============')
    generate_list()
    print('===========tuple_demo=============')
    tuple_demo()
    print('===========set_demo=============')
    set_demo()
    print('===========dict_demo=============')
    dict_demo()
