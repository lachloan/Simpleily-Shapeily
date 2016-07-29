import tkinter, random, time
from tkinter import ttk

border_colour = "#808098"

def run():
    global clickedcurrentlyNames, clickedcurrentlyShapes, pairsShape, pairsCount, calledNames, calledShapes, wincountNumber, wincount, losercount
    global names_canvases, names_text, names_boxes
    global shapes_canvases, shapes_boxes, shapes_shapes


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

    names_canvases = {}
    names_text = {}
    names_boxes = {}

    shapes_canvases = {}
    shapes_shapes = {}
    shapes_boxes = {}

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
        global shapes_canvases, shapes_shapes


        shapes_list = ['square', 'triangle', 'circle', 'diamond', 'pentagon', 'hexagon', 'trapezium']
        count = 0
        calledShapes = []
        shape_padx = 100

        while count < 3: # How many shapes to display
            shape = random.choice(shapes_list)
            while shape in calledShapes: # Get unique shape (gets rid of duplicates)
                shape = random.choice(shapes_list)


            shapes_canvases[shape] = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
            shapes_canvases[shape].grid(row=1, column=count, padx=shape_padx)


            if shape == "square":
                shapes_shapes[shape] = (shapes_canvases[shape].create_rectangle(10, 10, 160, 160, fill=shape_colour,
                                                                                outline=global_background))  # Square
                shapes_canvases[shape].bind("<ButtonPress-1>", lambda x: on_click("shape", "square"))

            elif shape == "triangle":
                shapes_shapes[shape] = (shapes_canvases[shape].create_polygon(10, 160, 85, 10, 160, 160, fill=shape_colour,
                                                                              outline=global_background))
                shapes_canvases[shape].bind("<ButtonPress-1>", lambda x: on_click("shape", "triangle"))

            elif shape == "circle":
                shapes_shapes[shape] = (shapes_canvases[shape].create_oval(10, 10, 160, 160, fill=shape_colour,
                                                                           outline=global_background))
                shapes_canvases[shape].bind("<ButtonPress-1>", lambda x: on_click("shape", "circle"))

            elif shape == "diamond":
                shapes_shapes[shape] = (shapes_canvases[shape].create_polygon(10, 85, 85, 10, 160, 85, 85, 160, fill=shape_colour,
                                                                              outline=global_background))  # Diamond
                shapes_canvases[shape].bind("<ButtonPress-1>", lambda x: on_click("shape", "diamond"))

            elif shape == "pentagon":
                shapes_shapes[shape] = (shapes_canvases[shape].create_polygon(85, 0, 4, 59, 35, 154, 135, 154, 166, 59, fill=shape_colour,
                                                                              outline=global_background))  # Pentagon
                shapes_canvases[shape].bind("<ButtonPress-1>", lambda x: on_click("shape", "pentagon"))

            elif shape == "hexagon":
                shapes_shapes[shape] = (shapes_canvases[shape].create_polygon(128, 11, 42, 11, 0, 85, 43, 159, 127, 159, 170, 85, fill=shape_colour,
                                                                              outline=global_background))  # Hexagon
                shapes_canvases[shape].bind("<ButtonPress-1>", lambda x: on_click("shape", "hexagon"))

            elif shape == "trapezium":
                shapes_shapes[shape] = (shapes_canvases[shape].create_polygon(128, 51, 42, 51, 0, 134.3, 170, 134.3, fill=shape_colour,
                                                                              outline=global_background))  # Trapezium
                shapes_canvases[shape].bind("<ButtonPress-1>", lambda x: on_click("shape", "trapezium"))

            calledShapes.append(shape)

            count += 1

        get_names()

    def get_names():
        global calledShapes, calledNames
        global names_canvases, names_text
        calledNames = []
        count = 0
        padx = 125

        for i in calledShapes:
            count = count + 1
            name = random.choice(calledShapes)
            while name in calledNames:
                name = random.choice(calledShapes)

            calledNames.append(name)
            names_canvases[name] = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
            names_canvases[name].grid(column=count, row=1, padx=padx)
            names_text[name] = names_canvases[name].create_text(60, 37.5, text=name.title())
            names_canvases[name].itemconfig(names_text[name], font=("MyriadPro-Regular", 20), fill=text_colour)
            names_canvases[name].bind("<ButtonPress-1>", lambda event,name=name: on_click("name", name))

    def on_click(type, shape):
        print(type, shape)
        global clickedcurrentlyNames, names_boxes, names_canvases, shapes_shapes, shapes_canvases, shapes_boxes
        frameWinner.lower()
        if type == "name":
            if clickedcurrentlyNames == 0:
                clickedcurrentlyNames = shape
                print(shape)
                names_boxes[shape] = names_canvases[shape].create_rectangle(0, 0, 119, 74, fill="", outline=border_colour)
                names_boxes[shape] = names_canvases[shape].create_rectangle(55, 65, 65, 75, fill="#808098", outline=border_colour)

        elif type == "shape":
            global clickedcurrentlyShapes
            frameWinner.lower()
            if clickedcurrentlyNames == 0:
                return()

            if clickedcurrentlyShapes  == 0:
                clickedcurrentlyShapes = shape
                shapes_boxes[shape] = shapes_canvases[shape].create_rectangle(0, 0, 169, 169, fill="", outline=border_colour)
                check_pairs()

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
