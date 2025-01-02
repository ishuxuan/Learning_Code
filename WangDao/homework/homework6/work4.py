# 作者:胡轩
# 2025年01月02日10时08分42秒
# 1733183066@qq.com

# 4.完成python的传参练习（与上课一致)
import sys

print(type(sys.argv))
print(sys.argv)


def write_hello(file_path):
    file = open(file_path, 'w+', encoding='utf8')
    file.write('hello')
    file.close()


if __name__ == '__main__':
    write_hello(sys.argv[1])
