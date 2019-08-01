import pygame
import constants

class Bullet(pygame.sprite.Sprite):
    """子弹类"""

    #子弹状态True：活着  False：超出屏幕或已碰撞

    def __init__(self,screen,plane,speed=None):
        super().__init__()#调用父类的构造方法
        self.screen=screen  #画
        #速度
        self.speed=speed or 10
        self.plane=plane

        #加载子弹的图片
        self.image=pygame.image.load(constants.BULLET_IMG)

        #改变子弹的位置
        self.rect=self.image.get_rect()
        self.rect.centerx=plane.rect.centerx
        self.rect.top=plane.rect.top

        #发射的音乐效果
        self.shoot_sound=pygame.mixer.Sound(constants.BULLET_SHOOT_SOUND)
        self.shoot_sound.set_volume(0.3) #音量
        self.shoot_sound.play()

    #def update(self,*args):
    def update(self,war):
        """更新子弹的位置"""
        self.rect.top-=self.speed
        #超出屏幕的范围
        if self.rect.top<0:
            self.remove(self.plane.bullets)
            print(self.plane.bullets)
        #绘制子弹
        self.screen.blit(self.image,self.rect)
        #碰撞检测，检测子弹是否已经碰撞到了敌机
        rest=pygame.sprite.spritecollide(self,war.enemies,False)
        print(rest,666)
        for r in rest:
            #1.子弹消失
            self.kill()
            #2.飞机爆炸
            r.broken_down()
            #3.统计游戏成绩
            war.rest.score+=constants.SCORE_SHOOT_SMALL
            #保存历史
            war.rest.set_history()

