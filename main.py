import tkinter as tk
from tkinter import *
import time


def start_typing():
    title_label.grid_forget()
    label.grid_forget()
    start_button.grid_forget()
    label_type = tk.Label(text="Start Typing...", font=("Arial", 20, "normal"))
    label_type.grid(column=0, row=0, columnspan=2)
    typing_area.grid(column=0, row=1, pady=20)
    typing_area.focus_set()
    typing_area.bind("<KeyPress>", start_typing_words)


def start_typing_words(event=None):
    global typing_timer
    # Cancel the existing timer if any
    if typing_timer is not None:
        windows.after_cancel(typing_timer)
    # Start a new timer for 5 seconds
    typing_timer = windows.after(5000, on_typing_stopped)


def on_typing_stopped():
    current_text = typing_area.get("1.0", "end-1c")  # Get the current text
    if current_text:  # If there is still text
        typing_area.delete(f"1.0")  # Delete the first character
        # Call this function again after a short delay (e.g., 100ms)
        windows.after(100, on_typing_stopped)


windows = Tk()
windows.title("The Most Dangerous Writing App")
windows.config(pady=100, padx=100, width=800, height=800)
typing_timer = None
title_label = tk.Label(text="The most Dangerous Writing App", font=("Ariel", 30, "bold"))
title_label.grid(column=0, row=0, columnspan=3)
label = tk.Label(text="Don’t stop writing, or all progress will be lost.", font=("Ariel", 18, "normal"))
label.grid(column=0, row=1, columnspan=3, pady=20)
start_button = tk.Button(text="Starting Typing", command=start_typing, font=("Arial", 12, "normal"))
start_button.grid(column=1, row=2, pady=40)
default_bg_color = windows["bg"]
typing_area = Text(windows,bg=default_bg_color, borderwidth=0, highlightthickness=0,font=("Arial", 14))

windows.mainloop()