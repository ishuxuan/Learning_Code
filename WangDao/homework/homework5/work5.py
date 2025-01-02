# 作者:胡轩
# 2024年12月30日23时55分59秒
# 1733183066@qq.com

# 5、通过try进行异常捕捉，确保输入的内容一定是一个整型数，然后判断该整型数是否是对称数，12321就是对称数，123321也是对称
while True:
    try:
        num = int(input('请输入一个整型数:'))
        break
    except:
        print('error,输入的不是整型数!')

num = str(num)
if num[::-1] == num:
    print('该整型数是对称数')
else:
    print('该整型数不是对称数')
