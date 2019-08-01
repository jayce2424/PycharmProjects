import sys

import pygame

import constants
from game.plane import OurPlane, SmallEnemyPlane
from game.war import PlaneWar


def main():
    # """游戏入口，main方法"""
    # #初始化
    # pygame.init()
    #
    # width,height=480,852
    #
    # #屏幕对象
    # screen=pygame.display.set_mode((width,height))
    # #设置标题
    # pygame.display.set_caption('飞机大战')
    #
    # #加载背景图片
    # bg=pygame.image.load(constants.BG_IMG)
    # #游戏的标题
    # img_game_title=pygame.image.load(constants.IMG_GAME_TITLE)
    # img_game_title_rect=img_game_title.get_rect()
    # #获取标题的长和宽
    # t_width,t_height=img_game_title.get_size()
    # img_game_title_rect.topleft=(int((width-t_width)/2),
    #                              int(height/2-t_height))
    #
    # #开始按钮
    # btn_start=pygame.image.load(constants.IMG_GAME_START_BTN)
    # btn_start_rect=btn_start.get_rect()
    # btn_width,btn_height=btn_start.get_size()
    # btn_start_rect.topleft=(int((width-btn_width)/2),
    #                         int(height/2+btn_height))
    #
    #
    # #加载背景音乐
    # # pygame.mixer.music.load(constants.BG_MUSIC)
    # # pygame.mixer.music.play(-1) #无线循环播放
    # # pygame.mixer.music.set_volume(0.2)  #设置音量
    #
    # #游戏状态
    # status = 0 #0准备中 1游戏中 2游戏结束
    #
    # our_plane=OurPlane(screen,speed=20)
    #
    #
    #
    # frame=0 #播放帧数
    # clock = pygame.time.Clock()
    #
    # #一架飞机可以属于多个精灵组，方便碰撞检测
    # small_enemies=pygame.sprite.Group()
    # enemies=pygame.sprite.Group()
    # #随机添加6架小型敌机
    # for i in range(6):
    #     plane=SmallEnemyPlane(screen,8)
    #     plane.add(small_enemies,enemies)
    #
    # while True:
    #     #设置帧速率
    #     clock.tick(60)
    #     frame+=1
    #     if frame>=60:
    #         frame=0
    #
    #     #1.监听事件
    #     for event in pygame.event.get():
    #         #退出游戏
    #         if event.type==pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         elif event.type==pygame.MOUSEBUTTONDOWN:
    #             #鼠标点击进入游戏
    #             #游戏只有在准备中，点击才能进入游戏
    #             if status==0:
    #                 status=1
    #         elif event.type==pygame.KEYDOWN:
    #             #键盘事件
    #             #游戏正在游戏中，才需要控制键盘  aswd
    #             if status==1:
    #                 if event.key==pygame.K_w or event.key==pygame.K_UP:
    #                     our_plane.move_up()
    #                 elif event.key==pygame.K_s or event.key==pygame.K_DOWN:
    #                     our_plane.move_down()
    #                 elif event.key==pygame.K_a or event.key==pygame.K_LEFT:
    #                     our_plane.move_left()
    #                 elif event.key==pygame.K_d or event.key==pygame.K_RIGHT:
    #                     our_plane.move_right()
    #                 elif event.key==pygame.K_SPACE:
    #                     #发射子弹
    #                     our_plane.shoot()
    #     #2.更新游戏的状态
    #     if status == 0:
    #         #游戏正在准备中
    #         # 3.绘制背景
    #         screen.blit(bg, bg.get_rect())
    #         #标题
    #         screen.blit(img_game_title,img_game_title_rect)
    #         #开始按钮
    #         screen.blit(btn_start,btn_start_rect)
    #     elif status==1:
    #         #游戏进行中
    #         #绘制背景
    #         screen.blit(bg, bg.get_rect())
    #         #绘制飞机
    #         our_plane.update(frame)
    #         #our_plane.blit_me()
    #         #screen.blit(our_plane.image())
    #         #绘制子弹
    #         our_plane.bullets.update()
    #         #绘制敌方飞机
    #         small_enemies.update()
    #
    #
    #
    #     pygame.display.flip()
    war=PlaneWar()
    #添加小型敌方飞机
    war.add_small_enemies(6)
    war.run_game()

if __name__=='__main__':
    main()