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
    print(str[::-2]) # 这里的负号代表反着切，值代表隔几个字符
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
    list1.insert(1,2)
    print(list1)
    list1 += [102,'a']
    print(list1)
    



if __name__ == '__main__':
    str_demo()
    list_demo()
