# # 1-ий варіант - просто забираємо слід

# import pygame

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# pygame.init()
 
# screen = pygame.display.set_mode([900, 500])
 
# pygame.display.set_caption('Fly')
 
# clock = pygame.time.Clock()

# pygame.display.update()
 

# player_image = pygame.image.load(r"C:\Users\dima\Desktop\lesson8_pygame\starship.png").convert()

# player_image.set_colorkey(WHITE)
 
# done = False
 
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True            

#     player_position = pygame.mouse.get_pos()
#     x = player_position[0]
#     y = player_position[1]
    
#     screen.fill(BLACK)  
#     screen.blit(player_image, [x, y]) 
    
#     pygame.display.flip()
    
#     clock.tick(60)

# pygame.quit()

# 2-ий варіант з фоном
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
 
screen = pygame.display.set_mode([900, 500])
 
pygame.display.set_caption('Fly')
 
clock = pygame.time.Clock()

pygame.display.update()
 
background_image = pygame.image.load(r"C:\Users\dima\Desktop\lesson8_pygame\space.png").convert()
background_image = pygame.transform.scale(background_image, [900, 500])
player_image = pygame.image.load(r"C:\Users\dima\Desktop\lesson8_pygame\starship.png").convert()

player_image.set_colorkey(WHITE)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True            

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    
    screen.blit(background_image, [0, 0]) 
    screen.blit(player_image, [x, y]) 
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()