# 作者:胡轩
# 2024年12月30日01时13分53秒
# 1733183066@qq.com

# 1、多个缺省参数的传递练习，练习多个缺省参数

def lack_argument(wage, name='张三', age='18', position='', insurance=True):
    if not insurance:
        wage += 500
    print(f'{position}{name}的年龄是{age},工资是{wage}')


lack_argument(6000, '李四')
lack_argument(8000, position='店长')
lack_argument(9000, insurance=False)
print('-' * 50)


# 2、多值参数练习，元组，字典的传参拆包练习
def another_func(*args, **kwargs):
    print('-' * 50)
    print(args)
    print(kwargs)


def mutiargu_unpack(*args, word, **kwargs):
    print(word)
    print(args)
    print(*args)
    print(kwargs)
    # print(**kwargs)
    another_func(*args, 'this is more info', **kwargs, lastmame='sss')


mutiargu_unpack('helloworld', 1, 2, 3, 4, word='', name='hh', age=22, surname='h')
print('-' * 50)
mutiargu_unpack(1, 2, 3, 4, word='helloworld', name='sda')


# 3.设计一个类，实例化1个对象，会实现下面两种行为
# 需求
# •一只 黄颜色 的 狗狗 叫 大黄
# •具有  汪汪叫 行为
# •具有  摇尾巴 行为

class dog():
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def bark(self):
        print(f'{self.color}的{self.name}正在汪汪叫')

    def welcome(self):
        print(f'{self.color}的{self.name}正在摇尾巴')


dog1 = dog('黄色', '大黄')
print(dir(dog))
dog1.bark()
dog1.welcome()
