# coding=utf-8

"""
作者: lmintlcx
日期: 2019-03-14
阵名: RE十六炮
出处: https://tieba.baidu.com/p/1410367512
节奏: ch6: PSD/P|IP-PPD|PSD/P|IP-PPD, (6|12|6|12)
视频:
- https://www.bilibili.com/video/av38407808
- https://www.youtube.com/watch?v=g1xNVLRDyKo
"""

from pvz import *

# EnableLogger(False)  # 输出调试信息
# SetWindowTopMost(True)  # 窗口置顶

# BackgroundRunning(True)  # 允许后台运行
# ZombieNoFalling(True)  # 僵尸死后不掉钱

# SetSun(8000)  # 阳光 8000
# SetMoney(0)  # 金钱 0
# JumpLevel(1009)  # 完成 2018 面旗帜数

SetZombies(["普僵", "撑杆", "橄榄", "冰车", "小丑", "气球", "跳跳", "蹦极", "扶梯", "篮球", "白眼", "红眼"])

Sleep(200)

SelectCards(["玉米", "玉米炮", "樱桃", "倭瓜", "坚果", "核蘑菇", "冰蘑菇", "模仿者寒冰菇", "咖啡豆", "花盆"])

UpdatePaoList(
    [
        (1, 3),  # P
        (1, 5),  # S
        (1, 7),  #    P
        (1, 1),  # D
        (2, 3),  # P
        (2, 5),  # P
        (2, 7),  #    P
        (2, 1),  # D
        (3, 3),  # P
        (3, 5),  # S
        (3, 7),  #    P
        (3, 1),  # D
        (4, 6),  # P
        (4, 1),  # P
        (5, 6),  #    P
        (5, 1),  # D
    ]
)

StartAutoFillIceThread([(5, 3), (4, 3)], 11)
StartAutoCollectThread()


for wave in range(1, 21):
    print("当前操作波次: " + str(wave))

    # PPSD
    if wave in (1, 3, 5, 7, 9, 10, 12, 14, 16, 18):
        Prejudge(-10, wave)  # -10+373 < 370
        RoofPao((2, 9), (2, 9), (4, 9))
        Delay(110)  # 110 拦截
        RoofPao((2, 8.8))
        Until(601 + 50 - 298)  # 50cs 预判冰
        Coffee()
        if wave == 9:
            Until(601 - 150)
            RoofPao((2, 9))
            Until(601 + 1200 - 200 - 373)
            RoofPao((5, 9), (5, 9))
            Delay(1100)  # 等会儿
            RoofPao((5, 9))

    # IP-PPD
    elif wave in (2, 4, 6, 8, 11, 13, 15, 17, 19):
        Prejudge(-150, wave)
        RoofPao((2, 9))
        Until(1200 - 200 - 373)  # 1200cs 波长
        RoofPao((2, 9), (4, 9))  # 激活炸
        Delay(220)  # 220 拦截
        RoofPao((2, 7.8))
        if wave == 19:
            Until(1200 - 10)
            RoofPao((2, 9), (2, 9), (4, 9))
            Delay(110)  # 110 拦截
            RoofPao((2, 8.8))
            Until(1200 + 601 - 150)
            RoofPao((5, 9))
            Until(1200 + 601 + 1200 - 200 - 373)
            Delay(50)  # 等会儿
            RoofPao((5, 9))

    elif wave == 20:
        Prejudge(-200, wave)
        Coffee()  # 冰消空降
        Until(-100)
        RoofPao((2, 9), (5, 9))  # 炸冰车
        Until(50)
        RoofPao((4, 2.5), (4, 6.7))  # 炸小偷
        Until(800)
        RoofPao((2, 9), (2, 9), (2, 9), (2, 9))
        Until(1000)
        RoofPao((4, 9), (4, 9), (4, 9), (4, 9))
        print(f"第 {wave} 波手动收尾.")
