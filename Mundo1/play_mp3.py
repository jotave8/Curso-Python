#Make a python program that opens and plays the audio from an MP3 file

import pygame

pygame.init() #Starts pygame
pygame.mixer.music.load() #Enter the file name in single quotes
pygame.mixer.music.play() #Plays the music
pygame.time.delay(30000) #Makes the program stay active for the specified time
