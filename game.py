from tkinter import ttk
import tkinter
import database
import random

global_background = "#64b4a9"

window = tkinter.Tk()
window.title("Simpiley Shapeily - Game Panel")
window.geometry("1280x720")
window.resizable(0,0)
window.configure(background=global_background)
ent = tkinter.Entry(window)

frameTeacher = tkinter.Frame(window, bg=global_background)

shape_name = tkinter.StringVar()
shape_name.set("test")


def findXCenter(canvas, item):
    coords = canvas.bbox(item)
    xOffset = (1280 / 2) - ((coords[2] - coords[0]) / 2)
    print(str(xOffset))
    return xOffset

def clickShape(event):
    print("clicked!!!")




label = tkinter.Label(frameTeacher, textvariable=shape_name).grid(row=1)





def generateShapes(x):
    shapes_list = ['square', 'triangle', 'circle', 'diamond']
    count = 0
    shapes_called = []
    shape_padx = 25

    while count < 3: # How many shapes to display
        print("running count" + str(count))
        shape = random.choice(shapes_list)
        while shape in shapes_called: # Get unique shape (gets rid of duplicates)
            shape = random.choice(shapes_list)

        if shape == "square":
            shape_canvas_square = tkinter.Canvas(frameTeacher, width=150, height=150, bg=global_background, bd=0,
                                                 highlightthickness=0, relief="ridge")
            shape_square = shape_canvas_square.create_rectangle(0, 0, 150, 150, fill="#fff379",
                                                            outline=global_background)  # Square
            shape_canvas_square.grid(row=1, column=count, padx=shape_padx)

        elif shape == "triangle":
            shape_canvas_triangle = tkinter.Canvas(frameTeacher, width=150, height=150, bg=global_background, bd=0,
                                                   highlightthickness=0, relief="ridge")
            shape_triangle = shape_canvas_triangle.create_polygon(0, 150, 75, 0, 150, 150, fill="#fff379",
                                                            outline=global_background)  # Triangle
            shape_canvas_triangle.grid(row=1, column=count, padx=shape_padx)

        elif shape == "circle":
            shape_canvas_circle = tkinter.Canvas(frameTeacher, width=150, height=150, bg=global_background, bd=0,
                                                 highlightthickness=0, relief="ridge")
            shape_circle = shape_canvas_circle.create_oval(0, 0, 150, 150, fill="#fff379",
                                                            outline=global_background)  # Circle
            shape_canvas_circle.grid(row=1, column=count, padx=shape_padx)

        elif shape == "diamond":
            shape_canvas_diamond = tkinter.Canvas(frameTeacher, width=150, height=150, bg=global_background, bd=0,
                                                  highlightthickness=0, relief="ridge")
            shape_diamond = shape_canvas_diamond.create_polygon(0, 75, 75, 0, 150, 75, 75, 150, fill="#fff379",
                                                            outline=global_background)  # Diamond
            shape_canvas_diamond.grid(row=1, column=count, padx=shape_padx)

        shapes_called.append(shape)
        print(shapes_called)

        count += 1


generateShapes(3)

frameTeacher.pack()
window.mainloop()
