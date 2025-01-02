# 作者:胡轩
# 2024年12月26日11时21分01秒
# 1733183066@qq.com

# 1.有7个整数，其中有3个数出现了两次，1个数出现了一次， 找出出现了一次的那个数。
ls = [6, 5, 6, 3, 5]
res = 0
for i in ls:
    res = res ^ i  # 异或满足交换律
print(res)
print('-' * 50)

# 2.写一个简单的for循环，从1打印到20，横着打为1排
for i in range(1, 21):
    print(i, end=' ')

print('')
print('-' * 50)


# 3.写一个say_hello函数打印多次hello并给该函数加备注（具体打印几次依靠传递的参数），然后调用say_hello，同时学会快速查看函数备注，及如何跳转到函数实现快捷操作（与上课一致）

def say_hello(n):
    """
    打印n次hello
    :param n:
    :return:
    """
    for i in range(n):
        print('hello')


say_hello(5)
