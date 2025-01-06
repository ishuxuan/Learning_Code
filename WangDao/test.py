# 作者:胡轩
# 2024年12月25日23时27分25秒
# 1733183066@qq.com
a=[1,2,3]
b=[2,3]
c=[a,b,6]
d=c.copy()
a[0]=3
c[2]=5
print(c)
print(id(c))
print(d)
print(id(d))
