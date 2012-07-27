import pygame,Utilities as util
from pygame.locals import *
#Initialize pygame and font.
pygame.init()
pygame.font.init()
font = pygame.font.Font(None,32)
#Define colors and bg
white = (255,255,255)
black = (0,0,0)
red = (255,102,73)
green = (107,255,113)
blue = (58,167,255)
magenta = (147,112,219) 
yellow = (255,244,80)
default_color = yellow
#Initialize the display surface
RESOLUTION = (SCREEN_WIDTH,SCREEN_HEIGHT) = (600,800)
screen = pygame.display.set_mode(RESOLUTION)
bg = util.Load_Image('ivybg.jpeg')
logo = util.Load_Image('logo.png',-1)
pygame.display.set_caption('Uni-Trainer')
pygame.display.set_icon(logo)
#Makes progress bars . . . all night long . . . aaaaallll right.
def draw_progress_bar(SURFACE = screen,COLOR = default_color,MAX_WIDTH = 500,MAX_QUANTITY = 1000,LOAD_QUANTITY = 1000,LOCATION = (50,300),HEIGHT = 60,BORDER_COLOR = (0,0,0)): #V
    PROGRESS = LOAD_QUANTITY/MAX_QUANTITY
    CURRENT_WIDTH = MAX_WIDTH * PROGRESS
    BAR_RECT = pygame.Rect(LOCATION[0],LOCATION[1],CURRENT_WIDTH,HEIGHT)
    BORDER_RECT = pygame.Rect(LOCATION[0],LOCATION[1],MAX_WIDTH,HEIGHT)
    pygame.draw.rect(SURFACE,white,BORDER_RECT)
    pygame.draw.rect(SURFACE,COLOR,BAR_RECT)
    BAR_BORDER_THICKNESS = 5
    pygame.draw.rect(SURFACE,BORDER_COLOR,BORDER_RECT,BAR_BORDER_THICKNESS)
def mikesFunction():
    max_quantity = 1000.0
    current_quantity = 800.0
    name = 'alpha'
    return[max_quantity,current_quantity,name]
class Color_Switchers(pygame.sprite.Sprite):
    def __init__(self,color):
        pass
#Update loop
running = True
while running:
    screen.blit(bg,(0,0))
    inports = mikesFunction()
    inports[1] -= 1.0
    
    waveName = font.render(inports[2],True,(255,255,255))
    draw_progress_bar(MAX_QUANTITY = inports[0], LOAD_QUANTITY = inports[1])
    screen.blit(waveName,(500,380))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
