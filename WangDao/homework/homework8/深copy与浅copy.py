# 作者:胡轩
# 2025年01月05日22时44分47秒
# 1733183066@qq.com
import copy


def list_copy():
    ls1 = [1, 2, 3]
    ls2 = ls1
    ls3 = ls1.copy()
    ls1[0] = 4
    print(ls2)
    print(ls3)
    print(id(ls1))
    print(id(ls2))
    print(id(ls3))


def copy_copy():
    # 列表自带的copy方法与copy类中的copy方法效果一样
    ls1 = [1, 2, 3]
    ls2 = copy.copy(ls1)
    ls1[0] = 4
    print(ls2)
    print(id(ls1))
    print(id(ls2))
    print('-' * 50)
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    a[0] = 5
    b[0] = 6
    print(c)
    print(d)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))


def copy_deepcopy():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    a[0] = 5
    b[0] = 6
    print(c)
    print(d)
    print(id(c[0]), id(c[1]))
    print(id(d[0]), id(d[1]))
    print('-'*50)
    class Student:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            self.subject=['语文','数学','英语']
        def __str__(self):
            return f'name:{self.name},age:{self.age},subject:{self.subject}'
    student1=Student('张三',18)
    student2=copy.deepcopy(student1)
    student3=copy.copy(student1)
    student2.age=20
    student2.subject.append('物理')
    student3.age=22
    student3.subject.append('化学')
    print(student1)
    print(student2)
    print(student3)

if __name__ == '__main__':
    # list_copy()
    # copy_copy()
    copy_deepcopy()
