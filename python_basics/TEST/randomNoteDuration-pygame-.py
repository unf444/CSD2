# Hier vertaal ik het voorbeeld van de map Assignment3 van simpleaudio naar pygame.





import pygame
import time
import random

# pygame mixer initialization for sound
pygame.mixer.init()

# Load audio files into a list using pygame.mixer.Sound
samples = [pygame.mixer.Sound("../audioFiles/Pop.wav"),
           pygame.mixer.Sound("../audioFiles/Laser1.wav"),
           pygame.mixer.Sound("../audioFiles/Dog2.wav")]

# Create a list with possible note durations: sixteenth, eighth, and a quarter note
noteDurations = [0.25, 0.5, 1]
bpm = 120

# Create a list to hold timeIntervals
timeIntervals = []

# Transform noteDurations into timeIntervals, depending on bpm
# Calculate quarterNote in seconds (duration of a quarter note)
quarterNote = 60.0 / bpm

for noteDuration in noteDurations:
    # Calculate timeDuration and add to the list
    timeIntervals.append(quarterNote * noteDuration)

# Display timeIntervals
print("Selection of time intervals: ", timeIntervals)


# A function that plays a list of samples with random timeIntervals in between,
# based on the values in the passed in interval list.
def playSamples(samples, intervals):
    # Play samples and wait in between (random duration)
    for sample in samples:
        sample.play()  # Play the sound
        # Retrieve a random timeInterval
        # Use the random.choice function -> returns a random element from a sequence
        timeInterval = random.choice(intervals)
        print("waiting: " + str(timeInterval) + " seconds.")
        # Convert timeInterval to milliseconds for pygame
        pygame.time.wait(int(timeInterval * 1000))


# Call the playSamples function 4 times
for i in range(4):
    playSamples(samples, timeIntervals)

# Quit the mixer after playing is done
pygame.mixer.quit()
