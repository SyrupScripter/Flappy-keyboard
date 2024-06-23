import pygame
import string #losowe literki
string.ascii_letters
import random #gdzie literki wyswietlane
import time #score

pygame.display.set_caption('Flappy osu keyboard bird??')

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2 - 280, screen.get_height() / 2)

base_font = pygame.font.Font(None, 32) 
user_text = '' 
input_rect = pygame.Rect(200, 200, 140, 32) 

color = pygame.Color('chartreuse4') 

jump = False #mechanika skakania
blokada = False #mechanika blokady skoku (bo nie wiedzialem jak zrobic zeby nie trza bylo trzymac)
klawisz_odblk = 'a'
start = False #czy ma zaczac sie frajda :)
score = -1

pygame.mouse.set_visible(0) #widocznosc kursora

#tekst
font = pygame.font.Font('freesansbold.ttf', 42)
text = font.render('<SPACE>', True, (0, 255, 0), (0, 0, 128))
textRect = text.get_rect()
textRect.center = (screen.get_width() / 2, screen.get_width() / 2) 

#tutorial
font2 = pygame.font.Font('freesansbold.ttf', 24)
text2 = font2.render('press space than, the key that appears to be albe to press space again', True, (0, 204, 153), (51, 153, 102))
textRect2 = text2.get_rect()
textRect2.center = (screen.get_width() / 2, screen.get_width() / 2 + 40)

while running:
    # poll for events
    # pygame.QUIT - > kliknięcie X na window
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            screen.fill("black")
            running = False
        if event.type == pygame.KEYDOWN:    #bierze input, jaki klawisz
            user_text = event.unicode
            if user_text == klawisz_odblk:
                blokada = False
                text = font.render("", True, "white", "dark green")


    #tlo
    screen.fill("light green")
    
    #rury
    r1 = pygame.draw.rect(screen, color, pygame.Rect(300, 500, 120, 200))
    r2 = pygame.draw.rect(screen, color, pygame.Rect(300, 30, 120, 200))
    p1 = pygame.draw.rect(screen, "light gray", pygame.Rect(280, 470, 160, 60))
    p2 = pygame.draw.rect(screen, "light gray", pygame.Rect(280, 210, 160, 60))
  
    #player
    pygame.draw.circle(screen, "yellow", player_pos, 40)

    #opadanie
    if(jump != True and start == True):
        player_pos.y += 40 * dt    

    #skakanie
    if(jump == True):
        for i in range(3):
            player_pos.y -= 800 * dt
        blokada = True
        klawisz_odblk = random.choice(string.ascii_letters).lower()
        textRect.center = (screen.get_width() / 2 + 200 + random.randrange(200), screen.get_width() / 2 - 500 + random.randrange(200))
        text = font.render(" " + klawisz_odblk + " ", True, "white", "dark green")
        #print(klawisz_odblk)
        jump = False
    
    
    screen.blit(text, textRect)

    if start == False:
        screen.blit(text2, textRect2)
    
    if pygame.Rect.collidepoint(p1, int(player_pos.x), int(player_pos.y)+30) == True:
        break
    elif pygame.Rect.collidepoint(p2, int(player_pos.x), int(player_pos.y)-30) == True:
        break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and blokada == False:    
        if start == False:
            start = True
        else:
            jump = True
            score += 1
    
    #flip() the display to put your work on screen        
    pygame.display.flip()

    dt = clock.tick(60) / 1000  #fps limit -> 60

#score fix
score = str(score)
score = "score: " + score

#score display
screen.fill("dark green")
text = font.render(score, True, "white", "dark green")
screen.blit(text, textRect)
pygame.display.flip()
time.sleep(3)
    
pygame.quit()
