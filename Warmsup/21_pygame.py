import pygame


pygame.init() #초기화 (필수)

#화면 크기를 설정
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

#타이틀 설정
pygame.display.set_caption('Pygame 예제')

#배경 이미지 불러오기
background = pygame.image.load('background_test.png')

#캐릭터 불러오기
character = pygame.image.load('character.png')
#캐릭터 크기 구하기
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
#캐릭터 위치 구하기
character_xpos = (screen_width/2) - (character_width/2)
character_ypos = (screen_height/2) - (character_height/2)

#적군 불러오기
enemy = pygame.image.load('enemy.png')

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xpos = (screen_width/2) - (enemy_width/2) -100
enemy_ypos = (screen_height/2) - (enemy_height/2) - 100



#이동할 좌표
to_x = 0
to_y = 0

#FPS를 위한 clock 저장
clock = pygame.time.Clock()

# 캐릭터 이동 속도
speed = 0.5

##==========================================================
running = True #게임중
while running:
    
    dt = clock.tick(30) #FPS 설정 - 초당 프레임수를 설정
    
    #10 fps : 1초에 10번 동작 100 -> 1번에 10만큼 이동을 해줘야 10 * 10 = 100 
    #20 fps : 1초에 20번 동작 100 -> 1번에 5만큼 이동을 하면 20 * 5 = 100
    
    
    for event in pygame.event.get(): #이벤트 발생했는지 체크
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생
            running = False
        
        #키보드 이벤트 
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #왼쪽
                to_x = -1 * speed
            elif event.key == pygame.K_RIGHT: #오른쪽
                to_x = speed
            elif event.key == pygame.K_UP: #위
                to_y = -1 * speed
            elif event.key == pygame.K_DOWN: #아래
                to_y = speed
         
        if event.type == pygame.KEYUP: #키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0            
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                to_y = 0
            
            
    #캐릭터 좌표 업데이트
    character_xpos = character_xpos + (to_x * dt)
    character_ypos = character_ypos + (to_y * dt)
    
    #프레임을 벗어나지 않도록 경계값 처리
    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width
    
    if character_ypos < 0:
        character_ypos = 0
    elif character_ypos > screen_height - character_height:
        character_ypos = screen_height - character_height
        
        
        
    # 충돌 체크
    character_rect = character.get_rect()
    character_rect.left = character_xpos
    character_rect.top = character_ypos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xpos
    enemy_rect.top = enemy_ypos
    
    if character_rect.colliderect(enemy_rect):
        running = False
        print('충돌했어요')
    
            
    # 이미지 그리기        
    screen.blit(background, (0,0)) #배경 이미지 그리기
    screen.blit(character, (character_xpos,character_ypos)) #캐릭터 이미지 그리기
    screen.blit(enemy, (enemy_xpos,enemy_ypos)) #적군 이미지 그리기
    pygame.display.update()

##==========================================================

pygame.quit() #종료
