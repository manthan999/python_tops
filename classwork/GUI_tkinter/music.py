"""
Advanced Tkinter Music Player
- Attractive modern UI (glass-like panels, rounded buttons, subtle animations)
- Dark / Light theme toggle
- Playlist, album art, progress bar, volume
- Simple animated audio visualizer (bar-based) that reacts to playback position

Dependencies:
    pip install pygame pillow numpy

Run:
    python Advanced_Tkinter_Music_Player.py

Notes:
- This implementation uses a visualizer approximation (no heavy audio decoding).
- For more accurate waveform, integrate pydub or soundfile + numpy to read samples.
"""

import os
import threading
import time
import random
import math
from pathlib import Path
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
import pygame
import numpy as np

# -------------------- Configuration --------------------
WINDOW_W = 980
WINDOW_H = 560
BG_LIGHT = "#F6F9FF"
PANEL_LIGHT = "#FFFFFF"
TEXT_LIGHT = "#0F1724"
ACCENT = "#5A8DEE"

BG_DARK = "#0B0F1A"
PANEL_DARK = "#0E1624"
TEXT_DARK = "#E6EEF8"

# -------------------- Helper UI primitives --------------------

def rounded_rect(canvas, x1, y1, x2, y2, r=12, **kwargs):
    """Draw rounded rectangle on a canvas and return the created object ids."""
    points = [
        x1+r, y1,
        x2-r, y1,
        x2, y1,
        x2, y1+r,
        x2, y2-r,
        x2, y2,
        x2-r, y2,
        x1+r, y2,
        x1, y2,
        x1, y2-r,
        x1, y1+r,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)


class RoundButton(tk.Canvas):
    """A simple rounded button using Canvas so we can animate and style easily."""
    def __init__(self, parent, w=90, h=38, corner=12, text='', command=None, bg='#5A8DEE', fg='white', font=('Helvetica', 11, 'bold')):
        super().__init__(parent, width=w, height=h, highlightthickness=0, bg=parent['bg'])
        self.w, self.h, self.corner = w, h, corner
        self.command = command
        self.bg = bg
        self.fg = fg
        self.font = font
        self._id = rounded_rect(self, 2, 2, w-2, h-2, r=corner, fill=bg, outline='')
        self._text = self.create_text(w//2, h//2, text=text, fill=fg, font=font)
        self.bind('<Button-1>', self._on_click)
        self.bind('<Enter>', lambda e: self.scale('all', w/2, h/2, 1.03, 1.03))
        self.bind('<Leave>', lambda e: self.scale('all', w/2, h/2, 1/1.03, 1/1.03))

    def _on_click(self, _):
        if callable(self.command):
            self.command()

    def set_text(self, text):
        self.itemconfigure(self._text, text=text)

    def set_bg(self, color):
        self.itemconfigure(self._id, fill=color)


# -------------------- Music Player App --------------------
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title('Modern Music Player — Advanced UI')
        self.root.geometry(f'{WINDOW_W}x{WINDOW_H}')
        self.root.resizable(False, False)

        pygame.mixer.init()

        self.theme = 'dark'  # 'light' or 'dark'
        self.playlist = []
        self.current_index = None
        self.is_playing = False
        self.paused = False
        self.stop_flag = False

        self._build_ui()
        self._apply_theme()
        self._start_visualizer_loop()

    def _build_ui(self):
        # root background
        self.container = tk.Frame(self.root)
        self.container.pack(fill='both', expand=True)

        # Left panel - Playlist
        self.left_panel = tk.Frame(self.container, width=320)
        self.left_panel.pack(side='left', fill='y', padx=18, pady=18)

        self.left_canvas = tk.Canvas(self.left_panel, width=320, height=520, highlightthickness=0)
        self.left_canvas.pack()
        rounded_rect(self.left_canvas, 0, 0, 320, 520, r=18, fill=PANEL_DARK)

        self.lp_title = tk.Label(self.left_panel, text='Playlist', font=('Poppins', 14, 'bold'))
        self.lp_title.place(x=36, y=28)

        # Playlist listbox
        self.playlist_box = tk.Listbox(self.left_panel, activestyle='none', width=28, height=18, bd=0, highlightthickness=0)
        self.playlist_box.place(x=36, y=68)
        self.playlist_box.bind('<Double-Button-1>', lambda e: self.play_index(self.playlist_box.curselection()[0] if self.playlist_box.curselection() else 0))

        self.add_btn = RoundButton(self.left_panel, w=240, h=44, text='➕ Add Music', command=self.add_music)
        self.add_btn.place(x=36, y=420)

        # Right panel - Player
        self.right_panel = tk.Frame(self.container)
        self.right_panel.pack(side='left', fill='both', expand=True, padx=(0,18), pady=18)

        # top controls area (album art + title)
        self.top_area = tk.Frame(self.right_panel)
        self.top_area.pack(fill='x')

        # album art canvas
        self.art_size = 220
        self.art_canvas = tk.Canvas(self.top_area, width=self.art_size, height=self.art_size, highlightthickness=0)
        self.art_canvas.pack(side='left', padx=24)
        rounded_rect(self.art_canvas, 0, 0, self.art_size, self.art_size, r=20, fill='#222')

        # default album art
        self.default_art = Image.new('RGBA', (self.art_size, self.art_size), (30, 40, 60))
        self._draw_default_art(self.default_art)
        self.album_art_tk = ImageTk.PhotoImage(self.default_art)
        self.art_image_id = self.art_canvas.create_image(self.art_size//2, self.art_size//2, image=self.album_art_tk)

        # title & meta
        self.title_frame = tk.Frame(self.top_area)
        self.title_frame.pack(side='left', anchor='n', padx=12, pady=8)
        self.song_title_var = tk.StringVar(value='No song selected')
        self.song_label = tk.Label(self.title_frame, textvariable=self.song_title_var, font=('Poppins', 16, 'bold'))
        self.song_label.pack(anchor='w')

        self.meta_label = tk.Label(self.title_frame, text='— Modern Music Player', font=('Poppins', 10))
        self.meta_label.pack(anchor='w', pady=(8,0))

        # theme toggle
        self.theme_btn = RoundButton(self.title_frame, w=120, h=36, text='Toggle Theme', command=self.toggle_theme)
        self.theme_btn.pack(pady=18, anchor='w')

        # visualizer
        self.visualizer = tk.Canvas(self.right_panel, height=120, highlightthickness=0)
        self.visualizer.pack(fill='x', padx=24, pady=(12,6))

        # controls (buttons)
        self.controls_frame = tk.Frame(self.right_panel)
        self.controls_frame.pack(pady=8)

        self.prev_btn = RoundButton(self.controls_frame, w=80, h=44, text='⟨⟨', command=self.prev_track)
        self.play_btn = RoundButton(self.controls_frame, w=120, h=56, text='▶', command=self.play_pause)
        self.next_btn = RoundButton(self.controls_frame, w=80, h=44, text='⟩⟩', command=self.next_track)
        self.stop_btn = RoundButton(self.controls_frame, w=80, h=44, text='⏹', command=self.stop)

        self.prev_btn.grid(row=0, column=0, padx=8)
        self.play_btn.grid(row=0, column=1, padx=8)
        self.next_btn.grid(row=0, column=2, padx=8)
        self.stop_btn.grid(row=0, column=3, padx=8)

        # progress + volume
        self.progress_frame = tk.Frame(self.right_panel)
        self.progress_frame.pack(fill='x', padx=24, pady=(12,6))

        self.current_time_var = tk.StringVar(value='00:00')
        self.total_time_var = tk.StringVar(value='00:00')
        self.current_time_label = tk.Label(self.progress_frame, textvariable=self.current_time_var, font=('Poppins', 10))
        self.total_time_label = tk.Label(self.progress_frame, textvariable=self.total_time_var, font=('Poppins', 10))

        self.progress = ttk.Scale(self.progress_frame, from_=0, to=100, orient='horizontal', length=640, command=self._seek)
        self.current_time_label.grid(row=0, column=0, padx=(6,6))
        self.progress.grid(row=0, column=1, sticky='ew')
        self.total_time_label.grid(row=0, column=2, padx=(6,6))

        # volume control
        self.volume_frame = tk.Frame(self.right_panel)
        self.volume_frame.pack(fill='x', padx=24)
        tk.Label(self.volume_frame, text='Volume', font=('Poppins', 10)).pack(side='left')
        self.volume_slider = ttk.Scale(self.volume_frame, from_=0, to=100, orient='horizontal', length=220, command=self._set_volume)
        self.volume_slider.set(70)
        self.volume_slider.pack(side='left', padx=8)

    def _draw_default_art(self, img):
        # draw a simple placeholder album art
        from PIL import ImageDraw, ImageFont
        d = ImageDraw.Draw(img)
        w,h = img.size
        txt = "MUSIC"
        try:
            f = ImageFont.truetype('arial.ttf', 36)
        except Exception:
            f = ImageFont.load_default()
        bbox = d.textbbox((0, 0), txt, font=f)
        textw = bbox[2] - bbox[0]
        texth = bbox[3] - bbox[1]
        d.text(((w-textw)/2,(h-texth)/2), txt, fill=(200,210,230), font=f)

    # -------------------- Theme --------------------
    def _apply_theme(self):
        if self.theme == 'dark':
            bg, panel, text = BG_DARK, PANEL_DARK, TEXT_DARK
        else:
            bg, panel, text = BG_LIGHT, PANEL_LIGHT, TEXT_LIGHT

        self.root.config(bg=bg)
        self.container.config(bg=bg)
        self.left_panel.config(bg=bg)
        self.left_canvas.config(bg=bg)
        self.right_panel.config(bg=bg)
        self.top_area.config(bg=bg)
        self.title_frame.config(bg=bg)
        self.progress_frame.config(bg=bg)
        self.volume_frame.config(bg=bg)
        self.controls_frame.config(bg=bg)
        self.visualizer.config(bg=bg)

        # labels
        for lbl in (self.lp_title, self.song_label, self.meta_label, self.current_time_label, self.total_time_label):
            lbl.config(bg=bg, fg=text)

        # playlist look
        self.playlist_box.config(bg=panel, fg=text, selectbackground=ACCENT)

        # update rounded buttons
        btn_bg = ACCENT if self.theme == 'dark' else '#3B82F6'
        for b in (self.add_btn, self.theme_btn, self.prev_btn, self.play_btn, self.next_btn, self.stop_btn):
            b.set_bg(btn_bg)

    def toggle_theme(self):
        self.theme = 'light' if self.theme == 'dark' else 'dark'
        self._apply_theme()

    # -------------------- Playback --------------------
    def add_music(self):
        files = filedialog.askopenfilenames(filetypes=[('Audio', '*.mp3 *.wav *.ogg')])
        for f in files:
            self.playlist.append(f)
            self.playlist_box.insert('end', Path(f).name)
        if self.current_index is None and self.playlist:
            self.current_index = 0
            self._update_song_info()

    def _update_song_info(self):
        if self.current_index is None:
            self.song_title_var.set('No song selected')
            return
        fname = Path(self.playlist[self.current_index]).name
        self.song_title_var.set(fname)
        # try to load album art from same folder (cover.jpg/png) else default
        folder = Path(self.playlist[self.current_index]).parent
        for artname in ('cover.jpg','cover.png','album.jpg','album.png'):
            path = folder/artname
            if path.exists():
                img = Image.open(path).resize((self.art_size, self.art_size))
                img = ImageOps.fit(img, (self.art_size, self.art_size))
                self.album_art_tk = ImageTk.PhotoImage(img)
                self.art_canvas.itemconfigure(self.art_image_id, image=self.album_art_tk)
                return
        # fallback default art
        self.album_art_tk = ImageTk.PhotoImage(self.default_art)
        self.art_canvas.itemconfigure(self.art_image_id, image=self.album_art_tk)

    def play_index(self, idx):
        if idx < 0 or idx >= len(self.playlist):
            return
        self.current_index = idx
        self._play_current()

    def play_pause(self):
        if not self.playlist:
            return
        if not self.is_playing:
            self._play_current()
        else:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
                self.play_btn.set_text('⏸')
            else:
                pygame.mixer.music.pause()
                self.paused = True
                self.play_btn.set_text('▶')

    def _play_current(self):
        try:
            p = self.playlist[self.current_index]
        except Exception:
            return
        self.stop_flag = False
        pygame.mixer.music.load(p)
        pygame.mixer.music.play()
        self.is_playing = True
        self.paused = False
        self.play_btn.set_text('⏸')
        self._update_song_info()
        # attempt to estimate duration
        self._set_total_time( self._estimate_duration(p) )
        # start progress thread
        threading.Thread(target=self._progress_worker, daemon=True).start()

    def _estimate_duration(self, path):
        # best-effort: use pygame Sound if small or return 0
        try:
            s = pygame.mixer.Sound(path)
            dur = s.get_length()
            return dur
        except Exception:
            return 0

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.paused = False
        self.play_btn.set_text('▶')

    def prev_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self._play_current()

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self._play_current()

    def _set_volume(self, value):
        try:
            v = float(value)/100.0
            pygame.mixer.music.set_volume(v)
        except Exception:
            pass

    def _seek(self, value):
        # seeking with pygame.mixer.music.rewind is limited; we approximate using play(start=pos)
        try:
            if not self.is_playing:
                return
            pos = float(value)
            total = float(self.progress['to'])
            total_seconds = getattr(self, '_total_seconds', 0)
            target = (pos/100.0) * total_seconds
            # re-play from target (works for some formats)
            pygame.mixer.music.play(start=target)
        except Exception:
            pass

    def _set_total_time(self, seconds):
        self._total_seconds = seconds
        self.total_time_var.set(self._format_time(seconds))

    @staticmethod
    def _format_time(sec):
        try:
            sec = int(sec)
            m = sec//60
            s = sec%60
            return f"{m:02d}:{s:02d}"
        except Exception:
            return '00:00'

    def _progress_worker(self):
        # update progress slider and time labels while playing
        while self.is_playing and pygame.mixer.music.get_busy():
            try:
                pos_ms = pygame.mixer.music.get_pos()
                if pos_ms < 0:
                    pos_ms = 0
                pos = pos_ms/1000.0
                if getattr(self, '_total_seconds', 0) > 0:
                    pct = (pos / self._total_seconds) * 100
                else:
                    pct = 0
                self.progress.set(pct)
                self.current_time_var.set(self._format_time(pos))
            except Exception:
                pass
            time.sleep(0.5)
        # playback ended
        self.is_playing = False
        self.play_btn.set_text('▶')

    # -------------------- Visualizer --------------------
    def _start_visualizer_loop(self):
        self._vis_bars = 36
        self._bar_items = []
        self._vis_width = self.visualizer.winfo_reqwidth()
        self._vis_height = 120
        self.visualizer.delete('all')
        w = self.visualizer.winfo_reqwidth() or (WINDOW_W - 380)
        spacing = max(2, int(w / self._vis_bars))
        bar_w = spacing - 2
        for i in range(self._vis_bars):
            x = 12 + i * spacing
            item = self.visualizer.create_rectangle(x, self._vis_height, x+bar_w, self._vis_height, width=0)
            self._bar_items.append(item)
        self._update_visualizer()

    def _update_visualizer(self):
        # simple reactive bars — amplitude derived from playback position + randomness
        base = 4
        pos = pygame.mixer.music.get_pos()/1000.0 if pygame.mixer.get_init() else 0
        # when not playing, create slow breathing animation
        for i, item in enumerate(self._bar_items):
            if self.is_playing and pygame.mixer.music.get_busy():
                # simulate energy from a sin + random noise
                energy = abs(math.sin((pos + i*0.1))) * 1.0
                energy += random.uniform(0, 0.6)
            else:
                energy = 0.08 + 0.06*math.sin(time.time()*0.8 + i)
            h = int((energy) * self._vis_height)
            x1, y1, x2, y2 = self.visualizer.coords(item)
            # update coords
            self.visualizer.coords(item, x1, self._vis_height-h, x2, self._vis_height)
            # color ramp
            color_val = int(120 + energy*120)
            color = f"#{color_val:02x}{(60+int(energy*120)):02x}{255:02x}"
            self.visualizer.itemconfigure(item, fill=color)
        # schedule next frame
        self.root.after(65, self._update_visualizer)


if __name__ == '__main__':
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()