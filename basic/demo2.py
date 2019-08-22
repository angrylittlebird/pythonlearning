from basic.demo1 import x


def foo():
    a = 1

    def bar(): #函数内部还可以定义函数
        b = 2
        nonlocal a #需要修改嵌套作用中的变量，指定a来自嵌套作用域
        a = 3
        print('a',a) #对于函数bar来说，b处于内置作用域，a处于嵌套作用域中，c处于全局作用域，d处于内置作用域
        print('b',b)
        print('c',c)
        print('d',__name__)


    bar() #需要调用才会执行函数内的函数
    # print(b) NameError: name 'b' is not defined
    print('a',a)


def modify_global_variable():
    global c
    c = 111 # 如果全局作用域中没有变量c，那么c变量将会被赋值后置于全局作用域中


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    x()
    print(__name__)
    c = 100
    foo() #依次搜索从 局部作用域，嵌套作用域，全局作用域，内置作用域中搜索
    modify_global_variable()
    print(c)

# 可执行代码中定义的变量是全局变量，全局变量的生命周期比局部变量的生命周期要长，因而可能会导致对象占用的内存长时间无法垃圾回收
# 而全局变量的作用域及影响过于广泛，很可能导致意料之外的修改、使用，因而应尽量避免全局变量的使用，减少代码耦合，
# 同时这也是对 Low of Demeter （迪米特法则）的践行
# 话说python 中没有 final 关键字吗？
#
# 总之这么写就ok了
# if __name__ == '__main__':
#       main()
# def main():
#       code...
#       pass