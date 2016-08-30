from tkinter import ttk
import tkinter, pickle
import game

def findXCenter(canvas, item):
    coords = canvas.bbox(item)
    xOffset = (1280 / 2) - ((coords[2] - coords[0]) / 2)
    return xOffset

window = tkinter.Tk()
window.title("Simpiley Shapeily")
window.geometry("1280x720")
window.resizable(0,0)
ent = tkinter.Entry(window)

def help_menu():
    global window, ent

    help_window = tkinter.Toplevel()
    help_window.title("Simpiley Shapeily")
    help_window.geometry("500x600")
    help_window.resizable(0,0)

    canvasHelp = tkinter.Canvas(help_window, width=500, height=600)
    canvasHelp.pack()


    background_image = tkinter.PhotoImage(
        file='resources\\background.gif')
    canvasHelp.create_image(0, 0, image=background_image, anchor="nw")

    help_title = canvasHelp.create_text(10, 0, anchor="nw")
    canvasHelp.itemconfig(help_title, text='Welcome to Simpiley Shapeily!', width=500, fill="#4f4f4f")
    canvasHelp.itemconfig(help_title, font=("MyriadPro-Regular", 24))
    canvasHelp.move(help_title, 35, 55)


    help_text = canvasHelp.create_text(10, 0, anchor="nw")
    canvasHelp.itemconfig(help_text,
                          text="Simpiley Shapeily is a shape matching game! It's easy! \nClick the name you want to connect, and then click the \nshape you want to connect it with! You cannot unselect\n your selections! The shapes are as follows:", width=500, fill="#4f4f4f")
    canvasHelp.itemconfig(help_text, font=("MyriadPro-Regular", 12))
    canvasHelp.move(help_text, 35, 105)

    help_title2 = canvasHelp.create_text(10, 0, anchor="nw")
    canvasHelp.itemconfig(help_title2, text='The Leaderboard', width=500, fill="#4f4f4f")
    canvasHelp.itemconfig(help_title2, font=("MyriadPro-Regular", 17))
    canvasHelp.move(help_title2, 250, 370)

    help_text2 = canvasHelp.create_text(10, 0, anchor="nw")
    canvasHelp.itemconfig(help_text2, text="The Leaderboard is where you can see who is the best at the game! If you score in the top 5, your name will appear in the leaderboard!",
                          width=200, fill="#4f4f4f")
    canvasHelp.itemconfig(help_text2, font=("MyriadPro-Regular", 11))
    canvasHelp.move(help_text2, 250, 400)

    shapes_shapes = {}
    shapes_shapes["square"] = (canvasHelp.create_rectangle(45, 200, 85, 240, fill="#4f4f4f",
                                                                    outline="#4f4f4f"))  # Square

    shapes_shapes["triangle"] = (canvasHelp.create_polygon(45, 300, 65, 260, 85, 300, fill="#4f4f4f",
                                                           outline="#4f4f4f"))  # Square

    shapes_shapes["circle"] = (canvasHelp.create_oval(45, 320, 85, 360, fill="#4f4f4f",
                                                           outline="#4f4f4f"))  # Square

    shapes_shapes["diamond"] = (canvasHelp.create_polygon(45, 400, 65, 380, 85, 400, 65, 420, fill="#4f4f4f",
                                                           outline="#4f4f4f"))  # Square

    shapes_shapes["trapezium"] = (canvasHelp.create_polygon(45, 460, 55, 440, 75, 440, 85, 460, fill="#4f4f4f",
                                                           outline="#4f4f4f"))  # Square

    shapes_shapes["pentagon"] = (canvasHelp.create_polygon(65, 480, 46, 494, 53, 516, 77, 516, 84, 494, fill="#4f4f4f",
                                                           outline="#4f4f4f"))  # Square

    shapes_shapes["hexagon"] = (canvasHelp.create_polygon(75, 533, 55, 533, 45, 550, 55, 567, 75, 567, 85, 550, fill="#4f4f4f",
                                                           outline="#4f4f4f"))  # Square

    shapes_name = {}
    shapes_list = ['square', 'triangle', 'circle', 'diamond', 'trapezium', 'pentagon', 'hexagon']
    count = 1

    for i in shapes_list:
        i = i.title()
        print(i)
        shapes_name[i] = canvasHelp.create_text(10, 0, anchor="nw")
        canvasHelp.itemconfig(shapes_name[i],
                              text=i,
                              width=500, fill="#4f4f4f")
        canvasHelp.itemconfig(shapes_name[i], font=("MyriadPro-Regular", 12))
        if i == "Pentagon":
            canvasHelp.move(shapes_name[i], 95, 150 + count * 57)

        elif i == "Hexagon":
            canvasHelp.move(shapes_name[i], 95, 150 + count * 56)
        else:
            canvasHelp.move(shapes_name[i], 95, 150+count*58)
        count = count + 1



    




    help_window.mainloop()


def main_menu():
    global window, ent

    frameOne = tkinter.Frame(window)
    frameTwo = tkinter.Frame(window)
    frameButtonsGo = tkinter.Frame(window)
    frameButtonsHelp = tkinter.Frame(window)
    frameLeaderboard = tkinter.Frame(window)

    canvasMain = tkinter.Canvas(frameOne, width=1280, height=720)
    canvasMain.pack()

    background_image = tkinter.PhotoImage(
        file='resources\\background.gif')
    canvasMain.create_image(0, 0, image=background_image, anchor="nw")

    canvasText = canvasMain.create_text(10, 10, anchor="nw")
    canvasMain.itemconfig(canvasText, text="Simpiley Shapeily", width=1280, fill="#4f4f4f")
    canvasMain.itemconfig(canvasText, font=("MyriadPro-Regular", 40))
    xOffset = findXCenter(canvasMain, canvasText)
    canvasMain.move(canvasText, xOffset, 75)

    canvasTextsub = canvasMain.create_text(10, 140, anchor="nw")
    canvasMain.itemconfig(canvasTextsub, text='Press "Go!" to start', width=1280, fill="#4f4f4f")
    canvasMain.itemconfig(canvasTextsub, font=("MyriadPro-Regular", 19))
    xOffset = findXCenter(canvasMain, canvasTextsub)
    canvasMain.move(canvasTextsub, xOffset, 75)

    canvasTexthelp = canvasMain.create_text(10, 500, anchor="nw")
    canvasMain.itemconfig(canvasTexthelp, text='Need any help? Press "Help?"', width=1280, fill="#4f4f4f")
    canvasMain.itemconfig(canvasTexthelp, font=("MyriadPro-Regular", 14))
    xOffset = findXCenter(canvasMain, canvasTexthelp)
    canvasMain.move(canvasTexthelp, xOffset, 75)

    canvasTextatt = canvasMain.create_text(10, 600, anchor="nw")
    canvasMain.itemconfig(canvasTextatt, text="Built by Lachlan, v1.2", width=1280, fill="#4f4f4f")
    canvasMain.itemconfig(canvasTextatt, font=("MyriadPro-Regular", 13))
    xOffset = findXCenter(canvasMain, canvasTextatt)
    canvasMain.move(canvasTextatt, xOffset, 75)

    canvasTextleader = canvasMain.create_text(4, 270, anchor="nw")
    canvasMain.itemconfig(canvasTextleader, text="The Leaderboard", width=1280, fill="#4f4f4f")
    canvasMain.itemconfig(canvasTextleader, font=("MyriadPro-Regular", 16))
    xOffset = findXCenter(canvasMain, canvasTextleader)
    canvasMain.move(canvasTextleader, xOffset, 75)

    buttonGo = ttk.Button(frameButtonsGo, text="Go!", command=lambda: game.run("timed")).grid(row=1)
    buttonHelp = ttk.Button(frameButtonsHelp, text="Help?", command=lambda: help_menu()).grid(row=1)

    file = "resources/leaderboard.db"
    try:
        leaderboard_dict = pickle.load(open(file, "rb"))
    except:
        open(file, "a").close()
        leaderboard_dict = {"Empty" : 0}
        pickle.dump(leaderboard_dict, open(file, "wb"))

    leaderboard_list = list(sorted(leaderboard_dict, key=leaderboard_dict.__getitem__, reverse=True))
    print(leaderboard_list)
    leaderboard_entries = {}
    leaderboard_count = 0
    for i in leaderboard_list:
        leaderboard_entries[i] = (tkinter.Label(frameLeaderboard, text=i + " " + str(leaderboard_dict.get(i)), font=("MyriadPro-Regular", 13)))
        leaderboard_entries[i].grid()
        leaderboard_count = leaderboard_count + 1
        if leaderboard_count == 5:
            break


    frameOne.pack()
    frameTwo.place(in_=frameOne, anchor="c", relx=.5, rely=.5)  # http://stackoverflow.com/questions/4241036/how-do-i-center-a-frame-within-a-frame-in-tkinter
    frameButtonsGo.place(in_=frameOne, anchor="c", relx=.5, rely=.37)
    frameLeaderboard.place(in_=frameOne, anchor="c", relx=.5, rely=.63)
    frameButtonsHelp.place(in_=frameOne, anchor="c", relx=.5, rely=.86)
    window.mainloop()

main_menu()
