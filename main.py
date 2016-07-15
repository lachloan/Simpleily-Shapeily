from tkinter import ttk
import tkinter

import database
import teacher
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

    canvasMain = tkinter.Canvas(frameOne, width=1280, height=720)
    canvasMain.pack()

    background_image = tkinter.PhotoImage(
        file='J:\\School\\Year 11\\Software Design and Development\\Simpily-Shapeily\\resources\\background.gif')
    canvasMain.create_image(0, 0, image=background_image, anchor="nw")

    canvasText = canvasMain.create_text(10, 10, anchor="nw")
    canvasMain.itemconfig(canvasText, text="Simpiley Shapeily", width=1280, fill="#4f4f4f")
    canvasMain.itemconfig(canvasText, font=("MyriadPro-Regular", 40))
    xOffset = findXCenter(canvasMain, canvasText)
    canvasMain.move(canvasText, xOffset, 75)

    canvasTextsub = canvasMain.create_text(10, 180, anchor="nw")
    canvasMain.itemconfig(canvasTextsub, text="Click on the picture of you to start!", width=1280, fill="#4f4f4f")
    canvasMain.itemconfig(canvasTextsub, font=("MyriadPro-Regular", 19))
    xOffset = findXCenter(canvasMain, canvasTextsub)
    canvasMain.move(canvasTextsub, xOffset, 75)

    canvasTextatt = canvasMain.create_text(10, 600, anchor="nw")
    canvasMain.itemconfig(canvasTextatt, text="Built by Lockie, v0.01", width=1280, fill="#4f4f4f")
    canvasMain.itemconfig(canvasTextatt, font=("MyriadPro-Regular", 13))
    xOffset = findXCenter(canvasMain, canvasTextatt)
    canvasMain.move(canvasTextatt, xOffset, 75)

    button = ttk.Button(frameButtons, text="Teacher Login", command=lambda:teacher.run()).grid(row=1)
    button = ttk.Button(frameButtons, text="TestGamePanel", command=lambda:game.run()).grid(row=2)

    children_dict = database.dbLoad()
    children_pictures = {}
    children_buttons = {}
    children_count = 0

    for i in children_dict:
        print(i)
        children_pictures[i] = tkinter.PhotoImage(
            file='J:\\School\\Year 11\\Software Design and Development\\Simpily-Shapeily\\resources\\child' + i + '.gif')
        children_buttons[i] = ttk.Button(frameTwo, image=children_pictures[i], command=lambda: print(i)).grid(
            column=children_count, row=0)
        children_count = children_count + 1

    frameOne.pack()
    frameTwo.place(in_=frameOne, anchor="c", relx=.5, rely=.5)  # http://stackoverflow.com/questions/4241036/how-do-i-center-a-frame-within-a-frame-in-tkinter
    frameButtons.place(in_=frameOne, anchor="c", relx=.5, rely=.91)
    window.mainloop()

main_menu()
