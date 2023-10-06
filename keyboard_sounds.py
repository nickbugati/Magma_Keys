import keyboard
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load sound files
SOUND_FOLDER = 'sounds'
SOUNDS = {}

# A basic set of keys to track. Adjust this list based on your needs
keys_to_track = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    # ... add any other keys you have sound effects for
]

for key in keys_to_track:
    try:
        sound_path = f"{SOUND_FOLDER}/{key}.mp3"
        SOUNDS[key] = pygame.mixer.Sound(sound_path)
    except:
        print(f"Couldn't load sound for {key}")

def play_sound(e):
    if e.event_type == keyboard.KEY_DOWN:  # Ensure the event is a key press
        key = e.name
        if key in SOUNDS:
            SOUNDS[key].play()

# Hook every key
keyboard.hook(play_sound)

# Keep the program running
keyboard.wait('esc')
