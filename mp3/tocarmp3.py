import pygame
import time

pygame.init()
pygame.mixer.music.load('fifa19.mp3')
pygame.mixer.music.play()
pygame.event.wait()

while pygame.mixer.music.get_busy():
    time.sleep(1)