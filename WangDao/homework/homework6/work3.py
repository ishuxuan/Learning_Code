# 作者:胡轩
# 2025年01月02日10时02分15秒
# 1733183066@qq.com

# 3.完成目录的listdir，getcwd,chdir的使用（与上课一致）
import os


def dir_opera():
    print(os.listdir('.'))
    os.mkdir('dir1')
    print(os.listdir())
    os.rmdir('dir1')
    print(os.listdir())
    os.chdir('.\message')
    print(os.listdir())
    print(os.getcwd())


# 6、完成目录深度优先遍历（代码编写与上课一致即可）
def dfs(current_path, width):
    file_list = os.listdir(current_path)  # 得到当前文件夹下的所有文件
    for file in file_list:
        print(' ' * width, file)  # 打印文件名,width代表多少个空格
        new_path = current_path + '/' + file  # 把当前路径和文件名拼接到一起
        if os.path.isdir(new_path):
            dfs(new_path, width + 4)


if __name__ == '__main__':
    # dir_opera()
    dfs('..', 0)
