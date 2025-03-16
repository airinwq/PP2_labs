Часы
import pygame
import math
import time

pygame.init()

width = 700
height = 500
center = (width // 2, height // 2)

screen = pygame.display.set_mode((width, height))

img_clock = pygame.image.load("clock.png")
img_clock = pygame.transform.scale(img_clock, (width, height))

img_min_hand = pygame.image.load("min_hand.png")
img_min_hand = pygame.transform.scale(img_min_hand, (750, 300))

img_sec_hand = pygame.image.load("sec_hand.png")
img_sec_hand = pygame.transform.scale(img_sec_hand, (600, 300))

running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(img_clock, (0, 0))
    
    current_time = time.localtime()
    minutes = current_time.tm_min 
    seconds = current_time.tm_sec 
    
    min_angle = (minutes % 60) * 6 + 60
    sec_angle = (seconds % 60) * 6 - 50
    
    rotate_min_hand = pygame.transform.rotate(img_min_hand, -min_angle)
    rotate_sec_hand = pygame.transform.rotate(img_sec_hand, -sec_angle)
    
    rect_min = rotate_min_hand.get_rect(center=center)
    rect_sec = rotate_sec_hand.get_rect(center=center)
    
    screen.blit(rotate_min_hand,  rect_min.topleft)
    screen.blit(rotate_sec_hand, rect_sec.topleft)
    
    pygame.display.flip()
    clock.tick(60) 

Музыка
import pygame

pygame.init()

width, height = 500, 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

# songs
songs = ["AI_People.mp3", "Price_tag.mp3", "Cheap_Thrills.mp3"]
index = 0

pygame.mixer.music.load(songs[index])
pygame.mixer.music.play()

pygame.mixer.music.set_endevent(pygame.USEREVENT)

paused = False

def next_song():
    global index
    index = (index + 1) % len(songs)
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()

def prev_song():
    global index
    index = (index - 1) % len(songs)
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause() 
                paused = not paused

            if event.key == pygame.K_LEFT:
                next_song()

            if event.key == pygame.K_RIGHT:
                    prev_song()
        
        if event.type == pygame.USEREVENT:
            next_song()
    
    
    screen.fill("lightgreen")
    pygame.display.flip()
    clock.tick(60)

Мяч
import pygame

pygame.init()

width, height = 700, 500
x = width // 2
y = height // 2
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
radius = 25

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y - radius > 0:
        y -= 20

    if keys[pygame.K_DOWN] and y + radius < height:
        y += 20

    if keys[pygame.K_RIGHT] and x + radius < width:
        x += 20

    if keys[pygame.K_LEFT] and  x - radius > 0:
        x -= 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()
    clock.tick(60)