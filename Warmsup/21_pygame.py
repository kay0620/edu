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

#이동할 좌표
to_x = 0
to_y = 0
##==========================================================
running = True #게임중
while running:
    for event in pygame.event.get(): #이벤트 발생했는지 체크
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생
            running = False
        
        #키보드 이벤트 
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #왼쪽
                to_x = -1
            elif event.key == pygame.K_RIGHT: #오른쪽
                to_x = 1
            elif event.key == pygame.K_UP: #위
                to_y = -1
            elif event.key == pygame.K_DOWN: #아래
                to_y = 1
         
        if event.type == pygame.KEYUP: #키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0            
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                to_y = 0
            
            
    #캐릭터 좌표 업데이트
    character_xpos = character_xpos + to_x
    character_ypos = character_ypos + to_y
    
    #프레임을 벗어나지 않도록 경계값 처리
    if character_xpos < 0:
        character_xpos = 0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width
    
    if character_ypos < 0:
        character_ypos = 0
    elif character_ypos > screen_height - character_height:
        character_ypos = screen_height - character_height
            
            
    screen.blit(background, (0,0)) #배경 이미지 그리기
    screen.blit(character, (character_xpos,character_ypos)) #캐릭터 이미지 그리기
    pygame.display.update()

##==========================================================

pygame.quit() #종료
