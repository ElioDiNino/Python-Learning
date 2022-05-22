import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (219, 137, 21)
YELLOW = (249, 229, 0)
DGREY = (128,128,128)
NGREEN = (101, 224, 74)
BLUE = (16, 114, 188)

x_speed = 0
x_coord = 224


pygame.init()
def draw_road():
    pygame.draw.rect(screen, DGREY, [0, 575, 600, 125])
    for lines_off in range(0, 561, 70):
        pygame.draw.line(screen,YELLOW,[5+lines_off,636],[55+lines_off,636],4)
def draw_car(x):
    pygame.draw.rect(screen, ORANGE, [x, 620, 150,40])
    pygame.draw.rect(screen, (122, 161, 193), [x + 35, 585, 75, 35])
    pygame.draw.circle(screen, BLACK, [x + 35, 665], 15)
    pygame.draw.circle(screen, BLACK, [x + 115, 665], 15)
def draw_face(screen, x, y):
    pygame.draw.circle(screen, YELLOW, [x,y], 20)
    pygame.draw.circle(screen, BLACK, [x-9,y-9], 7)
    pygame.draw.circle(screen, BLACK, [x+9,y-9], 7)
    pygame.draw.arc(screen, BLACK, [x-9,y+2, 18, 12], 3.14159, 0, 2)
# Set the width and height of the screen [width, height]
size = (600, 700)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Move Stuff")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Rain
rain = []
for i in range(300):
    x = random.randrange(0,1200)
    y = random.randrange(0,700)
    rain.append([x,y])
    
pygame.mouse.set_visible(0)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_speed = -3
            elif event.key == pygame.K_d:
                x_speed = 3
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_speed = 0

    # --- Game logic should go here
    x_coord += x_speed
    if x_coord < 0:
        x_coord = 0
    elif x_coord > 450:
        x_coord = 450
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    if x_coord + 75 < 300:
        screen.fill((61, 219, 206))
    elif x_coord + 75 >= 300:
        screen.fill((211,211,211))
    # --- Drawing code should go here
    pygame.draw.circle(screen, NGREEN, [50, 625], 315)
    pygame.draw.circle(screen, NGREEN, [550, 625], 315)
    draw_road()
    draw_car(x_coord)
    pos = pygame.mouse.get_pos()
    draw_face(screen, pos[0],pos[1])
    if x_coord + 75 < 300:
        pygame.draw.circle(screen, YELLOW, [300, 300], 50)
    elif x_coord + 75 >= 300:
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
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
