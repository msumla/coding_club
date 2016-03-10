import os, sys
import pygame
from pygame.locals import *
 
import random 
 
def __main__():
    pygame.init()
    pipe = pygame.image.load("floppy-gfx/pipe.png")
    bird = pygame.image.load("floppy-gfx/bird.png") #13px X 18px per bird
    background = pygame.image.load("floppy-gfx/bg.png")


    screen = pygame.display.set_mode((800,600)) #displaying the screen with dimensions
    pygame.display.set_caption('Floppy Bird')
    pygame.mouse.set_visible(0)
        
    y = 0
    vy = 0 # vertical
        
    print("Pipe dimensions: ", pipe.get_size())
    print("Background dimensions: ", background.get_size())
    
    level = []
    
    for u in range(99):
        level.append(0) 
        level.append(0)
        level.append(random.randint(1, 3))
    
    
    antipipe = pygame.transform.flip(pipe, 0, 1)
    frames = 0 #counting the frames
    scene = pygame.Surface((240,180))
 
    while True:
        scene.fill((0)) #Fills the buffer with black pixels
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_SPACE:
                vy -= 35
        if frames % 20 == 0: #once in 100 frames
            vy += 4
            y += 1
                
        for i in range(3):
            scene.blit(background, (i*148 - (frames / 10) % 148, 0), (0, 0, 200, 300))
        frames += 1
        
        for offset, pipe_height in enumerate(level):
            if pipe_height == 0: continue # skip pipes with the height 0
            scene.blit(pipe, (400 - frames / 2 + offset * 32, 180 - pipe_height * 32), (0, 0, 100, 160))
            scene.blit(antipipe, (400 - frames / 2 + offset * 32, 180 - pipe_height * 32 - 250), (0, 0, 100, 160))
        
        scene.blit(bird, (100, 100+vy), (18 * ((frames / 100) % 3), 0, 18, 13)) #copy the bird image on the screens
        pygame.transform.scale(scene, screen.get_size(), screen) #scale it up and paste to screen
        
        pygame.display.flip()
 
if __name__ == "__main__":
    __main__()
