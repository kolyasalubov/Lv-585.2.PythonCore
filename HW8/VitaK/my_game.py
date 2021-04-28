import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

X_INTERSECTION = 430
Y_INTERSECTION = 450

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([700, 700])
 
# This sets the name of the window
pygame.display.set_caption('Hungry Simon')
 
clock = pygame.time.Clock()

#обновляємо екран 
pygame.display.update()
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
#background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("cat.png").convert()
still_image = pygame.image.load("plate.png").convert()
result_image = pygame.image.load("happy_simon.png").convert()

#Якщо в зображення не має прозорого слою, то щоб його встановити,
#необхідно використати метод set_colorkey() класу Surface:
player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

     
 
    
# Get the current mouse position. This returns the position
    # as a list of two numbers.
#повертає поточну позицію мишки на екрані
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
  
       
    screen.fill((BLACK))
    
    if player_position[0] >= X_INTERSECTION and player_position[1]>=Y_INTERSECTION:
              
        screen.blit(result_image, [200, 200])
        pygame.display.flip()
        pygame.time.wait(1000)
        
        done = True
        
    else:
        screen.blit(still_image, [580, 630])
        screen.blit(player_image, [x, y])
 
#обновляємо екран
    pygame.display.flip()
 
    clock.tick(60)
    print (player_position)


pygame.quit()