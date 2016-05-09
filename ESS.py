import os
import pygame
import time
import sys
import webbrowser
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

size = width, height = 1280, 720
speed = [2, 2]
white = 255, 255, 255

screen = pygame.display.set_mode(size)
#uncomment to set fullscreen
#pygame.display.set_mode((1280,720),pygame.FULLSCREEN)
Netflix = pygame.image.load(os.path.join('C:\Users\kauch\OneDrive\Programs\ESS', 'Netflix.png'))
Netrect = Netflix.get_rect()
Netflix1 = 0

Photos = pygame.image.load(os.path.join('C:\Users\kauch\OneDrive\Programs\ESS', 'Photos.png'))
Phorect = Photos.get_rect()
Phorect.move_ip(250,0)
Photos1 = 0

Chrome = pygame.image.load(os.path.join('C:\Users\kauch\OneDrive\Programs\ESS', 'chrome.jpg'))
Chrect = Chrome.get_rect()
Chrect.move_ip(500,0)
Chrome1 = 0

iTunes = pygame.image.load(os.path.join('C:\Users\kauch\OneDrive\Programs\ESS', 'iTunes.jpg'))
iRect = iTunes.get_rect()
iRect.move_ip(750,0)
iTunes1 = 0

Xbox = pygame.image.load(os.path.join('C:\Users\kauch\OneDrive\Programs\ESS', 'xbox.png'))
Xrect = Xbox.get_rect()
Xrect.move_ip(1000, 0)
Xbox1 = 0

VLC = pygame.image.load(os.path.join('C:/Users/kauch/OneDrive/Programs/ESS', 'vlc.png'))
Vrect = VLC.get_rect()
Vrect.move_ip(0, 250)
VLC1 = 0

Steam = pygame.image.load(os.path.join('C:\Users\kauch\OneDrive\Programs\ESS', 'steam.png'))
Sterect = Steam.get_rect()
Sterect.move_ip(250, 250)
Steam1 = 0

Unity = pygame.image.load(os.path.join('C:/Users/kauch/OneDrive/Programs/ESS', 'unity.png'))
Urect = Unity.get_rect()
Urect.move_ip(500, 250)
U1 = 0

Firefox = pygame.image.load(os.path.join('C:/Users/kauch/OneDrive/Programs/ESS', 'firefox.jpg'))
Firect = Unity.get_rect()
Firect.move_ip(750, 250)
Fi1 = 0

Swa = pygame.image.load(os.path.join('C:/Users/kauch/OneDrive/Programs/ESS', 'swa.jpg'))
Swarect = Unity.get_rect()
Swarect.move_ip(1000, 250)
Swa1 = 0

GE = pygame.image.load(os.path.join('C:/Users/kauch/OneDrive/Programs/ESS', 'GE.png'))
Grect = GE.get_rect()
Grect.move_ip(0, 500)
GE1 = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(white)
    screen.blit(Netflix, Netrect)
    screen.blit(Photos, (250,0))
    screen.blit(Chrome, Chrect)
    screen.blit(iTunes, iRect)
    screen.blit(Xbox, Xrect)
    screen.blit(VLC, Vrect)
    screen.blit(Steam, Sterect)
    screen.blit(Unity, Urect)
    screen.blit(Firefox, Firect)
    screen.blit(Swa, Swarect)
    screen.blit(GE, Grect)
    pygame.display.flip()
    if pygame.mouse.get_pressed()[0] and Netrect.collidepoint(pygame.mouse.get_pos()):
        os.system('start netflix:')
        time.sleep(5)

    if pygame.mouse.get_pressed()[0] and Phorect.collidepoint(pygame.mouse.get_pos()):
        if Netflix1 != 1:
            os.system('start ms-photos:')
            time.sleep(5)
        Netflix1 = 1
    if pygame.mouse.get_pressed()[0] and Chrect.collidepoint(pygame.mouse.get_pos()):
        if Chrome1 != 1:
            os.system('start chrome')
            time.sleep(5)
        Chrome1 = 1
    if pygame.mouse.get_pressed()[0] and iRect.collidepoint(pygame.mouse.get_pos()):
        if iTunes1 != 1:
            os.system('start iTunes')
            time.sleep(5)
        iTunes1 = 1
    if pygame.mouse.get_pressed()[0] and Xrect.collidepoint(pygame.mouse.get_pos()):
        if Xbox1 != 1:
            os.system('start Xbox:')
            time.sleep(5)
        Xbox1 = 1
    if pygame.mouse.get_pressed()[0] and Vrect.collidepoint(pygame.mouse.get_pos()):
        if VLC1 != 1:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN\VLC media player')
            time.sleep(5)
        VLC1 = 1
    if pygame.mouse.get_pressed()[0] and Sterect.collidepoint(pygame.mouse.get_pos()):
        if Steam1 != 1:
            os.system('start Steam:')
            time.sleep(5)
        Steam1 = 1
    event = pygame.event.wait ()
    if pygame.mouse.get_pressed()[0] and Urect.collidepoint(pygame.mouse.get_pos()):
        if U1 != 1:
            os.startfile('C:\Program Files\Unity\Editor\Unity')
            time.sleep(5)
        U1 = 1
    if pygame.mouse.get_pressed()[0] and Firect.collidepoint(pygame.mouse.get_pos()):
        if Fi1 != 1:
            os.system('start firefox')
            time.sleep(5)
        Fi1 = 1
    if pygame.mouse.get_pressed()[0] and Swarect.collidepoint(pygame.mouse.get_pos()):
        if Swa1 != 1:
            webbrowser.open_new('http://www.asciimation.co.nz/')
            time.sleep(5)
        Swa1 = 1
    if pygame.mouse.get_pressed()[0] and Grect.collidepoint(pygame.mouse.get_pos()):
        if GE1 != 1:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Earth')
            time.sleep(5)
        GE1 = 1
    
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            break       
        

        
        
