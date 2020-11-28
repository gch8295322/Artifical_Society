import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import time


# 个体类 提供各种数值更改操作接口
class person:
    # x,y的真实值和像素坐标值
    x_real = 1
    y_real = 1
    x_pixel = x_real * 40 - 20
    y_pixel = y_real * 40 - 20
    money = 50
    iq = False
    life = True

    def __init__(self):
        pass

    # 写入xy值
    def per_xy(self, x, y):
        self.x_real = x
        self.y_real = y
        self.per_update()

    # 更新像素坐标位置
    def per_update(self):
        self.x_pixel = self.x_real * 40 - 20
        self.y_pixel = self.y_real * 40 - 20

    # 个体上下左右行走
    def person_walk_up(self):
        if self.y_real - 1 < 1:
            pass
        else:
            self.y_real -= 1
            self.per_update()

    def person_walk_down(self):
        if self.y_real + 1 > 25:
            pass
        else:
            self.y_real += 1
            self.per_update()

    def person_walk_left(self):
        if self.x_real - 1 < 1:
            pass
        else:
            self.x_real -= 1
            self.per_update()

    def person_walk_right(self):
        if self.x_real + 1 > 25:
            pass
        else:
            self.x_real += 1
            self.per_update()


# 区域类 提供各种绘图接口
class area:
    # 区域大小
    x_pixel = 1000
    y_pixel = 1000
    x_max = 25
    y_max = 25

    # 区域初始化
    def __init__(self):
        # 图像初始化
        self.image = np.zeros((self.x_pixel, self.y_pixel, 3), dtype='uint8')
        # 糖域初始化
        self.suger = np.zeros((self.x_max + 3, self.y_max + 3), dtype=np.float)

        # 绘制区域
        for i in range(0, 1000, 40):
            self.image[:, i] = 255
            self.image[i, :] = 255
        # 绘制糖域与糖域初始化
        for i in range(2 * 40, 13 * 40):
            for j in range(12 * 40, 23 * 40):
                self.image[i, j] = 100
                self.image[j, i] = 100
                if i % 40 == 0 and j % 40 == 0:
                    xx = int(i / 40 + 1)
                    yy = int(j / 40 + 1)
                    self.suger[xx, yy] = 1000
                    self.suger[yy, xx] = 1000

        for i in range(3 * 40, 12 * 40):
            for j in range(13 * 40, 22 * 40):
                self.image[i, j] = 130
                self.image[j, i] = 130
                if i % 40 == 0 and j % 40 == 0:
                    xx = int(i / 40 + 1)
                    yy = int(j / 40 + 1)
                    self.suger[xx, yy] = 2000
                    self.suger[yy, xx] = 2000
        for i in range(4 * 40, 11 * 40):
            for j in range(14 * 40, 21 * 40):
                self.image[i, j] = 160
                self.image[j, i] = 160
                if i % 40 == 0 and j % 40 == 0:
                    xx = int(i / 40 + 1)
                    yy = int(j / 40 + 1)
                    self.suger[xx, yy] = 3000
                    self.suger[yy, xx] = 3000
        for i in range(5 * 40, 10 * 40):
            for j in range(15 * 40, 20 * 40):
                self.image[i, j] = 190
                self.image[j, i] = 190
                if i % 40 == 0 and j % 40 == 0:
                    xx = int(i / 40 + 1)
                    yy = int(j / 40 + 1)
                    self.suger[xx, yy] = 4000
                    self.suger[yy, xx] = 4000
        # 中心为(8,18)和(18,8)
        for i in range(7 * 40, 8 * 40):
            for j in range(17 * 40, 18 * 40):
                self.image[i, j] = 255
                self.image[j, i] = 255
                if i % 40 == 0 and j % 40 == 0:
                    xx = int(i / 40 + 1)
                    yy = int(j / 40 + 1)
                    self.suger[xx, yy] = 5000
                    self.suger[yy, xx] = 5000

    # 单个person的区域绘图
    def person_on_area(self, x, y, k):
        # 半径取值
        radius = 10
        # 颜色取值
        color = (k, k, k)
        # 圆心取值 横/纵坐标
        pt = (x, y)
        # 画图
        cv2.circle(self.image, tuple(pt), radius, color, -1)

    # 区域绘制
    def show(self):
        fig1 = plt.figure(1)
        plt.imshow(self.image)
        # plt.axis('off')
        # plt.show()
        plt.pause(0.1)
        # plt.close(fig1)
        fig1.canvas.flush_events()

    def init_area(self):
        # 绘制区域
        for i in range(0, 1000, 40):
            self.image[:, i] = 255
            self.image[i, :] = 255
        # 绘制糖域与糖域初始化
        for i in range(2 * 40, 13 * 40):
            for j in range(12 * 40, 23 * 40):
                self.image[i, j] = 100
                self.image[j, i] = 100

        for i in range(3 * 40, 12 * 40):
            for j in range(13 * 40, 22 * 40):
                self.image[i, j] = 130
                self.image[j, i] = 130
        for i in range(4 * 40, 11 * 40):
            for j in range(14 * 40, 21 * 40):
                self.image[i, j] = 160
                self.image[j, i] = 160
        for i in range(5 * 40, 10 * 40):
            for j in range(15 * 40, 20 * 40):
                self.image[i, j] = 190
                self.image[j, i] = 190
        for i in range(7 * 40, 8 * 40):
            for j in range(17 * 40, 18 * 40):
                self.image[i, j] = 210
                self.image[j, i] = 210


# 个体位置初始化
def person_set_init(p_set, n):
    cnt = 0
    for i in range(15):
        for j in range(15):
            p_set[cnt].x_real = np.random.randint(1, 26)
            p_set[cnt].y_real = np.random.randint(1, 26)
            p_set[cnt].per_update()
            cnt += 1


# 个体绘制在区域内
def person_DrawOnArea(base, p_set):
    for per in p_set:
        if per.life == True:
            base.person_on_area(per.x_pixel, per.y_pixel, 255)


# 清除个体
def person_clear(base, p_set):
    for per in p_set:
        base.person_on_area(per.x_pixel, per.y_pixel, 0)


# 个体行走规则
def person_walk(p_set, base, time_k):
    for per in p_set:
        # 有远见的人直奔糖点中心
        if per.iq == True and time_k < 10:
            distance1 = abs(8 - per.x_real) + abs(18 - per.y_real)
            distance2 = abs(18 - per.x_real) + abs(8 - per.y_real)
            higher = np.argmin([distance1, distance2])
            if higher == 0:
                if per.x_real < 8:
                    per.person_walk_right()
                elif per.x_real > 8:
                    per.person_walk_left()
                elif per.x_real == 8:
                    if per.y_real < 18:
                        per.person_walk_down()
                    elif per.y_real > 18:
                        per.person_walk_up()
            else:
                if per.x_real < 18:
                    per.person_walk_right()
                elif per.x_real > 18:
                    per.person_walk_left()
                elif per.x_real == 18:
                    if per.y_real < 8:
                        per.person_walk_down()
                    elif per.y_real > 8:
                        per.person_walk_up()
        # 寻找附近最高糖点
        else:
            rand = np.random.randint(1, 101)
            left = base.suger[per.x_real - 1, per.y_real]
            up = base.suger[per.x_real, per.y_real - 1]
            right = base.suger[per.x_real + 1, per.y_real]
            down = base.suger[per.x_real, per.y_real + 1]
            # max_suger = max(left, up, right, down)
            max_arg = np.argmax([1, left, up, right, down])
            if max_arg == 1:
                per.person_walk_left()
            elif max_arg == 2:
                per.person_walk_up()
            elif max_arg == 3:
                per.person_walk_right()
            elif max_arg == 4:
                per.person_walk_down()
            elif rand <= 25:
                per.person_walk_left()
            elif rand > 25 and rand <= 50:
                per.person_walk_up()
            elif rand > 50 and rand <= 75:
                per.person_walk_right()
            elif rand > 75 and rand <= 100:
                per.person_walk_down()


# 收入模拟
def money_in(p_set, base):
    for per in p_set:
        per.money += 0.05 * base.suger[per.x_real, per.y_real]
        base.suger[per.x_real, per.y_real] -= 0.05 * base.suger[per.x_real, per.y_real]


# 弱者淘汰
def person_die(p_set):
    for per in p_set:
        per.money -= 3
        if per.money < 0:
            per.life = False


# 智商初始化
def iq_init(p_set):
    for per in p_set:
        if np.random.randint(0, 101) > 40:
            per.iq = True
        else:
            per.iq = False


if __name__ == '__main__':
    MaxN = 15 * 15  # 地区大小
    time_k = 0
    base = area()  # 创建区域
    person_set = [person() for i in range(MaxN)]  # 个体集合
    iq_init(person_set)
    person_set_init(person_set, MaxN)  # 个体位置初始化
    person_DrawOnArea(base, person_set)  # 个体位置分布于区域内
    person_clear(base, person_set)
    while time_k < 25:
        person_walk(person_set, base, time_k)
        money_in(person_set, base)
        person_die(person_set)
        base.init_area()
        person_DrawOnArea(base, person_set)
        base.show()  # 区域绘制
        person_clear(base, person_set)  # 清图
        time_k += 1
    x = np.zeros(225)
    y = np.zeros(225)
    cnt = 0
    for per in person_set:
        x[cnt] = cnt
        y[cnt] = per.money
        cnt += 1
    y = np.sort(y)
    plt.close()
    plt.xlabel("Num")
    plt.ylabel("Money")
    plt.title("Wealth Distribution")
    plt.plot(x, y)
    plt.show()
