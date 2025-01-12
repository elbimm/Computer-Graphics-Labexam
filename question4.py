import pygame 
pygame.init()
canvas = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Myboard")
running=True 
while not running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
           running = False
        elif event.type== K_ESCAPE: # type: ignore
            print("Escape")
    canvas.fill((255, 255, 255)) 
    pygame.display.flip() 

 
pygame.quit() 