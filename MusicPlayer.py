import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("400x100")

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Track and play status variables
        self.playing = False
        self.track_path = ""

        # Create UI elements
        self.label = tk.Label(root, text="Choose a song to play:")
        self.label.pack(pady=10)

        self.btn_play = tk.Button(root, text="Play", command=self.play_music)
        self.btn_play.pack(side=tk.LEFT, padx=5)

        self.btn_pause = tk.Button(root, text="Pause", command=self.pause_music, state=tk.DISABLED)
        self.btn_pause.pack(side=tk.LEFT, padx=5)

        self.btn_stop = tk.Button(root, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.btn_stop.pack(side=tk.LEFT, padx=5)

        self.btn_browse = tk.Button(root, text="Browse", command=self.browse_file)
        self.btn_browse.pack(side=tk.LEFT, padx=5)

    def browse_file(self):
        # Allow user to select a music file
        self.track_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if self.track_path:
            self.label.config(text="Selected: " + os.path.basename(self.track_path))
            self.btn_play.config(state=tk.NORMAL)
            self.btn_pause.config(state=tk.NORMAL)
            self.btn_stop.config(state=tk.NORMAL)

    def play_music(self):
        # Play the selected music
        if self.track_path:
            pygame.mixer.music.load(self.track_path)
            pygame.mixer.music.play()
            self.playing = True
            self.label.config(text="Now playing: " + os.path.basename(self.track_path))
            self.btn_play.config(state=tk.DISABLED)
            self.btn_pause.config(state=tk.NORMAL)
            self.btn_stop.config(state=tk.NORMAL)

    def pause_music(self):
        # Pause or unpause the music
        if self.playing:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                self.playing = False
                self.label.config(text="Paused: " + os.path.basename(self.track_path))
                self.btn_pause.config(text="Unpause")
            else:
                pygame.mixer.music.unpause()
                self.playing = True
                self.label.config(text="Now playing: " + os.path.basename(self.track_path))
                self.btn_pause.config(text="Pause")

    def stop_music(self):
        # Stop the music
        if self.playing:
            pygame.mixer.music.stop()
            self.playing = False
            self.label.config(text="Stopped: " + os.path.basename(self.track_path))
            self.btn_play.config(state=tk.NORMAL)
            self.btn_pause.config(state=tk.DISABLED)
            self.btn_stop.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
