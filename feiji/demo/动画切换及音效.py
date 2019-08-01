import sys,pygame
#初始化pygame
pygame.init()
#屏幕对象
screen=pygame.display.set_mode((500,500))
#加载图片
image=pygame.image.load('./static/hero1.png')
image2=pygame.image.load('./static/hero2.png')

clock=pygame.time.Clock()
counter=0

#游戏主循环
while True:
    #处理事件
    counter+=1
    print(1111)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)  #一秒执行60次  60帧
    # 绘制白色屏幕
    screen.fill(pygame.Color(255,255,255))

    #绘制
    if counter%5==0:
        screen.blit(image,(20,20))
    else:
        screen.blit(image2,(20,20))
    pygame.display.flip()