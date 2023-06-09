import pygame
import random

pygame.init()

# 1. 기본 초기화 

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption('똥피하기 게임')

# 배경만들기
background = pygame.image.load('background.png')

#사용자 캐릭터
user = pygame.image.load('frenh.png')
user_size = user.get_rect().size
user_width = user_size[0]
user_height = user_size[1]
user_xpos = (screen_width/2) - (user_width/2)
user_ypos = screen_height - user_height

#똥 캐릭터 
ddong = pygame.image.load('ddong.png')
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_xpos = random.randint(0,screen_width-ddong_width)
ddong_ypos = 10

#이동위치
to_x = 0

#FPS를 위한 clock 저장
clock = pygame.time.Clock()

# 캐릭터 이동 속도
speed = 0.5
ddong_speed = 0.3

#폰트 정의
game_font = pygame.font.SysFont('나눔손글씨펜',40)
msg = 'Game Over'

#시간 정의
total_time = 10 #총 게임 시간
start_ticks = pygame.time.get_ticks() #시작시간 정의

#점수 
score = 0
#==================================================================
#2. 게임중
running = True
while running:
    
    dt = clock.tick(60) #FPS 설정
    
    #키보드 이벤트
    for event in pygame.event.get(): #이벤트 발생했는지 체크
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 발생
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x = -1 * speed
            elif event.key == pygame.K_RIGHT:
                to_x = speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
       
    #캐릭터 위치 저장
    user_xpos += (to_x * dt)
    if user_xpos < 0:
        user_xpos = 0
    elif user_xpos > screen_width - user_width:
        user_xpos = screen_width - user_width
    
    #똥 캐릭터 위치 저장
    ddong_ypos += (ddong_speed * dt)
    
    if ddong_ypos > screen_height - ddong_height:
        ddong_xpos = random.randint(0,screen_width-ddong_width)
        ddong_ypos = 10
        
        #점수 추가
        score += 10
    
    #충돌처리
    user_rect = user.get_rect()
    user_rect.left = user_xpos
    user_rect.top = user_ypos
    
    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_xpos
    ddong_rect.top = ddong_ypos
    
    if user_rect.colliderect(ddong_rect):
        msg = '충돌했어요'
        running = False
    
    #화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(user, (user_xpos, user_ypos))
    screen.blit(ddong, (ddong_xpos, ddong_ypos))
    
    #경과시간 
    elapsed_time = (pygame.time.get_ticks()-start_ticks) // 1000
    
    if total_time - elapsed_time <= 0:
        running = False
        msg = 'Time Over'
    
    time_msg = 'Time: %d'%(total_time - elapsed_time)
    time_text = game_font.render(time_msg, True, (255,255,255))
    screen.blit(time_text, (10,10))
    
    #점수 출력
    score_msg = 'Score: %d'%(score)
    score_text = game_font.render(score_msg, True, (255,255,255))
    screen.blit(score_text, (screen_width-score_text.get_width()-10,10))
    
    pygame.display.update()
#==================================================================

# 3. 게임 종료시 처리
text = game_font.render(msg, True, (9,5,128))
text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
screen.blit(text, text_rect)
pygame.display.update()
pygame.time.delay(2000)

pygame.quit()
