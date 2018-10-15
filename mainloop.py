#파이게임 모듈 불러오기
import pygame, math, random

#파이게임 초기화
pygame.init()
width, height = 640, 480
keys = [False, False, False, False]
playerpos = [100, 100]
badtimer = 100 #적이 출현하는 시간 1000 = 1초
badtimer1 = 0
badguys = [[640,100]] #적이 출현하는 위치
healthvalue = 194

screen = pygame.display.set_mode((width, height))
acc = [0, 0] #[적을 몇명 죽였는지,화살을 몇개를 쐈는지]
arrows = []

#3. 이미지를 가져온다.
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg = pygame.image.load("resources/images/badguy.png")
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")

#4. 계속 화면이 보이도록 한다.

while True:
    badtimer-=1

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
    
    #6.3 적들을 화면에 그린다.
    if badtimer == 0:
        badguys.append([640, random.randint(50, 430)])
        badtimer = 100-(badtimer1 * 2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5

    index = 0

    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)
        else:
            badguy[0] -= 7

        #6.3.1 - 성을 공격
        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            healthvalue -= random.randint(5, 20)
            badguys.pop(index)

        #6.3.2 - 적이 화살에 맞았을 때
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect): #충돌 했는가? badrect이 bullrect과 출동했는가?
                acc[0]+=1
                badguys.pop(index)
                arrows.pop(index1)
            index1 += 1

        index += 1

    for badguy in badguys:
        screen.blit(badguyimg, badguy)


    #6.4 - 시간 표시
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str(int(90000-pygame.time.get_ticks())) + " : " \
                   + str(int((90000-pygame.time.get_ticks())/1000%60)).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635, 5]
    screen.blit(survivedtext, textRect)

    #6.5 - 체력바 그리기
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8, 8 ))

    #7. 화면을 다시 그린다.
    pygame.display.flip() #display.update

    #8 게임을 종료
    for event in pygame.event.get():
        #x를 누르면
        if event.type == pygame.QUIT:
        #게임을 종료
            pygame.quit()
            exit(0)

    #9.캐릭터 움직이기
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

    #10 클리어/페일 조건달기
        if pygame.time.get_ticks() >= 90000:
            running = 0
            exitcode = 1

        if healthvalue <= 0:
            running = 0
            exitcode = 0
        if acc[1] != 0:
            accuracy = acc[0]*1.0/acc[1]*100
        else:
            accuracy = 0

#11. 승/패 표시하기
