import sys, pygame

# 初始化pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))

# 加载字体
# fonts=pygame.font.get_fonts()
# print(fonts)
red = pygame.Color(255, 0, 0)
# 加粗 斜体
font = pygame.font.SysFont('方正兰亭超细黑简体', 40, True, True)
# 文字对象
text = font.render('得分', True, red)
# 加载音乐
bg_music = pygame.mixer.music.load('bullet.mp3')
# 设置音量大小0-1 值越小音越小
pygame.mixer.music.set_volume(0.2)
# 循环播发bgm
pygame.mixer.music.play(-1)   #-1代表无线循环播放

while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(text, (20, 20))
    pygame.display.flip()
