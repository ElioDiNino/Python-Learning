import pygame
import random
# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (67, 183, 44)
RED = (255, 0, 0)
BROWN = (202, 143, 47)
BLUE = (16, 114, 188)
GREY = (211,211,211)
DGREY = (128,128,128)
YELLOW = (251,255,17)
BRICK = (186, 56, 16)
CLOUD = (158, 161, 163)
ORANGE = (219, 137, 21)
# Start
pygame.init()
size = (600, 700)
# Size
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Rainy Scenery")
#S tuff
done = False
clock = pygame.time.Clock()
rain = []
car_x = -150
car_change = 5
# Rain
for i in range(300):
    x = random.randrange(0,1200)
    y = random.randrange(0,700)
    rain.append([x,y])
    
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    # --- Drawing code
    # Background, Grass, and Path
    pygame.draw.rect(screen, CLOUD, [0,0,600,700])
    pygame.draw.rect(screen, GREEN, [0, 450, 600, 250])
    for path_off in range(0, 125, 1):
        pygame.draw.line(screen,GREY,[250+path_off,450+path_off],[350+path_off,450+path_off],1)
    # Road and Marking Lines
    pygame.draw.rect(screen, DGREY, [0, 575, 600, 125])
    for lines_off in range(0, 561, 70):
        pygame.draw.line(screen,YELLOW,[5+lines_off,636],[55+lines_off,636],4)
    # The Bulding
    pygame.draw.rect(screen, BRICK, [175, 50, 250, 400])
    pygame.draw.polygon(screen, BROWN, [[175, 50], [425,50], [300,0]])
    # - Its Windows
    for wind_x in range(0, 201, 40):
        for wind_y in range(0, 300, 40):
            pygame.draw.rect(screen, BLACK, [185+wind_x, 60+wind_y, 30, 30])
    # - Its Doors
    pygame.draw.rect(screen, BLACK, [258, 380 , 40, 70])
    pygame.draw.rect(screen, BLACK, [302, 380 , 40, 70])
    pygame.draw.ellipse(screen, WHITE, [288, 415, 6, 6])
    pygame.draw.ellipse(screen, WHITE, [306, 415, 6, 6])
    # Car
    pygame.draw.rect(screen, ORANGE, [car_x, 620, 150,40])
    pygame.draw.rect(screen, (122, 161, 193), [car_x + 35, 585, 75, 35])
    pygame.draw.circle(screen, BLACK, [car_x + 35, 665], 15)
    pygame.draw.circle(screen, BLACK, [car_x + 115, 665], 15)
    car_x += car_change
    if car_x > 600:
        car_x = -200
    # Rain
    for i in range(len(rain)):
        pygame.draw.circle(screen, BLUE, rain[i], 2)
        rain[i][1] += 5
        rain[i][0] -= 3
        if rain[i][1] > 700:
            y = random.randrange(-50, -10)
            rain[i][1] = y
            x = random.randrange(0, 1200)
            rain[i][0] = x
    # --- Update the screen with what I've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
pygame.quit()
