import pygame  
pygame.init()

screen_width,screen_height =640,480
screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption("Drawing Shapes in triangle ") 

blue = (0, 0, 255) 

running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
# Fill background 
screen.fill(blue)
pygame.draw.polygon(screen, blue, [(300, 300), (350, 250), (400, 300), 
], 5) 
pygame.display.flip()

pygame.quit()


