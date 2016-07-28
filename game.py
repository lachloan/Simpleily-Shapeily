import tkinter, random, time
from tkinter import ttk

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

    def getChecked():
        global clickedcurrentlyShapes, clickedcurrentlyNames, pairsShape, pairsCount, calledNames, calledShapes


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
                    print("fucked up")
                    losercount.set("Win count: " + str(wincount))
                    frameLoser.lift()
                    break

            if matches == 3:
                putWin()

    def getShapes(x):
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

        getNames()

    def getNames():
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
                canvasSquare_name.bind("<ButtonPress-1>", on_click_square_name)


            elif name == "circle":
                canvasCircle_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                   highlightthickness=0, relief="ridge")
                canvasCircle_name.grid(column=count, row=1, padx=padx)
                name_circle = canvasCircle_name.create_text(60, 37.5, text="Circle")
                canvasCircle_name.itemconfig(name_circle, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasCircle_name.bind("<ButtonPress-1>", on_click_circle_name)

            elif name == "triangle":
                canvasTriangle_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                     highlightthickness=0, relief="ridge")
                canvasTriangle_name.grid(column=count, row=1, padx=padx)
                name_triangle = canvasTriangle_name.create_text(60, 37.5, text="Triangle")
                canvasTriangle_name.itemconfig(name_triangle, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasTriangle_name.bind("<ButtonPress-1>", on_click_triangle_name)

            elif name == "diamond":
                canvasDiamond_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                canvasDiamond_name.grid(column=count, row=1, padx=padx)
                name_diamond = canvasDiamond_name.create_text(60, 37.5, text="Diamond")
                canvasDiamond_name.itemconfig(name_diamond, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasDiamond_name.bind("<ButtonPress-1>", on_click_diamond_name)

            elif name == "pentagon":
                canvasPentagon_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                     highlightthickness=0, relief="ridge")
                canvasPentagon_name.grid(column=count, row=1, padx=padx)
                name_pentagon = canvasPentagon_name.create_text(60, 37.5, text="Pentagon")
                canvasPentagon_name.itemconfig(name_pentagon, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasPentagon_name.bind("<ButtonPress-1>", on_click_pentagon_name)

            elif name == "hexagon":
                canvasHexagon_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                canvasHexagon_name.grid(column=count, row=1, padx=padx)
                name_hexagon = canvasHexagon_name.create_text(60, 37.5, text="Hexagon")
                canvasHexagon_name.itemconfig(name_hexagon, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasHexagon_name.bind("<ButtonPress-1>", on_click_hexagon_name)

            elif name == "trapezium":
                canvasTrapezium_name = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                canvasTrapezium_name.grid(column=count, row=1, padx=padx)
                name_trapezium = canvasTrapezium_name.create_text(60, 37.5, text="Trapezium")
                canvasTrapezium_name.itemconfig(name_trapezium, font=("MyriadPro-Regular", 20), fill=text_colour)
                canvasTrapezium_name.bind("<ButtonPress-1>", on_click_trapezium_name)

    #
    # # Clicking Section
    #

    # Square Clicks
    def on_click_square_name(event):
        global canvasSquare_name, clickedcurrentlyNames
        frameWinner.lower()

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "square"
            name_square_box = canvasSquare_name.create_rectangle(0, 0, 119, 74, fill="", outline=border_colour)
            name_square_box = canvasSquare_name.create_rectangle(55, 65, 65, 75, fill=border_colour, outline=border_colour)
    def on_click_square(event):
        global shape_canvas_square, clickedcurrentlyShapes
        frameWinner.lower()

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "square"
            shape_canvas_square.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            getChecked()

    # Circle Clicks
    def on_click_circle_name(event):
        global canvasCircle_name, clickedcurrentlyNames
        frameWinner.lower()

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "circle"
            name_circle_box = canvasCircle_name.create_rectangle(0, 0, 119, 74, fill="", outline=border_colour)
            name_circle_box = canvasCircle_name.create_rectangle(55, 65, 65, 75, fill=border_colour, outline=border_colour)
    def on_click_circle(event):
        global shape_canvas_circle, clickedcurrentlyShapes
        frameWinner.lower()

        if clickedcurrentlyNames == 0:
            return

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "circle"
            shape_canvas_circle.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            getChecked()

    # Triangle Clicks
    def on_click_triangle_name(event):
        global canvasTriangle_name, clickedcurrentlyNames
        frameWinner.lower()

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "triangle"
            name_triangle_box = canvasTriangle_name.create_rectangle(0, 0, 119, 74, fill="", outline=border_colour)
            name_triangle_box = canvasTriangle_name.create_rectangle(55, 65, 65, 75, fill=border_colour, outline=border_colour)
    def on_click_triangle(event):
        global shape_canvas_triangle, clickedcurrentlyShapes
        frameWinner.lower()

        if clickedcurrentlyNames == 0:
            return

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "triangle"
            shape_canvas_triangle.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            getChecked()

    # Diamond Clicks
    def on_click_diamond_name(event):
        global canvasDiamond_name, clickedcurrentlyNames
        frameWinner.lower()

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "diamond"
            name_diamond_box = canvasDiamond_name.create_rectangle(0, 0, 119, 74, fill="", outline=border_colour)
            name_diamond_box = canvasDiamond_name.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                   outline=border_colour)
    def on_click_diamond(event):
        global shape_canvas_diamond, clickedcurrentlyShapes
        frameWinner.lower()

        if clickedcurrentlyNames == 0:
            return

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "diamond"
            shape_canvas_diamond.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            getChecked()

    # Pentagon Clicks
    def on_click_pentagon_name(event):
        global canvasPentagon_name, clickedcurrentlyNames
        frameWinner.lower()

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "pentagon"
            name_pentagon_box = canvasPentagon_name.create_rectangle(0, 0, 119, 74, fill="", outline=border_colour)
            name_pentagon_box = canvasPentagon_name.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                     outline=border_colour)
    def on_click_pentagon(event):
        global shape_canvas_pentagon, clickedcurrentlyShapes
        frameWinner.lower()

        if clickedcurrentlyNames == 0:
            return

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "pentagon"
            shape_canvas_pentagon.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            getChecked()

    # Hexagon Clicks
    def on_click_hexagon_name(event):
        global canvasHexagon_name, clickedcurrentlyNames
        frameWinner.lower()

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "hexagon"
            name_hexagon_box = canvasHexagon_name.create_rectangle(0, 0, 119, 74, fill="", outline=border_colour)
            name_hexagon_box = canvasHexagon_name.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                   outline=border_colour)
    def on_click_hexagon(event):
        global shape_canvas_hexagon, clickedcurrentlyShapes
        frameWinner.lower()

        if clickedcurrentlyNames == 0:
            return

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "hexagon"
            shape_canvas_hexagon.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            getChecked()

    # Trapezium Clicks
    def on_click_trapezium_name(event):
        global canvasTrapezium_name, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "trapezium"
            name_trapezium_box = canvasTrapezium_name.create_rectangle(0, 0, 119, 74, fill="", outline=border_colour)
            name_trapezium_box = canvasTrapezium_name.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                       outline=border_colour)
    def on_click_trapezium(event):
        global shape_canvas_trapezium, clickedcurrentlyShapes

        if clickedcurrentlyNames == 0:
            return

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "trapezium"
            shape_canvas_trapezium.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            getChecked()

    #
    # # End Clicking Section
    #


    def putWin():
        global wincountNumber, wincount

        getReset()
        wincount = wincount + 1
        wincountNumber.set("Wins: " + str(wincount))

        frameWinner.lift()



    def getReset():
        global pairsCount, pairsShape, wincountNumber, wincount

        pairsCount = 0
        pairsShape.clear()
        line_canvas.delete("all")
        frameWinner.lower()
        frameLoser.lower()

        wincountNumber.set("Wins: 0")
        wincount = 0


        getShapes(3)

    getShapes(3)

    frameShapes.place(relx=.5, rely=.65, anchor="center")
    frameNames.place(relx=.5, rely=.2, anchor="center")
    frameWincount.place(relx=.05, rely=.05, anchor="center")
    frameWinner.place(relx=.5, rely=.5, anchor="center")
    frameLoser.place(relx=.5, rely=.5, anchor="center")
    frameWinner.lower()
    frameLoser.lower()

    window.mainloop()

run()
