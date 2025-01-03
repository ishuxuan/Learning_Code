# 作者:胡轩
# 2024年12月28日12时05分56秒
# 1733183066@qq.com
def tuple_practice():
    '''
    元组的一些方法练习
    :return:
    '''
    my_tuple = ('芒果', 2, 4, 2, 8, 2, '小明', 1.78, 140, '早晨')
    print(my_tuple.index('小明'))
    print(len(my_tuple))
    print(my_tuple.count(2))
    print(f'{my_tuple[6]}在{my_tuple[9]}吃了一个{my_tuple[0]}')
    print('%s身高%.2f米，体重%d斤' % my_tuple[6:9])
    print(type((1)))
    print(type((1,)))


def dict_practice():
    '''
    字典的一些方法练习
    :return:
    '''
    my_dict = {'name': '小明'}
    print(my_dict['name'])
    print(id(my_dict))
    my_dict['age'] = 18
    print(id(my_dict))
    print(my_dict)
    my_dict['name'] = '小黄'
    del my_dict['age']
    print(my_dict)
    another_dict = {'age': 20,
                    'height': 1.78}
    my_dict.update(another_dict)
    print(my_dict)
    print(id(my_dict))
    del my_dict['age']
    my_dict.pop('height')
    print(my_dict)
    my_dict.clear()
    print(my_dict)
    print(id(my_dict))
    print('-' * 50)
    xiaoming_dict = {"name": "小明",
                     "qq": "123456",
                     "phone": "10086"}
    # 迭代遍历字典
    # 变量k是每一次循环中，获取到的键值对的key
    for k in xiaoming_dict:
        print(k, xiaoming_dict[k])
    for k, v in xiaoming_dict.items():
        print(f'键 {k},值 {v}')
    for k in xiaoming_dict.keys():
        print(k)
    for v in xiaoming_dict.values():
        print(v)


def str_practice():
    '''
    字符串的一些方法练习
    :return:
    '''
    str1 = ' '
    print(str1.isspace())
    str1 = ''
    print(str1.isspace())
    str2 = 'kjksd123123123'
    print(str2.isalnum())
    print(str2.isalpha())
    print(str2.isdecimal())
    str3 = 'abc'
    print(str3.isalpha())
    print(str3.upper())
    str4 = '1234'
    print(str4.isdecimal())
    print('-' * 50)
    print(str2.find('123'))
    print(str2.find('123', 7))
    str2 = str2.replace('123', '456', 2)
    print(str2)
    print(str2.count('456'))
    print('-' * 50)
    str5 = ' 222\n234\n567\n '
    str5 = str5.strip()
    print(str5)
    print(str5.split('\n'))
    print(str5.splitlines(True))
    print('-' * 50)
    str6 = 'abc\rd'
    str7 = 'abc\n\rd'
    print(str6)
    print(str7)
    str_list = ['1', '2', '3', '4', '5', '6']
    print('$'.join(str_list) + '$')
    print('-' * 50)
    num_str = "0123456789"
    print(num_str[2:6])
    print(num_str[2:])
    print(num_str[:6])
    print(num_str[:])
    print(num_str[::2])
    print(num_str[1::2])
    print(num_str[-1])
    print(num_str[2:-1])
    print(num_str[-2:])
    print(num_str[::-1])


def set_practice():
    set1 = {}
    print(type(set1))
    set2 = set()
    print(set2)
    fruits = {"apple", "banana", "cherry"}
    print(id(fruits))
    fruits.add("orange")
    fruits.add('apple')
    fruits.discard('banana')
    fruits.remove('apple')
    print(id(fruits))
    print(fruits)
    print('-' * 50)
    fruits = {"apple", "banana", "cherry"}
    x = fruits.copy()
    y = fruits
    print(id(x))
    print(id(y))
    print(id(fruits))
    print('-' * 50)
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.difference(y)
    print(f'差集{z}')
    x.difference_update(y)
    print(x)
    x.update(y)
    print(x)
    print('-' * 50)
    x = {"a", "b", "c"}
    y = {"c", "d", "e"}
    z = {"f", "g", "c"}
    result = x.intersection(y, z)  # 返回三个集合的交集
    print(result)
    print('-' * 50)
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.symmetric_difference(y)  # 返回两个集合中不重复元素的集合
    print(z)
    print('-' * 50)
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.union(y)  # 返回两个集合的并集
    print(z)
    print('apple' in z)
    print('-' * 50)
    print(x - y)  # x-xy
    print(x | y)  # x+y
    print(x & y)  # xy
    print(x ^ y)  # x+y-xy


def default_parameter(name, age=6):
    print(name, age)


if __name__ == '__main__':
    # tuple_practice()
    dict_practice()
    # str_practice()
    # set_practice()
    # default_parameter('xiaoming')
    # default_parameter('xiaoming', 10)
