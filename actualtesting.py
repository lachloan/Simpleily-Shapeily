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

    canvases.append(tkinter.Canvas(frameTesting, width=720, height=720))

    canvases[0].pack()

    shapes.append(canvases[0].create_rectangle(0,0,50,50, fill="black"))
    shapes.append(canvases[0].create_oval(50,50,100,100, fill="black"))





    print(shapes)
    print(canvases)
    frameTesting.pack()
    window.mainloop()



run()