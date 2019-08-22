class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age, gender='男'):
        self.name = name
        self.age = age
        self.__gender = gender

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


def main():
    student = Student('小明', 20)
    print(student.name, ':', student.age)
    student.study("python")
    student.watch_movie()

    student2 = Student('小丁', 17, '男')
    # Python并没有从语法上严格保证私有属性或方法的私密性，
    # 它只是给私有的属性和方法换了一个名字来“妨碍”对它们的访问，
    # 事实上如果你知道更换名字的规则仍然可以访问到它们，
    print(student2._Student__gender)


if __name__ == '__main__':
    main()
