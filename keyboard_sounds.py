import keyboard
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the sound file
SOUND_FOLDER = 'sounds'
SOUND_FILE = 'main.mp3'  
sound_effect = pygame.mixer.Sound(f"{SOUND_FOLDER}/{SOUND_FILE}")

def play_sound(e):
    if e.event_type == keyboard.KEY_DOWN:  # Ensure the event is a key press
        sound_effect.play()

# Hook every key
keyboard.hook(play_sound)

# Keep the program running
keyboard.wait('esc')