# 4、实现单例模式（和上课保持一致即可）
class MusicPlayer(object):
    instance = None  # 用来保存对象的

    def __new__(cls, *args, **kwargs):
        # 1、创建对象，分配空间
        if cls.instance is None:
            cls.instance = super().__new__(cls)  # 父亲的new类似于C的malloc
        return cls.instance

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    player1 = MusicPlayer('七里香')
    player2 = MusicPlayer('东风破')
    print(player1 is player2)
    print(player1.name)
    print(player2.name)
