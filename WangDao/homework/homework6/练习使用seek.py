# 作者:胡轩
# 2025年01月02日10时55分34秒
# 1733183066@qq.com
import os


# 5、完成普通文件文件的seek，二进制文件的seek（代码编写与上课一致即可）
def seek():
    file = open('file1', mode='r+', encoding='utf-8')
    file1 = open('file1', mode='r+', encoding='utf-8')
    file2 = open('file1', mode='r+', encoding='utf-8')
    file.seek(3, os.SEEK_SET)
    print(file.read())
    file1.seek(0, os.SEEK_CUR)
    print(file1.read())
    file2.seek(0, os.SEEK_END)
    print(file2.read())
    file.close()
    file1.close()
    file2.close()


def seek_b():
    file = open('file1', mode='rb+')
    file.seek(4, os.SEEK_SET)
    file.seek(-2, os.SEEK_CUR)
    print(file.read())
    file.seek(-5, os.SEEK_END)
    print(file.read())
    file.close()

def modify_pict():
    file=open('Google.jpg',mode='rb+')
    file.seek(10,os.SEEK_SET)
    b = file.read(1)
    inverted_b = bytes([~b[0] & 0xFF])  # 按位取反后限制在0-255范围内
    file.seek(10, os.SEEK_SET)
    file.write(inverted_b)
    file.close()


if __name__ == '__main__':
    # seek()
    # seek_b()
    modify_pict()