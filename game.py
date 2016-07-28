from tkinter import ttk
import tkinter
import database
import random
import time

def run():
    global clickedcurrentlyNames, clickedcurrentlyShapes, shape_pairs, count_pairs, shapeNameCoords, calledNames, calledShapes, count_pairs

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

    calledShapes = []

    clickedcurrentlyShapes = 0
    clickedcurrentlyNames = 0

    shape_pairs = {}
    count_pairs = 0
    shapeNameCoords = {}

    calledNames = None

    def check_shapes():
        global clickedcurrentlyShapes, clickedcurrentlyNames, shape_pairs, count_pairs, calledNames, calledShapes


        if clickedcurrentlyShapes and clickedcurrentlyNames is not 0:
            shape_pairs[clickedcurrentlyNames] = clickedcurrentlyShapes
            print(shape_pairs)

            Coord_X = [270, 640, 1010]
            Coord_YS = 383
            Coord_YN = 180

            Pos_Shape = calledShapes.index(clickedcurrentlyShapes)
            Pos_Name = calledNames.index(clickedcurrentlyNames)

            if Pos_Name == Pos_Shape:
                line_canvas.create_line(Coord_X[Pos_Name], Coord_YN, Coord_X[Pos_Name], Coord_YS)

            elif Pos_Name < Pos_Shape:
                line_canvas.create_line(Coord_X[Pos_Name], Coord_YN, Coord_X[Pos_Name], Coord_YN + 40) # Down
                line_canvas.create_line(Coord_X[Pos_Name], Coord_YN + 40, Coord_X[Pos_Name] + 150, Coord_YN + 40) # Across
                line_canvas.create_line(Coord_X[Pos_Name] + 150, Coord_YN + 40, Coord_X[Pos_Name] + 150, Coord_YS - 40) # Down
                line_canvas.create_line(Coord_X[Pos_Name] + 150, Coord_YS - 40, Coord_X[Pos_Shape], Coord_YS - 40)  # Across
                line_canvas.create_line(Coord_X[Pos_Shape], Coord_YS - 40, Coord_X[Pos_Shape],Coord_YS)  # Down

            elif Pos_Name > Pos_Shape:
                line_canvas.create_line(Coord_X[Pos_Name], Coord_YN, Coord_X[Pos_Name], Coord_YN + 70)  # Down
                line_canvas.create_line(Coord_X[Pos_Name], Coord_YN + 70, Coord_X[Pos_Name] - 150, Coord_YN + 70)  # Across
                line_canvas.create_line(Coord_X[Pos_Name] - 150, Coord_YN + 70, Coord_X[Pos_Name] - 150, Coord_YS - 70)  # Down
                line_canvas.create_line(Coord_X[Pos_Name] - 150, Coord_YS - 70, Coord_X[Pos_Shape], Coord_YS - 70)  # Across
                line_canvas.create_line(Coord_X[Pos_Shape], Coord_YS - 70, Coord_X[Pos_Shape], Coord_YS)  # Down


            clickedcurrentlyShapes = 0
            clickedcurrentlyNames = 0
            count_pairs = count_pairs + 1

        if count_pairs == 3:
            matches = 0
            for key, value in shape_pairs.items():
                if key == value:
                    matches = matches + 1

            if matches == 3:
                print("All Correct")
                win()

    def generateShapes(x):
        global calledShapes
        global shape_canvas_square, shape_canvas_triangle, shape_canvas_circle, shape_canvas_diamond, shape_canvas_pentagon, shape_canvas_hexagon, shape_canvas_trapezium

        shapes_list = ['square', 'triangle', 'circle', 'diamond', 'pentagon', 'hexagon', 'trapezium']
        count = 0
        calledShapes = []
        shape_padx = 100
        shapes_shapes = []

        while count < 3: # How many shapes to display
            shape = random.choice(shapes_list)
            while shape in calledShapes: # Get unique shape (gets rid of duplicates)
                shape = random.choice(shapes_list)

            if shape == "square":
                shape_canvas_square = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                     highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_square.create_rectangle(10, 10, 160, 160, fill=shape_colour,
                                                                outline=global_background))  # Square
                shape_canvas_square.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_square.bind("<ButtonPress-1>", on_click_square)

            elif shape == "triangle":
                shape_canvas_triangle = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                       highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_triangle.create_polygon(10, 160, 85, 10, 160, 160, fill=shape_colour,
                                                                outline=global_background))
                shape_canvas_triangle.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_triangle.bind("<ButtonPress-1>", on_click_triangle)

            elif shape == "circle":
                shape_canvas_circle = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                     highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_circle.create_oval(10, 10, 160, 160, fill=shape_colour,
                                                                outline=global_background))
                shape_canvas_circle.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_circle.bind("<ButtonPress-1>", on_click_circle)

            elif shape == "diamond":
                shape_canvas_diamond = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_diamond.create_polygon(10, 85, 85, 10, 160, 85, 85, 160, fill=shape_colour,
                                                                outline=global_background))  # Diamond
                shape_canvas_diamond.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_diamond.bind("<ButtonPress-1>", on_click_diamond)

            elif shape == "pentagon":
                shape_canvas_pentagon = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_pentagon.create_polygon(85, 0, 4, 59, 35, 154, 135, 154, 166, 59, fill=shape_colour,
                                                                outline=global_background))  # Pentagon
                shape_canvas_pentagon.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_pentagon.bind("<ButtonPress-1>", on_click_pentagon)

            elif shape == "hexagon":
                shape_canvas_hexagon = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_hexagon.create_polygon(128,11,42,11,0,85,43,159,127,159,170,85, fill=shape_colour,
                                                                outline=global_background))  # Hexagon
                shape_canvas_hexagon.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_hexagon.bind("<ButtonPress-1>", on_click_hexagon)

            elif shape == "trapezium":
                shape_canvas_trapezium = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_trapezium.create_polygon(128,51,42,51,0,134.3,170,134.3,fill=shape_colour,
                                                                outline=global_background))  # Trapezium
                shape_canvas_trapezium.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_trapezium.bind("<ButtonPress-1>", on_click_trapezium)

            calledShapes.append(shape)

            count += 1

        generateNames()

    #
    # # Clicking Section
    #

    # Square Clicks

    def on_click_square_name(event):
        global name_canvas_square, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "square"
            name_square_box = name_canvas_square.create_rectangle(0,0,119,74, fill="", outline=border_colour)
            name_square_box = name_canvas_square.create_rectangle(55, 65, 65, 75, fill=border_colour, outline=border_colour)
    def on_click_square(event):
        global shape_canvas_square, clickedcurrentlyShapes

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "square"
            shape_canvas_square.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            check_shapes()

    # Circle Clicks
    def on_click_circle_name(event):
        global name_canvas_circle, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "circle"
            name_circle_box = name_canvas_circle.create_rectangle(0,0,119,74, fill="", outline=border_colour)
            name_circle_box = name_canvas_circle.create_rectangle(55,65,65,75, fill=border_colour, outline=border_colour)
    def on_click_circle(event):
        global shape_canvas_circle, clickedcurrentlyShapes

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "circle"
            shape_canvas_circle.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            check_shapes()

    # Triangle Clicks
    def on_click_triangle_name(event):
        global name_canvas_triangle, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "triangle"
            name_triangle_box = name_canvas_triangle.create_rectangle(0,0,119,74, fill="", outline=border_colour)
            name_triangle_box = name_canvas_triangle.create_rectangle(55, 65, 65, 75, fill=border_colour, outline=border_colour)
    def on_click_triangle(event):
        global shape_canvas_triangle, clickedcurrentlyShapes

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "triangle"
            shape_canvas_triangle.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            check_shapes()

    # Diamond Clicks
    def on_click_diamond_name(event):
        global name_canvas_diamond, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "diamond"
            name_diamond_box = name_canvas_diamond.create_rectangle(0,0,119,74, fill="", outline=border_colour)
            name_diamond_box = name_canvas_diamond.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                  outline=border_colour)
    def on_click_diamond(event):
        global shape_canvas_diamond, clickedcurrentlyShapes

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "diamond"
            shape_canvas_diamond.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            check_shapes()

    # Pentagon Clicks
    def on_click_pentagon_name(event):
        global name_canvas_pentagon, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "pentagon"
            name_pentagon_box = name_canvas_pentagon.create_rectangle(0,0,119,74, fill="", outline=border_colour)
            name_pentagon_box = name_canvas_pentagon.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                  outline=border_colour)
    def on_click_pentagon(event):
        global shape_canvas_pentagon, clickedcurrentlyShapes

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "pentagon"
            shape_canvas_pentagon.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            check_shapes()

    # Hexagon Clicks
    def on_click_hexagon_name(event):
        global name_canvas_hexagon, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "hexagon"
            name_hexagon_box = name_canvas_hexagon.create_rectangle(0,0,119,74, fill="", outline=border_colour)
            name_hexagon_box = name_canvas_hexagon.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                  outline=border_colour)
    def on_click_hexagon(event):
        global shape_canvas_hexagon, clickedcurrentlyShapes

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "hexagon"
            shape_canvas_hexagon.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            check_shapes()

    # Trapezium Clicks
    def on_click_trapezium_name(event):
        global name_canvas_trapezium, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "trapezium"
            name_trapezium_box = name_canvas_trapezium.create_rectangle(0,0,119,74, fill="", outline=border_colour)
            name_trapezium_box = name_canvas_trapezium.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                  outline=border_colour)
    def on_click_trapezium(event):
        global shape_canvas_trapezium, clickedcurrentlyShapes

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "trapezium"
            shape_canvas_trapezium.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            check_shapes()

    #
    # # End Clicking Section
    #

    # Generation of names for shapes
    def generateNames():
        global calledShapes, name_canvas_square, name_canvas_circle, name_canvas_diamond, name_canvas_triangle, calledNames, name_canvas_pentagon, name_canvas_hexagon
        calledNames = []
        count = 0
        print("Generating Names")
        padx = 125

        for i in calledShapes:
            count = count + 1
            name = random.choice(calledShapes)
            while name in calledNames:
                name = random.choice(calledShapes)

            calledNames.append(name)
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

            elif name == "pentagon":
                name_canvas_pentagon = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_pentagon.grid(column=count, row=1, padx=padx)
                name_pentagon = name_canvas_pentagon.create_text(60,37.5, text="Pentagon")
                name_canvas_pentagon.itemconfig(name_pentagon, font=("MyriadPro-Regular", 20), fill=text_colour)
                name_canvas_pentagon.bind("<ButtonPress-1>", on_click_pentagon_name)

            elif name == "hexagon":
                name_canvas_hexagon = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_hexagon.grid(column=count, row=1, padx=padx)
                name_hexagon = name_canvas_hexagon.create_text(60,37.5, text="Hexagon")
                name_canvas_hexagon.itemconfig(name_hexagon, font=("MyriadPro-Regular", 20), fill=text_colour)
                name_canvas_hexagon.bind("<ButtonPress-1>", on_click_hexagon_name)

            elif name == "trapezium":
                name_canvas_trapezium = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_trapezium.grid(column=count, row=1, padx=padx)
                name_trapezium = name_canvas_trapezium.create_text(60,37.5, text="Trapezium")
                name_canvas_trapezium.itemconfig(name_trapezium, font=("MyriadPro-Regular", 20), fill=text_colour)
                name_canvas_trapezium.bind("<ButtonPress-1>", on_click_trapezium_name)
                
    def win():
        global toplevel
        toplevel = tkinter.Toplevel()
        winner = tkinter.Label(toplevel, text="You won!")
        continuebutton = tkinter.Button(toplevel, text="Continue", command=toplevel.destroy)
        reset()
        winner.pack(pady = 20, padx = 10)
        continuebutton.pack(pady = 5)

    def reset():
        global count_pairs, shape_pairs

        count_pairs = 0
        shape_pairs.clear()
        line_canvas.delete("all")
        generateShapes(3)

    generateShapes(3)

    frameShapes.place(relx=.5, rely=.65, anchor="center")
    frameNames.place(relx=.5, rely=.2, anchor="center")


    window.mainloop()

run()
