from tkinter import ttk
import tkinter
import database
import random

def run():
    global_background = "#EFF0D1"
    shape_colour = "#77BA99"

    window = tkinter.Tk()
    window.title("Simpiley Shapeily - Game Panel")
    window.geometry("1280x720")
    window.resizable(0,0)
    window.configure(background="white")
    ent = tkinter.Entry(window)

    line_canvas = tkinter.Canvas(window, width=1280, height=720, bg=global_background)
    line_canvas.pack()

    frameShapes = tkinter.Frame(window, bg=global_background)
    frameNames = tkinter.Frame(window, bg=global_background)

    shapes_called = []

    def generateShapes(x):
        global shapes_called

        shapes_list = ['square', 'triangle', 'circle', 'diamond']
        count = 0
        shapes_called = []
        shape_padx = 100

        while count < 3: # How many shapes to display
            shape = random.choice(shapes_list)
            while shape in shapes_called: # Get unique shape (gets rid of duplicates)
                shape = random.choice(shapes_list)

            if shape == "square":
                shape_canvas_square = tkinter.Canvas(frameShapes, width=150, height=150, bg=global_background, bd=0,
                                                     highlightthickness=0, relief="ridge")
                shape_square = shape_canvas_square.create_rectangle(0, 0, 150, 150, fill=shape_colour,
                                                                outline=global_background)  # Square
                shape_canvas_square.grid(row=1, column=count, padx=shape_padx)

            elif shape == "triangle":
                shape_canvas_triangle = tkinter.Canvas(frameShapes, width=150, height=150, bg=global_background, bd=0,
                                                       highlightthickness=0, relief="ridge")
                shape_triangle = shape_canvas_triangle.create_polygon(0, 150, 75, 0, 150, 150, fill=shape_colour,
                                                                outline=global_background)  # Triangle
                shape_canvas_triangle.grid(row=1, column=count, padx=shape_padx)

            elif shape == "circle":
                shape_canvas_circle = tkinter.Canvas(frameShapes, width=150, height=150, bg=global_background, bd=0,
                                                     highlightthickness=0, relief="ridge")
                shape_circle = shape_canvas_circle.create_oval(0, 0, 150, 150, fill=shape_colour,
                                                                outline=global_background)  # Circle
                shape_canvas_circle.grid(row=1, column=count, padx=shape_padx)

            elif shape == "diamond":
                shape_canvas_diamond = tkinter.Canvas(frameShapes, width=150, height=150, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shape_diamond = shape_canvas_diamond.create_polygon(0, 75, 75, 0, 150, 75, 75, 150, fill=shape_colour,
                                                                outline=global_background)  # Diamond
                shape_canvas_diamond.grid(row=1, column=count, padx=shape_padx)

            shapes_called.append(shape)
            print(shapes_called)

            count += 1

        print(shapes_called)
        generateNames()

    def onClick(event):
        print("clicked")
        generateShapes(3)

    def generateNames():
        global shapes_called, name_canvas_square, name_canvas_circle, name_canvas_diamond, name_canvas_triangle
        name_called = []
        count = 0
        print("Generating Names")

        for i in shapes_called:
            count = count + 1
            name = random.choice(shapes_called)
            while name in name_called:
                name = random.choice(shapes_called)

            name_called.append(name)
            if name == "square":
                name_canvas_square = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_square.grid(column=count, row=1, padx=114)
                name_square = name_canvas_square.create_text(60,37.5, text="Square")
                name_canvas_square.itemconfig(name_square, font=("MyriadPro-Regular", 20,))
                name_canvas_square.bind(clickHold)

            elif name == "circle":
                name_canvas_circle = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_circle.grid(column=count, row=1, padx=114)
                name_circle = name_canvas_circle.create_text(60,37.5, text="Circle")
                name_canvas_circle.itemconfig(name_circle, font=("MyriadPro-Regular", 20))
                name_canvas_circle.bind(clickHold)

            elif name == "triangle":
                name_canvas_triangle = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_triangle.grid(column=count, row=1, padx=114)
                name_triangle = name_canvas_triangle.create_text(60,37.5, text="Triangle")
                name_canvas_triangle.itemconfig(name_triangle, font=("MyriadPro-Regular", 20))
                name_canvas_triangle.bind(clickHold)

            elif name == "diamond":
                name_canvas_diamond = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_diamond.grid(column=count, row=1, padx=114)
                name_diamond = name_canvas_diamond.create_text(60,37.5, text="Diamond")
                name_canvas_diamond.itemconfig(name_diamond, font=("MyriadPro-Regular", 20))
                name_canvas_diamond.bind(clickHold)

            print(name_called)
            print(count)

    generateShapes(3)



    start_x = None
    start_y = None

    def clickHold(event):
        global start_y, start_x

        print("Running click")
        start_x = event.x
        start_y = event.y

        point_start = line_canvas.create_rectangle(start_x - 10, start_y - 10, start_x + 10, start_y + 10, fill="black")

    def clickRelease(event):
        global start_y, start_x

        end_x = event.x
        end_y = event.y

        line = line_canvas.create_line(start_x, start_y, end_x, end_y, fill="black")
        point_end = line_canvas.create_rectangle(end_x - 10, end_y - 10, end_x + 10, end_y + 10, fill="black")

    start_x = None


    frameShapes.place(relx=.5, rely=.65, anchor="center")
    frameNames.place(relx=.5, rely=.2, anchor="center")
    window.mainloop()

run()