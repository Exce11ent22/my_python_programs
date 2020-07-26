from tkinter import *
import time

root = Tk()

canvas = Canvas(root, width = 500, height = 500, bg = "white")
canvas.pack()

canvas.create_rectangle(10, 10, 50, 50, fill = "green")