# 作者:胡轩
# 2025年01月02日08时58分52秒
# 1733183066@qq.com

# 2.完成文件的文本模式的读，写（与上课一致）

def file_r():
    file = open('file1', mode='r', encoding='utf-8')
    print(file.read())
    file.close()


def file_w():
    file = open('file1', mode='w', encoding='utf-8')
    file.write("what's up?")
    file.close()


def file_rw():
    file = open('file1', mode='r+', encoding='utf-8')
    print(file.read())
    file.write('\nhelloworld,你好世界')
    file.close()


def file_wr():
    file = open('file1', mode='w+', encoding='utf-8')
    print(file.read())
    file.write('welcome')
    file.close()


def file_a():
    file = open('file1', mode='a', encoding='utf-8')
    file.write('\nhelloworld')
    file.close()


def file_readline():
    file = open('file1', mode='r', encoding='utf-8')
    # while True:
    #     text = file.readline()
    #     if text:
    #         print(text, end='')
    #     else:
    #         break
    lines = file.readlines()
    for i in lines:
        print(i, end='')
    file.close()


if __name__ == '__main__':
    # file_r()
    # file_w()
    # file_rw()
    # file_wr()
    # file_a()
    file_readline()
