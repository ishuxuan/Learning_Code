# 作者:胡轩
# 2024年12月26日20时02分23秒
# 1733183066@qq.com

# 5.练习列表基本使用，排序，生成式等各种操作（与上课的代码保持一致）
num_ls = [6, 7, 3, 5, 1, 0, 2, 9, 8, 4]
print(num_ls[2:6])
num_ls.sort(reverse=False)
print(num_ls)
num_ls.reverse()
print(num_ls)

name_list = ["张三", "李四", "王五", "王小二"]
for my_name in name_list:
    print("我的名字叫　%s" % my_name)
name_list.sort(reverse=True)
print(name_list)

a = [1, 2, 3]
b = [4, 5]
print(f'{a}的地址是{id(a)}')
print(f'{a + b}的地址是{id(a + b)}')
a += b
print(f'{a}的地址是{id(a)}')

print([i for i in range(10)])
print([[i * j for i in range(5)] for j in range(3)])
print([i if i % 2 == 0 else i ** 2 for i in range(10)])
