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

    shapes = []
    canvases = []

    canvas.create_polygon(150,75,113,10,38,10,0,75,37,140,112,140, fill="black")





    print(shapes)
    print(canvases)
    frameTesting.pack()
    window.mainloop()



run()