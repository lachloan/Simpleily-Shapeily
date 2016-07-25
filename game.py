from tkinter import ttk
import tkinter
import database
import random

def run():
    global_background = "#C1CDCD"
    shape_colour = "#808098"
    text_colour = "#3A4161"
    border_colour = "#808098"

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
        global shape_canvas_square, shape_canvas_triangle, shape_canvas_circle, shape_canvas_diamond

        shapes_list = ['square', 'triangle', 'circle', 'diamond']
        count = 0
        shapes_called = []
        shape_padx = 100

        while count < 3: # How many shapes to display
            shape = random.choice(shapes_list)
            while shape in shapes_called: # Get unique shape (gets rid of duplicates)
                shape = random.choice(shapes_list)

            if shape == "square":
                shape_canvas_square = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                     highlightthickness=0, relief="ridge")
                shape_square = shape_canvas_square.create_rectangle(10, 10, 160, 160, fill=shape_colour,
                                                                outline=global_background)  # Square
                shape_canvas_square.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_square.bind("<ButtonPress-1>", on_click_square)

            elif shape == "triangle":
                shape_canvas_triangle = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                       highlightthickness=0, relief="ridge")
                shape_triangle = shape_canvas_triangle.create_polygon(10, 160, 85, 10, 160, 160, fill=shape_colour,
                                                                outline=global_background)  # Triangle
                shape_canvas_triangle.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_triangle.bind("<ButtonPress-1>", on_click_triangle)

            elif shape == "circle":
                shape_canvas_circle = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                     highlightthickness=0, relief="ridge")
                shape_circle = shape_canvas_circle.create_oval(10, 10, 160, 160, fill=shape_colour,
                                                                outline=global_background)  # Circle
                shape_canvas_circle.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_circle.bind("<ButtonPress-1>", on_click_circle)

            elif shape == "diamond":
                shape_canvas_diamond = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shape_diamond = shape_canvas_diamond.create_polygon(10, 85, 85, 10, 160, 85, 85, 160, fill=shape_colour,
                                                                outline=global_background)  # Diamond
                shape_canvas_diamond.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_diamond.bind("<ButtonPress-1>", on_click_diamond)

            shapes_called.append(shape)
            print(shapes_called)

            count += 1

        print(shapes_called)
        generateNames()

    def on_click_square_name(event):
        global name_canvas_square
        print("clicked square")
        name_square_box = name_canvas_square.create_rectangle(0,0,119,74, fill="", outline=border_colour)
        name_square_box = name_canvas_square.create_rectangle(55, 65, 65, 75, fill=border_colour, outline=border_colour)

    def on_click_square(event):
        global shape_canvas_square
        shape_canvas_square.create_rectangle(0,0,169,169, fill="", outline=border_colour)

    def on_click_circle_name(event):
        global name_canvas_circle
        print("clicked circle")
        name_circle_box = name_canvas_circle.create_rectangle(0,0,119,74, fill="", outline=border_colour)
        name_circle_box = name_canvas_circle.create_rectangle(55,65,65,75, fill=border_colour, outline=border_colour)


    def on_click_circle(event):
        global shape_canvas_circle
        shape_canvas_circle.create_rectangle(0,0,169,169, fill="", outline=border_colour)

    def on_click_triangle_name(event):
        global name_canvas_triangle
        print("clicked triangle")
        name_triangle_box = name_canvas_triangle.create_rectangle(0,0,119,74, fill="", outline=border_colour)
        name_triangle_box = name_canvas_triangle.create_rectangle(55, 65, 65, 75, fill=border_colour, outline=border_colour)

    def on_click_triangle(event):
        global shape_canvas_triangle
        shape_canvas_triangle.create_rectangle(0,0,169,169, fill="", outline=border_colour)

    def on_click_diamond_name(event):
        global name_canvas_diamond
        print("clicked diamond")
        name_diamond_box = name_canvas_diamond.create_rectangle(0,0,119,74, fill="", outline=border_colour)
        name_diamond_box = name_canvas_diamond.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                  outline=border_colour)

    def on_click_diamond(event):
        global shape_canvas_diamond
        shape_canvas_diamond.create_rectangle(0,0,169,169, fill="", outline=border_colour)




    def generateNames():
        global shapes_called, name_canvas_square, name_canvas_circle, name_canvas_diamond, name_canvas_triangle
        name_called = []
        count = 0
        print("Generating Names")
        padx = 127

        for i in shapes_called:
            count = count + 1
            name = random.choice(shapes_called)
            while name in name_called:
                name = random.choice(shapes_called)

            name_called.append(name)
            if name == "square":
                name_canvas_square = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_square.grid(column=count, row=1, padx=padx)
                name_square = name_canvas_square.create_text(60,37.5, text="Square")
                name_canvas_square.itemconfig(name_square, font=("MyriadPro-Regular", 20,), fill=text_colour)
                name_canvas_square.bind("<ButtonPress-1>", on_click_square_name)

            elif name == "circle":
                name_canvas_circle = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_circle.grid(column=count, row=1, padx=padx)
                name_circle = name_canvas_circle.create_text(60,37.5, text="Circle")
                name_canvas_circle.itemconfig(name_circle, font=("MyriadPro-Regular", 20), fill=text_colour)
                name_canvas_circle.bind("<ButtonPress-1>", on_click_circle_name)

            elif name == "triangle":
                name_canvas_triangle = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_triangle.grid(column=count, row=1, padx=padx)
                name_triangle = name_canvas_triangle.create_text(60,37.5, text="Triangle")
                name_canvas_triangle.itemconfig(name_triangle, font=("MyriadPro-Regular", 20), fill=text_colour)
                name_canvas_triangle.bind("<ButtonPress-1>", on_click_triangle_name)

            elif name == "diamond":
                name_canvas_diamond = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_diamond.grid(column=count, row=1, padx=padx)
                name_diamond = name_canvas_diamond.create_text(60,37.5, text="Diamond")
                name_canvas_diamond.itemconfig(name_diamond, font=("MyriadPro-Regular", 20), fill=text_colour)
                name_canvas_diamond.bind("<ButtonPress-1>", on_click_diamond_name)

            print(name_called)
            print(count)

    generateShapes(3)



    start_x = None
    start_y = None


    start_x = None


    frameShapes.place(relx=.5, rely=.65, anchor="center")
    frameNames.place(relx=.5, rely=.2, anchor="center")


    window.mainloop()

run()