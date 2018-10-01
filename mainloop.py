#파이게임 모듈 불러오기
import pygame, math

#파이게임 초기화
pygame.init()
width, height = 640, 480
keys = [False, False, False, False]
playerpos = [100, 100]

screen = pygame.display.set_mode((width, height))
acc = [0, 0] #[적을 몇명 죽였는지,화살을 몇개를 쐈는지]
arrows = []

#3. 이미지를 가져온다.
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")

#4. 계속 화면이 보이도록 한다.

while True:
    #5. 화면을 깨끗하게 한다.

    screen.fill((0,0,0))

    #6. 모든 요소들을 다시 그린다.

    for x in range(width // grass.get_width() + 1):             #grass.get_width --> grass라는 객체의 width값을 가져옴
        for y in range(height // grass.get_height() + 1):               # +1은 나누기는 몫만 출력하기 때문에 남는 부분 하나 더 그려주게함
            screen.blit(grass, (x * 100, y * 100))

    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    # screen.blit(player,playerpos) #screen이라는 객체에 blit함수를 가져온다.

    #6.1 캐릭터 회전
    position = pygame.mouse.get_pos() #현재 마우스의 위치 값을 찾아냄
    angle = math.atan2(position[1]-(playerpos[1]+32), position[0]-(playerpos[0]+26)) #+32, +26는 토끼의 중심에서 회전하기 위함
    playerrot = pygame.transform.rotate(player, 360-angle * 57.29) #마우스 위치로 일정하게 회전 2pi=360
    playerpos1 = (playerpos[0]-playerrot.get_rect().width//2, playerpos[1]-playerrot.get_rect().height//2)
    screen.blit(playerrot, playerpos1)
    
    #6.2  화살 그리기
    for bullet in arrows: #bullet <== [각도, 플레이어의 x좌표, 플레이어의 y좌표]
        index=0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10

        bullet[1]+=velx
        bullet[2]+=vely

        if bullet[1] < -64 or bullet[1]>640 or bullet[2]< -60 or bullet[2] > 480:
            arrows.pop(index)

        index += 1

    for projectile in arrows:
        arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
        screen.blit(arrow1, (projectile[1], projectile[2]))
    
    
    #7. 화면을 다시 그린다.\
    pygame.display.flip() #display.update

    #8 게임을 종료
    for event in pygame.event.get():
        #x를 누르면
        if event.type == pygame.QUIT:
        #게임을 종료
            pygame.quit()
            exit(0)

    #캐릭터 움직이기
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] = acc[1] + 1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32), \
                           position[0] - (playerpos1[0]+26)),\
                           playerpos1[0]+32,\
                           playerpos1[1]+32])


#arrows 화살이 나갈 angle


    playerpos1[0] + 32
    playerpos1[1]+32

    #마우스 이벤트
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5

    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5
