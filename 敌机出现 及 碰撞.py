添加第四次
第三次添加
添加第二次
添加一次

"""
1、上下左右移动
2、实现方法，捕捉键盘信号，修改图片坐标

"""
# 导入pygame
import pygame
from pygame.locals import *
import sys
import random

"""
创建玩家飞机类
属性：1、图片； 2、x、y ；3、需要显示的窗口
行为：显示图片到窗口
"""


# 创建 玩家飞机 类
class HeroPlan:
    # 玩家飞机属性
    def __init__(self, x, y, window):
        self.__x = x
        self.__y = y
        self.window = window
        self.image = pygame.image.load("./img/hero2.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.bullets = []

    # 玩家飞机 行为
    # 将自己展示出来
    def disply(self):
        self.window.blit(self.image, (self.__x, self.__y))
        for bullet in self.bullets:
            bullet.display()
            bullet.Bmove()
            # pygame.display.flip()

    # 1、在 飞机类 里创建玩家子弹对象(主体思想：子弹跟最飞机出现，组成完整模块 ）
    # 2、                               （另：方便调用飞机坐标,回传到子弹类中）
    #     bullet=Bullet(self.x+self.width/2,self.y,self.window)？？？？？？？？？？？？？？？？？？
    #    bullet = Bullet(self.x + self.width / 2, self.y, self.window)
    # TypeError: unsupported operand type(s) for /: 'builtin_function_or_method' and 'int'
    #         bullet = Bullet(self.x + self.width / 2, self.y, self.window)

    # 飞机移动
    def up(self):
        # 限制移动范围
        if self.__y <= 0:
            self.__y = 0
        else:
            self.__y -= 5

    def down(self):
        # 限制移动范围
        if self.__y >= (self.window.get_height() - self.image.get_height()):
            self.__y = (self.window.get_height() - self.image.get_height())
        else:
            self.__y += 5

    def right(self):
        # 限制移动范围
        if self.__x >= (self.window.get_width() - self.image.get_width()):
            self.__x = (self.window.get_width() - self.image.get_width())
        else:
            self.__x += 5

    def left(self):
        # 限制移动范围
        if self.__x <= 0:
            self.__x = 0
        else:
            self.__x -= 5

    def fir(self):
        # 发射子弹
        # bx = x + 飞机宽度 / 2 - 子弹宽度 / 2
        # by = y - 子弹的高度

        # 创建子弹对象
        bullet = Bullet(self.__x + self.width / 2, self.__y, self.window)
        # 添加到子弹列表中
        self.bullets.append(bullet)

    # def Fir(self):
    #     # 1、在 飞机类 里创建玩家子弹对象(主体思想：子弹跟最飞机出现，组成完整模块 ）
    #     # 2、                               （另：方便调用飞机坐标,回传到子弹类中）
    #     bullet = Bullet(self.x + self.width / 2, self.y, self.window)
    #     bullet.display()

#创建 子弹类
class Bullet:
    def __init__(self, x, y, window):
        self.image = pygame.image.load("./img/bullet_{}.png".format(random.randint(9, 13)))
        self.__x = x - self.image.get_width() / 2
        self.__y = y - self.image.get_height()
        self.window = window

    # 显示子弹
    def display(self):
        self.window.blit(self.image, (self.__x, self.__y))

    # 子弹移动
    def Bmove(self):
        self.__y -= 5


#创建 敌机类
class E


# 创建主体函数
def star():
    # 初始化窗口，加载窗口基本元素
    pygame.init()

    # 图片加载
    # heroImage = pygame.image.load("./img/hero2.png")
    enemyImage = pygame.image.load("./img/img-plane_{}.png".format(random.randint(1, 7)))
    iconImage = pygame.image.load("./img/game.ico")
    bgImage = pygame.image.load("./img/img_bg_level_2.jpg")

    # 获取图片大小
    WINDOW_WITH = bgImage.get_width()
    WINDOW_HIGH = bgImage.get_height()

    # 设置窗口大小
    window = pygame.display.set_mode((WINDOW_WITH, WINDOW_HIGH))
    # 窗口标题设置
    pygame.display.set_caption("飞机大战")
    # 窗口图标设置
    pygame.display.set_icon(iconImage)

    # 创建玩家飞机对象，简洁语句、方便调用
    heroplan = HeroPlan(200, 500, window)

    # 界面循环（阻塞）：包含 展示内容（画面不断刷新）、捕获事件（窗口上关于鼠标、键盘操作、退出按钮）
    while True:

        # 获取事件列表
        eventList = pygame.event.get()
        # print(eventList)

        # 显示图片
        window.blit(bgImage, (0, 0))
        # window.blit(heroImage, (200, 200))
        heroplan.disply()

        for event in eventList:
            pass
        # 刷新窗口
        pygame.display.flip()

        # 事件一  基于pygame 事件（event）下功能
        # 遍历事件列表，捕捉退出窗口事件
        for event in eventList:

            # 判断是否出现退出窗口事件
            if event.type == QUIT:
                # print(event.type)
                # 退出pygame程序
                pygame.quit()
                # 退出系统
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_j:
                    heroplan.fir()

            # 如果事件类型为按下键盘，捕捉
            # 按下捕捉但是按一次捕捉一次，需要判断按下就执行
            # """
            # 按下捕捉但是按一次捕捉一次，需要判断按下就执行
            # elif event.type==KEYDOWN:
            pass

        # 事件二 捕捉按键按压 基于pygme 按键（key）下功能
        #     print(event.key)
        #     if event.key==K_a:
        #         print("a")
        #         heroplan.left()
        #     if event.key==K_d:
        #         heroplan.right()
        #     if event.key==K_w:
        #         heroplan.up()
        #     if event.key==K_s:
        #         heroplan.down()
        # """
        # 使用以下语句捕捉按下
        stay = pygame.key.get_pressed()
        if stay[K_a]:
            heroplan.left()
        if stay[K_d]:
            heroplan.right()
        if stay[K_s]:
            heroplan.down()
        if stay[K_w]:
            heroplan.up()

#入口函数
if __name__ == '__main__':
    star()

# 知识点获取：
"""
知识点获取：
1、如何将函数中有用数值传出：
    1）在函数中 创建对象，再将值赋值到对象函数中 eg：line78
    2）在函数中创建列表(eg：line 80)  再从列表中提取(line 35)  ps:此处提取的是对象！！


"""