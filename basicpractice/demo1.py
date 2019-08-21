"""
有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
"""

def group(list):
    map = {"key1": [], "key2": []}

    for num in list:
        if (num > 66):
            map["key1"].append(num)
        elif (num < 66):
            map["key2"].append(num)

    return map


if __name__ == '__main__':
    list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]

    map = group(list)
    print(map)