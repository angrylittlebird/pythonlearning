"""
# 题目二：
# 查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
"""


def find(target):
    ret: list = []
    if (type(target) == list or type(target) == tuple):
        temp_tuple = list(target)
        for i in range(len(target)):
            temp_tuple[i] = target[i].strip()
            if (temp_tuple[i].capitalize().startswith("A") and temp_tuple[i].endswith("c")):
                ret.append(temp_tuple[i])
    elif (type(target) == dict):
        for item in target.values():
            item = item.strip()
            if (item.capitalize().startswith("A") and item.endswith("c")):
                ret.append(item)

    return ret


if __name__ == '__main__':
    li = ["alec", " aric", "Alex", "Tony", "rain"]
    tu = ("alec", " aric", "Alex", "Tony", "rain")
    dic = {'k1': "alec", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

    ret1 = find(li)
    print(ret1)
    ret2 = find(tu)
    print(ret2)
    ret3 = find(dic)
    print(ret3)
