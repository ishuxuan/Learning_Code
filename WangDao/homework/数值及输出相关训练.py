# 2.自己定义变量赋值不同的数据类型并打印，并使用type
a = 10
b = 'abc'
c = 4.6
d = True
e = False
print(type(a))
print(type(b))
print(type(c))
print(type(e))
print(type(a + c))
print(type(d + e))

# 3.能够将整型转为不同进制，进行输出（与上课一致）
print('-' * 50)
print(bin(a))
print(hex(a))
print(oct(a))

# 4.实现从1到100之间的奇数求和
print('-' * 50)
sum = 0
for i in range(100):
    if (i % 2 == 1):
        sum += i
print(sum)

# 5.打印九九乘法表（直接百度乘法表图像，与其一致即可）
print('-' * 50)
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end=' ')
    print('')

# 6.统计一个整数对应的二进制数的1的个数。输入一个整数（可正可负，负数就按64位去遍历即可）， 输出该整数的二进制包含1的个数（使用位运算）
print('-' * 50)
num = int(input('输入一个整数：'))
if (num >= 0):
    print(bin(num).count('1'))
else:
    print(bin((2 ** 64) + num).count('1'))
