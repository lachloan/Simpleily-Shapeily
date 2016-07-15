from tkinter import ttk
import tkinter
import database
import random

def findXCenter(canvas, item):
    coords = canvas.bbox(item)
    xOffset = (1280 / 2) - ((coords[2] - coords[0]) / 2)
    print(str(xOffset))
    return xOffset

def testClick(event):
    print("clicked!!!")

def getShapes():
    number = random.randint(0, 1)



def run():

    window = tkinter.Tk()
    window.title("Simpiley Shapeily - Game Panel")
    window.geometry("1280x720")
    window.resizable(0,0)
    window.configure(background="#64b4a9")
    ent = tkinter.Entry(window)

    frameTeacher = tkinter.Frame(window)

    shape_name = tkinter.StringVar()
    shape_name.set("test")

    label = tkinter.Label(frameTeacher, textvariable=shape_name).grid(row=1)

    shape_canvas = tkinter.Canvas(frameTeacher, width=1280, height=150, bg="#64b4a9", bd=0, highlightthickness=0, relief="ridge") #Highlightthickness removes border
    shape_canvas.grid(row=2)

    testCanvasSquare = shape_canvas.create_rectangle(0,0,150,150, fill="#fff379", outline="#64b4a9")
    testCanvasTriangle = shape_canvas.create_polygon(0, 150, 75, 0, 150, 150, fill="#fff379", outline="#64b4a9")
    testCanvasCircle = shape_canvas.create_oval(0, 0, 150, 150, fill="#fff379", outline="#64b4a9")
    testCanvasDiamond = shape_canvas.create_polygon(150,75,225,0,300,75,225,150, fill="#fff379", outline="#64b4a9")

    shape_canvas.tag_bind(testCanvasSquare, '<ButtonPress-1>', testClick)

    xOffset = findXCenter(shape_canvas, testCanvasSquare)
    shape_canvas.move(testCanvasSquare, xOffset, 0)

    getShapes()

    frameTeacher.pack()
    window.mainloop()


run()