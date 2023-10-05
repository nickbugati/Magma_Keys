import keyboard
from pydub import AudioSegment
from pydub.playback import play
import threading  # Import the threading module

# Load sound files
SOUND_FOLDER = 'sounds'
SOUNDS = {}

# A basic set of keys to track. Adjust this list based on your needs
keys_to_track = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'space', 'enter', 'backspace', 'tab', 'esc', 'ctrl', 'alt', 'shift',
    # ... add any other keys you have sound effects for
]

for key in keys_to_track:
    try:
        sound_path = f"{SOUND_FOLDER}/{key}.mp3"
        SOUNDS[key] = AudioSegment.from_mp3(sound_path)
    except:
        print(f"Couldn't load sound for {key}")

def threaded_play(sound):  # Function to play sound in a separate thread
    play(sound)

def play_sound(e):
    if e.event_type == keyboard.KEY_DOWN:  # Ensure the event is a key press
        key = e.name
        if key in SOUNDS:
            threading.Thread(target=threaded_play, args=(SOUNDS[key],)).start()  # Start a new thread to play the sound

# Hook every key
keyboard.hook(play_sound)

# Keep the program running
keyboard.wait('esc')