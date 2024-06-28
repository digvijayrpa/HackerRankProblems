from tkinter import *

root = Tk()
root.title("Paint App")
root.geometry("1000x600")

frame1 = Frame(root, height=100, width=1100, bg="red")
frame1.grid(row=0, column=0)

frame2 = Frame(root, height=500, width=1100, bg="yellow")
frame2.grid(row=1, column=0)

canvas = Canvas(frame2, height=500, width=1100, bg="white")
canvas.grid(row=0, column=0)

canvas.create_line(100, 100, 200, 100)
canvas.create_rectangle(300, 300, 400, 400)

root.resizable(False, False)

root.mainloop()