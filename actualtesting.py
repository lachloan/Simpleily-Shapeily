from tkinter import ttk
import tkinter
import database

def run():
    global window, start_x, start_y, canvas

    window = tkinter.Tk()
    window.title("Simpiley Shapeily - Testing Panel")
    window.geometry("720x720")
    window.resizable(0,0)
    ent = tkinter.Entry(window)

    frameTesting = tkinter.Frame(window)

    canvas = tkinter.Canvas(frameTesting, width=720, height=720)

    canvas.pack()

    window.bind("<ButtonPress-1>", clickHold)
    window.bind("<ButtonRelease-1>", clickRelease)

    start_x = None
    start_y = None

    frameTesting.pack()
    window.mainloop()

def clickHold(event):
    global start_y, start_x

    print("Running click")
    start_x = event.x
    start_y = event.y

    point_start = canvas.create_rectangle(1, 100, 2, 90, fill="black")

def clickRelease(event):
    global start_y, start_x

    end_x = event.x
    end_y = event.y

    line = canvas.create_line(start_x, start_y, end_x, end_y,fill="black")
    point_end = canvas.create_rectangle(end_x - 10, end_y - 10, end_x + 10, end_y + 10, fill="black")


run()