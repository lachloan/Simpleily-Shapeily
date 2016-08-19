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



def main_menu():
    global window, ent

    frameOne = tkinter.Frame(window)
    frameTwo = tkinter.Frame(window)
    frameButtons = tkinter.Frame(window)
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

    canvasTextsub = canvasMain.create_text(10, 180, anchor="nw")
    canvasMain.itemconfig(canvasTextsub, text='Press "Go!" to start', width=1280, fill="#4f4f4f")
    canvasMain.itemconfig(canvasTextsub, font=("MyriadPro-Regular", 19))
    xOffset = findXCenter(canvasMain, canvasTextsub)
    canvasMain.move(canvasTextsub, xOffset, 75)

    canvasTextatt = canvasMain.create_text(10, 600, anchor="nw")
    canvasMain.itemconfig(canvasTextatt, text="Built by Lockie, v0.01", width=1280, fill="#4f4f4f")
    canvasMain.itemconfig(canvasTextatt, font=("MyriadPro-Regular", 13))
    xOffset = findXCenter(canvasMain, canvasTextatt)
    canvasMain.move(canvasTextatt, xOffset, 75)

    button = ttk.Button(frameButtons, text="Go!", command=lambda: game.run("timed")).grid(row=1)

    file = "resources/leaderboard.db"
    leaderboard_dict = pickle.load(open(file, "rb"))
    leaderboard_list = list(sorted(leaderboard_dict, key=leaderboard_dict.__getitem__, reverse=True))
    print(leaderboard_list)
    leaderboard_entries = {}
    for i in leaderboard_list:
        leaderboard_entries[i] = (tkinter.Label(frameLeaderboard, text=i + " " + str(leaderboard_dict.get(i)), font=("MyriadPro-Regular", 13)))
        leaderboard_entries[i].grid()


    frameOne.pack()
    frameTwo.place(in_=frameOne, anchor="c", relx=.5, rely=.5)  # http://stackoverflow.com/questions/4241036/how-do-i-center-a-frame-within-a-frame-in-tkinter
    frameButtons.place(in_=frameOne, anchor="c", relx=.5, rely=.45)
    frameLeaderboard.place(in_=frameOne, anchor="c", relx=.5, rely=.7)
    window.mainloop()

main_menu()
