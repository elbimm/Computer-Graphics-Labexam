import pygame 
pygame.init()
screen_width, screen_height = 640, 480 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Myboard")
red=(255,0,0)
white=(255,255,255)
running=True 
while not running:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
           running = False
        elif event.type== K_ESCAPE: # type: ignore
            print("Escape")
    screen.fill(white) 
pygame.draw.line(screen,red,(0,0),(50,50),3,)
pygame.display.flip() 
pygame.time.wait(20)
 
pygame.quit() 