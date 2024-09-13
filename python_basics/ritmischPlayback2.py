import pygame
import time


numPlaybackTimes = int(input("Number of playbacks: "))


rhythm = []


for i in range(numPlaybackTimes):
    note_duration = float(input(f"Enter the note duration for playback {i+1} : "))
    rhythm.append(note_duration)


bpm = float(input("Enter the BPM: "))
seconds_per_beat = 60 / bpm  


pygame.mixer.init()


pygame.mixer.music.load("sound.wav")

pygame.mixer.music.set_volume(0.5)


for i in range(numPlaybackTimes):
    pygame.mixer.music.play()
    
    time.sleep(rhythm[i] * seconds_per_beat)
