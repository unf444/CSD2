import pygame
import time

playBacktimes = int(input("Please enter the playback amount: "))


pygame.mixer.init()


pygame.mixer.music.load("noise.wav")


pygame.mixer.music.set_volume(0.5)

sound_length = pygame.mixer.Sound("noise.wav").get_length()

pygame.mixer.music.play(loops=playBacktimes - 1)


time.sleep(sound_length * playBacktimes)

