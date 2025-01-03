# 作者:胡轩
# 2025年01月03日17时18分08秒
# 1733183066@qq.com
list1 = 'Life is short,you need Python'.split(',')
list2 = [i.split(' ') for i in list1]
my_list = [i for j in list2 for i in j]
print(my_list)

print(sorted(my_list))
print(my_list)
my_list.sort()
print(my_list)


def change_lower(word):
    return word.lower()


# my_list.sort(key=change_lower)
my_list.sort(key=lambda x: x.lower())
print(my_list)
print('-' * 50)

student_tuples = [
    ('jane', 'B', 12),
    ('john', 'A', 15),
    ('dave', 'B', 10),
]

print(sorted(student_tuples, key=lambda x: x[2]))
print('-' * 50)
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__来说，更方便，可以返回非字符串类型
        :return:
        """
        return repr((self.name, self.grade, self.age))


student = Student('john', 'A', 15)
print(student)
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print(sorted(student_objects,key=lambda student:student.age))
print('-' * 50)
from operator import itemgetter, attrgetter
# itemgetter一般用于元组，列表（取下标）。attrgetter一般用于对象（取属性）
print('使用operator系列')
print(sorted(student_tuples, key=itemgetter(0)))
print(sorted(student_objects,key=attrgetter('age')))
print('使用operator系列,多列排序')
print(sorted(student_tuples, key=itemgetter(1,2)))
print(sorted(student_tuples, key=lambda x: (x[1],-x[2]))) #第一列升序，第二列降序
print(sorted(student_objects, key=attrgetter('grade', 'age'),reverse=True))

print('查看排序稳定性')
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data, key=lambda x:x[0]))

mydict = { 'Li'   : ['M',7],
           'Zhang': ['E',2],
           'Wang' : ['P',3],
           'Du'   : ['C',2],
           'Ma'   : ['C',9],
           'Zhe'  : ['H',7] }

print(sorted(mydict.items(),key=lambda x:x[1][1]))