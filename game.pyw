import tkinter, random, time
from tkinter import ttk

border_colour = "#808098"

def run():
    global clickedcurrentlyNames, clickedcurrentlyShapes, pairsShape, pairsCount, calledNames, calledShapes, wincountNumber, wincount, losercount

    global_background = "#C1CDCD"
    shape_colour = "#808098"
    text_colour = "#3A4161"
    border_colour = "#808098"

    wincount = 0
    calledShapes = []
    clickedcurrentlyShapes = 0
    clickedcurrentlyNames = 0
    pairsShape = {}
    pairsCount = 0
    calledNames = None

    window = tkinter.Tk()
    window.title("Simpiley Shapeily - Game Panel")
    window.geometry("1280x720")
    window.resizable(0,0)
    window.configure(background="white")
    ent = tkinter.Entry(window)

    # Canvas for connecting lines
    line_canvas = tkinter.Canvas(window, width=1280, height=720, bg=global_background)
    line_canvas.pack()

    # Frames for shapes/names
    frameShapes = tkinter.Frame(window, bg=global_background)
    frameNames = tkinter.Frame(window, bg=global_background)

    # Setting up the winner screen
    wincountNumber = tkinter.StringVar()
    frameWincount = tkinter.Frame(window, bg=global_background)
    wincountLabelNumber = tkinter.Label(frameWincount, textvariable=wincountNumber, background=global_background, font=("MyriadPro-Regular", 15)).grid(column=2)
    wincountNumber.set("Wins: 0")

    frameWinner = tkinter.Frame(window, bg="white", height="5")
    winnerCanvas = tkinter.Canvas(frameWinner, width=500, height=300, bg="white")
    winnerLabel = tkinter.Label(frameWinner, text="Congratulations, you won!!", background="white", font=("MyriadPro-Regular", 15)).place(rely = 0.5, relx = .5, anchor="center")
    winnerLabelsub = tkinter.Label(frameWinner, textvariable=wincountNumber, background="white", font=("MyriadPro-Regular", 15)).place(rely = 0.6, relx = .5, anchor="center")
    winnerButton = ttk.Button(frameWinner, text="Continue", command=lambda:frameWinner.lower()).place(rely = 0.7, relx = .5, anchor="center")

    winnerImage = tkinter.PhotoImage(
        file='resources\\winnerBackground.gif')
    winnerCanvas.create_image(0, 0, image=winnerImage, anchor="nw")
    winnerCanvas.pack()

    # Setting up loser screen
    losercount = tkinter.StringVar()
    losercount.set("Win count:")

    frameLoser = tkinter.Frame(window, bg="white", height="5")
    loserCanvas = tkinter.Canvas(frameLoser, width=500, height=300, bg="white")
    loserLabel = tkinter.Label(frameLoser, text="Sorry, you lost!", background="white",font=("MyriadPro-Regular", 15)).place(rely=0.5, relx=.5, anchor="center")
    loserLabelsub = tkinter.Label(frameLoser, textvariable=losercount, background="white",font=("MyriadPro-Regular", 15)).place(rely=0.6, relx=.5, anchor="center")
    loserButton = ttk.Button(frameLoser, text="Continue", command=lambda: getReset()).place(rely=0.7,relx=.5, anchor="center")

    loserImage = tkinter.PhotoImage(
        file='resources\\winnerBackground.gif')
    loserCanvas.create_image(0, 0, image=loserImage, anchor="nw")
    loserCanvas.pack()

    def check_pairs():
        global clickedcurrentlyShapes, clickedcurrentlyNames, pairsShape, pairsCount, calledNames, calledShapes, wincount


        if clickedcurrentlyShapes and clickedcurrentlyNames is not 0:
            pairsShape[clickedcurrentlyNames] = clickedcurrentlyShapes

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
            pairsCount = pairsCount + 1

        if pairsCount == 3:
            matches = 0
            for key, value in pairsShape.items():
                if key == value:
                    matches = matches + 1

                else:
                    losercount.set("Win count: " + str(wincount))
                    frameLoser.lift()

                    wincountNumber.set("Wins: 0")
                    wincount = 0
                    break

            if matches == 3:
                putWin()

    def get_shapes(x):
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
                shape_canvas_square.bind("<ButtonPress-1>", lambda x: on_click("shape", "square"))

            elif shape == "triangle":
                shape_canvas_triangle = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                       highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_triangle.create_polygon(10, 160, 85, 10, 160, 160, fill=shape_colour,
                                                                outline=global_background))
                shape_canvas_triangle.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_triangle.bind("<ButtonPress-1>", lambda x: on_click("shape", "triangle"))

            elif shape == "circle":
                shape_canvas_circle = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                     highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_circle.create_oval(10, 10, 160, 160, fill=shape_colour,
                                                                outline=global_background))
                shape_canvas_circle.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_circle.bind("<ButtonPress-1>", lambda x: on_click("shape", "circle"))

            elif shape == "diamond":
                shape_canvas_diamond = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_diamond.create_polygon(10, 85, 85, 10, 160, 85, 85, 160, fill=shape_colour,
                                                                outline=global_background))  # Diamond
                shape_canvas_diamond.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_diamond.bind("<ButtonPress-1>", lambda x: on_click("shape", "diamond"))

            elif shape == "pentagon":
                shape_canvas_pentagon = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_pentagon.create_polygon(85, 0, 4, 59, 35, 154, 135, 154, 166, 59, fill=shape_colour,
                                                                outline=global_background))  # Pentagon
                shape_canvas_pentagon.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_pentagon.bind("<ButtonPress-1>", lambda x: on_click("shape", "pentagon"))

            elif shape == "hexagon":
                shape_canvas_hexagon = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_hexagon.create_polygon(128,11,42,11,0,85,43,159,127,159,170,85, fill=shape_colour,
                                                                outline=global_background))  # Hexagon
                shape_canvas_hexagon.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_hexagon.bind("<ButtonPress-1>", lambda x: on_click("shape", "hexagon"))

            elif shape == "trapezium":
                shape_canvas_trapezium = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_trapezium.create_polygon(128,51,42,51,0,134.3,170,134.3,fill=shape_colour,
                                                                outline=global_background))  # Trapezium
                shape_canvas_trapezium.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_trapezium.bind("<ButtonPress-1>", lambda x: on_click("shape", "trapezium"))

            calledShapes.append(shape)

            count += 1

        get_names()

    def get_names():
        global calledShapes, calledNames
        global canvasSquare_name, canvasCircle_name, canvasDiamond_name, canvasTriangle_name, canvasPentagon_name, canvasHexagon_name, canvasTrapezium_name
        calledNames = []
        count = 0
        padx = 125

        for i in calledShapes:
            count = count + 1
            name = random.choice(calledShapes)
            while name in calledNames:
                name = random.choice(calledShapes)

            calledNames.append(name)
            if name == "square":
                canvasSquare_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                   highlightthickness=0, relief="ridge")
                canvasSquare_name.grid(column=count, row=1, padx=padx)
                name_square = canvasSquare_name.create_text(60, 37.5, text="Square")
                canvasSquare_name.itemconfig(name_square, font=("MyriadPro-Regular", 20,), fill=text_colour)
                canvasSquare_name.bind("<ButtonPress-1>", lambda x: on_click("name", "square"))


            elif name == "circle":
                canvasCircle_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                   highlightthickness=0, relief="ridge")
                canvasCircle_name.grid(column=count, row=1, padx=padx)
                name_circle = canvasCircle_name.create_text(60, 37.5, text="Circle")
                canvasCircle_name.itemconfig(name_circle, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasCircle_name.bind("<ButtonPress-1>", lambda x: on_click("name", "circle"))

            elif name == "triangle":
                canvasTriangle_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                     highlightthickness=0, relief="ridge")
                canvasTriangle_name.grid(column=count, row=1, padx=padx)
                name_triangle = canvasTriangle_name.create_text(60, 37.5, text="Triangle")
                canvasTriangle_name.itemconfig(name_triangle, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasTriangle_name.bind("<ButtonPress-1>", lambda x: on_click("name", "triangle"))

            elif name == "diamond":
                canvasDiamond_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                canvasDiamond_name.grid(column=count, row=1, padx=padx)
                name_diamond = canvasDiamond_name.create_text(60, 37.5, text="Diamond")
                canvasDiamond_name.itemconfig(name_diamond, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasDiamond_name.bind("<ButtonPress-1>", lambda x: on_click("name", "diamond"))

            elif name == "pentagon":
                canvasPentagon_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                     highlightthickness=0, relief="ridge")
                canvasPentagon_name.grid(column=count, row=1, padx=padx)
                name_pentagon = canvasPentagon_name.create_text(60, 37.5, text="Pentagon")
                canvasPentagon_name.itemconfig(name_pentagon, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasPentagon_name.bind("<ButtonPress-1>", lambda x: on_click("name", "pentagon"))

            elif name == "hexagon":
                canvasHexagon_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                canvasHexagon_name.grid(column=count, row=1, padx=padx)
                name_hexagon = canvasHexagon_name.create_text(60, 37.5, text="Hexagon")
                canvasHexagon_name.itemconfig(name_hexagon, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasHexagon_name.bind("<ButtonPress-1>", lambda x: on_click("name", "hexagon"))

            elif name == "trapezium":
                canvasTrapezium_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                canvasTrapezium_name.grid(column=count, row=1, padx=padx)
                name_trapezium = canvasTrapezium_name.create_text(60, 37.5, text="Trapezium")
                canvasTrapezium_name.itemconfig(name_trapezium, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasTrapezium_name.bind("<ButtonPress-1>", lambda x: on_click("name", "trapezium"))

                

    #
    # # Clicking Section
    #
    def on_click(type, shape):
        global clickedcurrentlyNames
        frameWinner.lower()

        if type == "name":
            if clickedcurrentlyNames == 0:
                clickedcurrentlyNames = shape
                exec('name_' + shape + '_box = canvas' + shape.title() + '_name.create_rectangle(0, 0, 119, 74, fill="", outline=border_colour)')
                exec('name_' + shape + '_box = canvas' + shape.title() + '_name.create_rectangle(55, 65, 65, 75, fill="#808098", outline=border_colour)')

        elif type == "shape":
            global clickedcurrentlyShapes
            frameWinner.lower()

            if clickedcurrentlyShapes == 0:
                clickedcurrentlyShapes = shape
                exec('shape_canvas_' + shape + '.create_rectangle(0,0,169,169, fill="", outline=border_colour)')
                check_pairs()

    #
    # # End Clicking Section
    #


    def putWin():
        global wincountNumber, wincount

        getReset()
        wincount = wincount + 1
        print(str(wincount))
        wincountNumber.set("Wins: " + str(wincount))
        frameWinner.lift()



    def getReset():
        global pairsCount, pairsShape, wincountNumber, wincount

        pairsCount = 0
        pairsShape.clear()
        line_canvas.delete("all")
        frameWinner.lower()
        frameLoser.lower()


        get_shapes(3)

    get_shapes(3)

    frameShapes.place(relx=.5, rely=.65, anchor="center")
    frameNames.place(relx=.5, rely=.2, anchor="center")
    frameWincount.place(relx=.05, rely=.05, anchor="center")
    frameWinner.place(relx=.5, rely=.5, anchor="center")
    frameLoser.place(relx=.5, rely=.5, anchor="center")
    frameWinner.lower()
    frameLoser.lower()

    window.mainloop()

run()
