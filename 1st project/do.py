import tkinter as tk
from tkinter import filedialog
import pygame

def initialize_music_player():
    pygame.mixer.init()

def add_to_playlist():
    file_paths = filedialog.askopenfilenames(filetypes=[("Audio files", "*.mp3")])
    for file_path in file_paths:
        playlist.append(file_path)
        playlist_box.insert(tk.END, file_path)

def play_music():
    if not playlist:
        tk.messagebox.showerror("Error", "Playlist is empty! Add some music to the playlist.")
        return

    selected_index = playlist_box.curselection()
    if not selected_index:
        selected_index = 0
    else:
        selected_index = selected_index[0]

    file_path = playlist[selected_index]

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def skip_next():
    if not playlist:
        tk.messagebox.showerror("Error", "Playlist is empty! Add some music to the playlist.")
        return

    selected_index = playlist_box.curselection()
    if not selected_index:
        selected_index = 0
    else:
        selected_index = selected_index[0]

    selected_index = (selected_index + 1) % len(playlist)
    playlist_box.selection_clear(0, tk.END)
    playlist_box.selection_set(selected_index)
    play_music()

# Create the main application window
root = tk.Tk()
root.title("Music Player")

# Initialize the music player
initialize_music_player()

# Create a playlist to store file paths
playlist = []

# Create a listbox widget to display the playlist
playlist_box = tk.Listbox(root, selectmode=tk.SINGLE)
playlist_box.pack(expand=True, fill="both")

# Create buttons for various actions
add_button = tk.Button(root, text="Add to Playlist", command=add_to_playlist)
add_button.pack(pady=5)

play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=5)

pause_button = tk.Button(root, text="Pause", command=pause_music)
pause_button.pack(pady=5)

unpause_button = tk.Button(root, text="Unpause", command=unpause_music)
unpause_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=5)

skip_button = tk.Button(root, text="Skip Next", command=skip_next)
skip_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
