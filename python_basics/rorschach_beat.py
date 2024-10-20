import pygame
import time
import random
from midiutil import MIDIFile  # For MIDI export

# Initialize pygame mixer
pygame.mixer.init()

# Load sound files
kick_sound = pygame.mixer.Sound("kick.wav")
snare_sound = pygame.mixer.Sound("snare.wav")
hihat_sound = pygame.mixer.Sound("hihat.wav")

# Get user input with time signature limits
def get_user_input():
    bpm = int(input("Enter the BPM (Beats Per Minute): "))
    
    time_signature_top = int(input("Enter the top number of the time signature (1-16): "))
    if time_signature_top < 1 or time_signature_top > 16:
        print("The top number must be between 1 and 16.")
        return None
    
    time_signature_bottom = int(input("Enter the bottom number of the time signature (1-16, e.g., 4 for 4/4): "))
    if time_signature_bottom < 1 or time_signature_bottom > 16:
        print("The bottom number must be between 1 and 16.")
        return None
    
    length_in_steps = int(input("Enter the number of steps (length of the beat): "))
    
    # Ask the number of times to repeat the generated beat
    repeat_times = int(input("Enter the number of times to repeat the beat: "))
    
    return bpm, time_signature_top, time_signature_bottom, length_in_steps, repeat_times

# Calculate interval based on time signature
def calculate_interval(bpm, time_signature_bottom):
    note_value = 4 / time_signature_bottom  # 4 = quarter notes, 8 = eighth notes, etc.
    return (60.0 / bpm) * note_value

# Generate basic kick/snare/hihat pattern
def generate_pattern(length_in_steps, beats_per_measure):
    kick_pattern = [random.choice([0, 1]) for _ in range(length_in_steps)]
    snare_pattern = [random.choice([0, 1]) for _ in range(length_in_steps)]
    hihat_pattern = [random.choice([0, 1]) for _ in range(length_in_steps)]
    
    return kick_pattern, snare_pattern, hihat_pattern

# Play the pattern
def play_pattern(kick_pattern, snare_pattern, hihat_pattern, interval, repeat_times):
    for _ in range(repeat_times):
        for i in range(len(kick_pattern)):
            if kick_pattern[i] == 1:
                kick_sound.play()
            if snare_pattern[i] == 1:
                snare_sound.play()
            if hihat_pattern[i] == 1:
                hihat_sound.play()
            
            time.sleep(interval)

# Function to export the pattern to MIDI (without glitches for now)
def export_to_midi(kick_pattern, snare_pattern, hihat_pattern, bpm, file_name):
    midi = MIDIFile(1)  # One track
    track = 0
    time = 0    # Start at the beginning
    midi.addTrackName(track, time, "Beat")
    midi.addTempo(track, time, bpm)
    
    # Add kick pattern to MIDI
    for i, hit in enumerate(kick_pattern):
        if hit == 1:
            midi.addNote(track, 9, 36, i * (60.0 / bpm), 0.5, 100)  # MIDI note for kick is 36
    
    # Add snare pattern to MIDI
    for i, hit in enumerate(snare_pattern):
        if hit == 1:
            midi.addNote(track, 9, 38, i * (60.0 / bpm), 0.5, 100)  # MIDI note for snare is 38
    
    # Add hihat pattern to MIDI
    for i, hit in enumerate(hihat_pattern):
        if hit == 1:
            midi.addNote(track, 9, 42, i * (60.0 / bpm), 0.5, 100)  # MIDI note for hihat is 42
    
    # Write the MIDI file to disk with the user-specified name
    with open(f"{file_name}.mid", "wb") as output_file:
        midi.writeFile(output_file)
    print(f"MIDI file saved as '{file_name}.mid'")

# Main function
def main():
    user_input = get_user_input()
    if user_input is None:
        return
    
    bpm, time_signature_top, time_signature_bottom, length_in_steps, repeat_times = user_input
    
    # Calculate the time between beats
    interval = calculate_interval(bpm, time_signature_bottom)
    
    # Generate patterns
    kick_pattern, snare_pattern, hihat_pattern = generate_pattern(length_in_steps, time_signature_top)
    
    # Play the generated pattern
    print("Playing the beat...")
    play_pattern(kick_pattern, snare_pattern, hihat_pattern, interval, repeat_times)
    
    # Ask if the user wants to save the beat as a MIDI file
    save_midi = input("Do you want to save the original generated beat as a MIDI file? (yes/no): ").lower()
    
    if save_midi == 'yes':
        file_name = input("What would you like to name the MIDI file? ")
        export_to_midi(kick_pattern, snare_pattern, hihat_pattern, bpm, file_name)

if __name__ == "__main__":
    main()
