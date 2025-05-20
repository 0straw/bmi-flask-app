import pyautogui
import random
import time

# Song list - you can replace these with full file paths or track IDs
song_files = [
    "C:/Music/song1.mp3",
    "C:/Music/song2.mp3",
    "C:/Music/song3.mp3",
    "C:/Music/song4.mp3"
]

def open_song(song_path):
    # Simulates pressing Ctrl+O to open file dialog
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(2)
    
    # Types the path
    pyautogui.write(song_path)
    time.sleep(1)

    # Press Enter
    pyautogui.press('enter')
    time.sleep(3)

def play_song():
    # Clicks the play button – set exact coordinates
    pyautogui.click(x=500, y=700)  # Replace with actual coordinates of Play
    time.sleep(2)

def stop_song():
    # Click stop button – set exact coordinates
    pyautogui.click(x=550, y=700)  # Replace with actual coordinates of Stop
    time.sleep(1)

def random_mix_loop(interval=30):
    while True:
        stop_song()
        song = random.choice(song_files)
        open_song(song)
        play_song()
        time.sleep(interval)

# Start mixing
print("Starting Virtual DJ Mixing Bot...")
time.sleep(5)  # Give user time to switch to VDJ
random_mix_loop(interval=60)  # Change every 60 seconds
