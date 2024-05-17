import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

image_objects = []

def create_window(title, image_source, start_x=None, start_y=None):
    window = tk.Toplevel(root)
    window.title(title)
    window.overrideredirect(True)  
  
    if start_x is not None and start_y is not None:
        window.geometry(f"+{start_x}+{start_y}")

    # Dragging functionality
    def start_move(event):
        window.x = event.x
        window.y = event.y

    def on_move(event):
        deltax = event.x - window.x
        deltay = event.y - window.y
        x = window.winfo_x() + deltax
        y = window.winfo_y() + deltay
        window.geometry(f"+{x}+{y}")

    window.bind("<ButtonPress-1>", start_move)
    window.bind("<B1-Motion>", on_move)

    top_bar = tk.Frame(window, bg="black", relief=tk.FLAT, bd=0)
    top_bar.pack(fill=tk.X)

    tk.Label(top_bar, text=title, fg="white", bg="black", padx=10).pack(side=tk.LEFT)
    tk.Button(top_bar, text="X", command=window.destroy, bg="black", fg="white", bd=0, padx=5).pack(side=tk.RIGHT)

    gif = Image.open(image_source)
    frames = []
    for frame in ImageSequence.Iterator(gif):
        frames.append(ImageTk.PhotoImage(frame))
    label = tk.Label(window)
    label.frames = frames  
    label.pack()

    def display_frame(frame_index):
        if frame_index >= len(frames):
            frame_index = 0
        label.config(image=frames[frame_index])
        window.after(100, display_frame, frame_index + 1)

    display_frame(0)

    image_objects.extend(frames)

root = tk.Tk()
root.title("Main Window")

create_window("Access Denied", "./assets/access_deny.gif", start_x=100, start_y=100)
create_window("Scripts", "./assets/scripts.gif", start_x=200, start_y=200)
create_window("Malware Upload", "./assets/uploading_malware.gif", start_x=300, start_y=300)

root.withdraw()
root.mainloop()
