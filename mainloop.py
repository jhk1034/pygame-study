#파이게임 모듈 불러오기
import pygame

#파이게임 초기화
pygame.init()
width, height = 640, 480
keys = [False, False, False, False]
playerpos = [100, 100]

screen = pygame.display.set_mode((width, height))

#3. 이미지를 가져온다.
player = pygame.image.load("images/dude.png")
grass = pygame.image.load("images/grass.png")
castle = pygame.image.load("images/castle.png")
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

    screen.blit(player,playerpos) #screen이라는 객체에 blit함수를 가져온다.

    #7. 화면을 다시 그린다.
    pygame.display.flip()#화면을 업데이트 = pygame.display.updata()

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

    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5

    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5
