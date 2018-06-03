import pygame

BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

# Initialize window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong-RL")

ball_size = 10
paddle_vel = 10
paddle_length = 100
paddle_height = 20
paddle_length_th = ball_size/2

# Initial coordinates of paddle
rect_x = 400
rect_y = 600 - paddle_height

# Initial speed of paddle
rect_change_x = 0
rect_change_y = 0

# Initial position of ball
ball_x = 50
ball_y = 50

# Speed of ball
ball_change_x = 8
ball_change_y = 8

score = 0

# Draw paddle
def drawrect(screen, x, y):
	if x <= 0:
		x = 0
	if x >= 699:
		x = 699
	pygame.draw.rect(screen, BLUE, [x, y, paddle_length, paddle_height])

# Main loop
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_change_x = -paddle_vel
            elif event.key == pygame.K_RIGHT:
                rect_change_x = paddle_vel           
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rect_change_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rect_change_y = 0                   
    screen.fill(BLACK)
    rect_x += rect_change_x
    rect_y += rect_change_y
    
    ball_x += ball_change_x
    ball_y += ball_change_y
    
    
    # Ball movement
    if ball_x < 0:
        ball_x = 0
        ball_change_x = ball_change_x * -1
    elif ball_x > 785:
        ball_x = 785
        ball_change_x = ball_change_x * -1
    elif ball_y < 0:
        ball_y = 0
        ball_change_y = ball_change_y * -1
    elif ball_x > rect_x - paddle_length_th and ball_x < rect_x+paddle_length+ paddle_length_th and ball_y>=600- paddle_height - ball_size/2:
        ball_change_y = ball_change_y * -1
        ball_y = 600 - paddle_height - ball_size/2
        score = score + 1
    elif ball_y>600 - ball_size/2:
        ball_change_y = ball_change_y * -1
        ball_y = 600 - ball_size/2
        score = 0                        
    pygame.draw.rect(screen, WHITE, [ball_x, ball_y, ball_size, ball_size])
    
    drawrect(screen, rect_x, rect_y)
    
    # Scoreboard
    font= pygame.font.SysFont('Calibri', 25, False, False)
    text = font.render("Score = " + str(score), True, WHITE)
    screen.blit(text, [600, 100])    
       
    pygame.display.flip()         
    clock.tick(60)
    
pygame.quit()