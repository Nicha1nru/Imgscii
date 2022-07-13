import tkinter as tk
from tkinter import filedialog, Text
import os
import PIL.Image

root = tk.Tk()

path1 = tk.Entry(root)
path1.pack()

def doConvert():
    img_flag = True
    path = path1.get()

    try:
        img = PIL.Image.open(path)
        img_flag = True
    except:
        labelError = tk.Label(root, text="Error path not found")
        labelError.pack()

    width, height = img.size
    aspect_ratio = height/width
    new_width = 150
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))

    img = img.convert('L')

    chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]

    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    with open("ascii_image.txt", "w") as f:
      f.write(ascii_image)

    ascii = tk.Label(root, text=ascii_image)
    ascii.pack()

startConvert = tk.Button(root, text="Convert", padx=10, pady=5, fg="black", bg="white", command = doConvert)
startConvert.pack()

root.mainloop()