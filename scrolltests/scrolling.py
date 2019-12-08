import tkinter as tk
from tkinter import ttk

root = tk.Tk()
canvas = tk.Canvas(root)
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

frame = tk.Frame(canvas)

tk.Label(frame, text="मिति:").grid(row = 0, column = 0)
tk.Entry(frame).grid(row=0, column=1)

tk.Label(frame, text="नागरिकता नं.: ").grid(row=0, column=3)
tk.Entry(frame).grid(row=0, column=4)

frame.columnconfigure(2, minsize=440)

## Put the frame into the canvas
canvas.create_window(0, 0, anchor="nw", window=frame)
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)

canvas.pack(fill="both", expand=True, side="left")
scroll_y.pack(fill="y", side="right")

root.geometry("850x900")
root.mainloop()