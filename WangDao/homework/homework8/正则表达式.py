# 作者:胡轩
# 2025年01月05日23时25分50秒
# 1733183066@qq.com
import re


# 匹配单个字符，多个字符，匹配分组的正则表达式案例
def single():
    """
    匹配单个字符
    :return:
    """
    ret = re.match(".", "M")
    print(ret.group())

    ret = re.match("t.o", "too")
    print(ret.group())

    ret = re.match("t.o", "two")
    print(ret.group())
    print('-' * 50)
    # 大小写h都可以的情况
    ret = re.match("[hH]", "hello Python")
    print(ret.group())
    ret = re.match("[hH]", "Hello Python")
    print(ret.group())
    ret = re.match("[hH]ello Python", "Hello Python")
    print(ret.group())

    # 匹配0到9第二种写法
    ret = re.match("[0-9]Hello Python", "6Hello Python")
    print(ret.group())

    ret = re.match("[0-35-9]Hello Python", "7Hello Python")
    print(ret.group())
    print('-' * 50)
    # 使用\d进行匹配
    ret = re.match(r"嫦娥\d号", "嫦娥1号发射成功")
    print(ret.group())

    ret = re.match(r"嫦娥\d号", "嫦娥2号发射成功")
    print(ret.group())

    ret = re.match(r"嫦娥\d号", "嫦娥3号发射成功")
    print(ret.group())


def more_alp():
    """
    匹配多个字符
    :return:
    """
    ret = re.match("[A-Z][a-z]*", "M")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "MnnM")
    print(ret.group())

    ret = re.match("[A-Z][a-z]*", "Aabcdef")
    print(ret.group())
    print('-' * 50)
    names = ["name1", "_name", "2_name", "__name__"]
    for name in names:
        ret = re.match(r'[a-zA-Z_]+\w*', name)
        if ret:
            print(f'{ret.group()} 是正确的')
        else:
            print(f'{name} 不符合命名规范')
    print('-' * 50)
    ret = re.match(r"[1-9]?[0-9]", "7")
    print(ret.group())

    ret = re.match(r"[1-9]?\d", "33")
    print(ret.group())

    ret = re.match(r"[1-9]?\d", "09")
    print(ret.group())

    print('-' * 50)
    ret = re.match("[a-zA-Z0-9_]{6}", "12a3g45678")
    print(ret.group())
    ret = re.match("[a-zA-Z0-9_]{8,20}", "1ad12f23s*34455ff66")
    print(ret.group())


def start_end():
    """
    匹配结尾
    :return:
    """
    # 符合163的邮箱找出来
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
    for email in email_list:
        ret = re.match(r'\w{4,20}@163\.com$', email)  # 匹配的字符串中出现了正则的符号，要使用\进行转义
        if ret:
            print(f'{ret.group()}是正确的邮箱{email}')
        else:
            print(f'{email}邮箱地址不正确')

    print('-' * 50)
    # 匹配0到99
    ret = re.match(r"[1-9]?\d$", "49")
    if ret:
        print(ret.group())
    else:
        print('不是0-99之间')


def split_group():
    """
    匹配分组
    :return:
    """
    # 匹配0到100
    ret = re.match(r"[1-9]?\d$|100", "78")
    if ret:
        print(ret.group())
    else:
        print('不是0-100之间')
    # 匹配1到99,匹配分组，依次匹配，写到前面的会先匹配
    # ret = re.match(r"[1-9][0-9]|[1-9]", "11")
    ret = re.match(r"[1-9]$|[1-9][0-9]", "11")
    if ret:
        print(ret.group())
    else:
        print('不是1-99之间')
    print('-' * 50)
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@qq.com")
    print(ret.group())
    ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@126.com")
    print(ret.group())
    print('-' * 50)
    # 代表没有遇到小横杠 - 就一直进行匹配，一直匹配下去
    ret = re.match(r"([^-]+)-(\d+)", "010-12345678")
    print(ret.group())  # 不传参默认取0
    # print(ret.group(0))
    print(ret.group(1))
    print(ret.group(2))
    print('-' * 50)
    # 能够完成对正确的字符串的匹配
    ret = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmla>")
    print(ret.group())
    ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
    print(ret.group())
    print('-' * 50)
    labels = ["<html><h1>www.cskaoyan.com</h1></html>", "<html><h1>www.cskaoyan.com</h2></html>"]

    for label in labels:
        ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", label)
        if ret:
            print("%s 是符合要求的标签" % ret.group())
        else:
            print("%s 不符合要求" % label)
    print('-' * 50)
    for label in labels:
        ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", label)
        if ret:
            print("%s 是符合要求的标签" % ret.group())
        else:
            print("%s 不符合要求" % label)


def use_search_findall_sub_split():
    """
    search findall sub split
    :return:
    """
    ret = re.search(r"\d+", "阅读次数为 9999,点赞888")
    print(ret.group())
    print('-' * 50)
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(ret)
    print('-' * 50)
    ret = re.sub(r"\d+", '998', "python = 997")
    print(ret)
    ret = re.sub(r"\d+", lambda x: str(int(x.group()) + 100), "python = 997")
    print(ret)
    # sub只替换前三个
    text = "apple apple apple apple"
    pattern = r"apple"
    replacement = "orange"

    new_text = re.sub(pattern, replacement, text, count=3)
    print(new_text)
    print('-' * 50)
    s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日', r' ', ret_s)
    ret_s = re.sub(r'时', r':', ret_s)
    ret_s = re.sub(r'分', r'', ret_s)
    ret_s = re.sub(r'。', r'.', ret_s)
    print(ret_s)
    # findall 内部的设计机制，在分组前面加?:
    pattern = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    ret = pattern.findall(ret_s)
    print(ret)
    pattern1 = re.compile(r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]')
    # search 没问题
    ret1 = pattern1.search(ret_s)
    print(ret1.group())
    print('-' * 50)
    long_text = """<div>
            <p>岗位职责：</p>
    <p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
    <p><br></p>
    <p>必备要求：</p>
    <p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
    <p>&nbsp;<br></p>
    <p>技术要求：</p>
    <p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
    <p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
    <p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
    <p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
    <p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
    <p>&nbsp;<br></p>
    <p>加分项：</p>
    <p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

            </div>
        """
    # print(long_text)
    ret = re.sub(r'<[^>]*>|&nbsp;|\n|\s', '', long_text)
    print(ret)
    print('-' * 50)
    ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
    print(ret)


def greedy():
    s = "This is a number 234-235-22-423"
    ret = re.match(r".+?(\d+-\d+-\d+-\d+)", s)
    print(ret.group(1))
    print(re.match(r"aa(\d+)", "aa2343ddd").group(1))

    print(re.match(r"aa(\d+?)", "aa2343ddd").group(1))

    print(re.match(r"aa(\d+)ddd", "aa2343ddd").group(1))

    print(re.match(r"aa(\d+?)ddd", "aa2343ddd").group(1))


if __name__ == '__main__':
    # single()
    # more_alp()
    # start_end()
    # split_group()
    # use_search_findall_sub_split()
    greedy()
