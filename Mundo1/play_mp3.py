#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3

import pygame

pygame.init() #Inicia o pygame
pygame.mixer.music.load() #Inserir o nome do arquivo entre aspas simples
pygame.mixer.music.play() #Toca a música
pygame.time.delay(30000) #Faz o programa continuar ativo pelo tempo determinado