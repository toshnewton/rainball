import pygame
#initialize game
pygame.init()

#define width of screen
width = 500
#define height of screen
height = 500

screen_res = (width, height)

pygame.display.set_caption("bouncingball")
screen = pygame.display.set_mode(screen_res)

black = (0,0,0)

#define ball
Rad = 10
maxRadius = 300
color = [(255,0,0), (255,127,0), (255,255,0), (0,255,0), (0,0,255), (75, 0, 130), (128,0,211)]
i=0

ball_obj = pygame.draw.circle(
    surface = screen, color = color[i], center=[250,250], radius=Rad)

#define speed of ball
#speed = [X direction speed, Y direction speed]
x=0
y=1
speed = [x,y]
speedMultipler = -1.01

#game loop
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #fill black color on screen
    screen.fill(black)        

    #move the ball
    #let center of ball is 100,100 and the speed is (1,1)
    ball_obj = ball_obj.move(speed)
    #now center of ball is (101,101)
    #in this way our wall will move
    if Rad >= maxRadius:
        if ball_obj.left <= 0 or ball_obj.right >= width:
            speed[0] *= speedMultipler
            if i == 6:
                i = -1
            i+=1

        if ball_obj.top <= 0 or ball_obj.bottom >= height:
            speed[1] *= speedMultipler
            if i == 6:
                i = -1
            i+=1
    else:
        if ball_obj.left <= 0 or ball_obj.right >= width:
            speed[0] *= speedMultipler
            Rad*=1.05
            if i == 6:
                i = -1
            i+=1

        if ball_obj.top <= 0 or ball_obj.bottom >= height:
            speed[1] *= speedMultipler
            Rad*=1.05
            if i == 6:
                i = -1
            i+=1

    #draw ball at new centers that are obtain after moving ball_obj
    pygame.draw.circle(surface=screen, color=color[i],
                       center=ball_obj.center, radius=Rad)
    
    #update screen
    pygame.display.flip()