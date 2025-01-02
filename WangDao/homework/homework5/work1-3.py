# 作者:胡轩
# 2024年12月30日19时39分44秒
# 1733183066@qq.com

# 1、练习封装案例（和上课保持一致即可）
# 2、练习私有属性和私有方法（和上课保持一致即可）
# 3、练习单继承，多重继承案例（和上课保持一致即可）
class Weapon:
    """
    武器类
    """

    def __init__(self, name):
        self.name = name

    def get(self):
        print(f'获得了一个{self.name}')

    def abandon(self):
        print(f'丢弃了一个{self.name}')


class Gun(Weapon):
    """
    枪类继承武器类（单继承）
    """

    def __init__(self, bullets=3, *args):
        super().__init__(*args)
        self.bullets = bullets

    def fire(self):
        if self.bullets > 0:
            print('哒哒哒....')
            self.bullets -= 1
        else:
            raise Exception('lacking bullet,can not shoot!')

    def get_bullet(self, count):
        self.bullets += count


class Bomb(Weapon):
    """
    手榴弹类继承武器类（单继承）
    """

    def __init__(self, num=1, *args):
        super().__init__(*args)
        self.num = num

    def fire(self):
        if self.num > 0:
            print('fire in the hole!')
        else:
            raise Exception('lacking bomb,can not throw bomb!')


class GrenadeGun(Gun, Bomb):
    """
    榴弹枪类继承枪类和炸弹类（多继承）
    """

    def fire(self):
        if self.bullets > 0 and self.num > 0:
            print('哒哒哒，砰砰砰...')
            self.bullets -= 1
            self.num -= 1
        else:
            raise Exception('子弹或榴弹数量不足，无法射击')


class Soldier:
    def __init__(self, name, age, gender, HasWeapon=False):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.HasWeapon = HasWeapon

    def get_weapon(self, weapon):
        weapon.get()
        self.HasWeapon = True

    def abandon_weapon(self, weapon):
        weapon.abandon()
        self.HasWeapon = False

    def use_weapon(self, hand, times):
        if self.HasWeapon:
            for i in range(times):
                try:
                    hand.fire()
                except:
                    print('弹药数量不足！')
                    self.abandon_weapon(hand)
        else:
            print('还未获得武器，无法使用武器')

    def __output_info(self):
        print(self.__name, self.__age, self.__gender)

    def superior(self):
        self.__output_info()


if __name__ == '__main__':
    # 多态
    zhangsan = Soldier('张三', 25, '男')
    zhangsan.superior()

    m4a1 = Gun(3, 'm4a1')
    flash_bomb = Bomb(2, '闪光弹')
    zhangsan.get_weapon(m4a1)
    zhangsan.use_weapon(m4a1, 4)
    zhangsan.get_weapon(flash_bomb)
    zhangsan.use_weapon(flash_bomb, 1)

    m79 = GrenadeGun(4, 3, 'm79榴弹枪')
    zhangsan.get_weapon(m79)
    n = int(input('张三要使用榴弹枪射击几次:'))
    zhangsan.use_weapon(m79, n)
