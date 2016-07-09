from tkinter import ttk
import tkinter

def findXCenter(canvas, item):
    coords = canvas.bbox(item)
    xOffset = (1280 / 2) - ((coords[2] - coords[0]) / 2)
    return xOffset

window = tkinter.Tk()
window.title("Simplily Shapeily")
window.geometry("1280x720")
window.resizable(0,0)
ent = tkinter.Entry(window)

frameOne = tkinter.Frame(window)
frameTwo = tkinter.Frame(window)
frameButtons = tkinter.Frame(window)

canvasMain = tkinter.Canvas(frameOne, width=1280, height=720)
canvasMain.pack()



background_image = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\background.gif')
canvasMain.create_image(0, 0, image=background_image, anchor="nw")

canvasText = canvasMain.create_text(10, 10, anchor="nw")
canvasMain.itemconfig(canvasText, text="Simpiley Shapeily", width=1280, fill ="#4f4f4f")
canvasMain.itemconfig(canvasText, font=("MyriadPro-Regular", 40))
xOffset = findXCenter(canvasMain, canvasText)
canvasMain.move(canvasText, xOffset, 75)

canvasTextsub = canvasMain.create_text(10, 180, anchor="nw")
canvasMain.itemconfig(canvasTextsub, text="Click on the picture of you to start!", width=1280, fill ="#4f4f4f")
canvasMain.itemconfig(canvasTextsub, font=("MyriadPro-Regular", 19))
xOffset = findXCenter(canvasMain, canvasTextsub)
canvasMain.move(canvasTextsub, xOffset, 75)

canvasTextatt = canvasMain.create_text(10, 600, anchor="nw")
canvasMain.itemconfig(canvasTextatt, text="Built by Lachlan McEwen, v0.01", width=1280, fill ="#4f4f4f")
canvasMain.itemconfig(canvasTextatt, font=("MyriadPro-Regular", 13))
xOffset = findXCenter(canvasMain, canvasTextatt)
canvasMain.move(canvasTextatt, xOffset, 75)

button = ttk.Button(frameButtons, text="Teacher Login").grid(row = 1)



childSam = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\childSam.gif')
childLamb = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\childLamb.gif')
childDamn = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\childDamn.gif')
childGram = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\childGram.gif')

image_childSam = ttk.Button(frameTwo, image=childSam, command=lambda: print("sam")).grid(column = 0, row = 0)
image_labelchildLamb = ttk.Button(frameTwo, image=childLamb, command=lambda: print("Lamb")).grid(column = 1, row = 0)
image_labelchildDamn = ttk.Button(frameTwo, image=childDamn, command=lambda: print("Damn")).grid(column = 2, row = 0)
image_labelchildGram = ttk.Button(frameTwo, image=childGram, command=lambda: print("Gram")).grid(column = 3, row = 0)


frameOne.pack()
frameTwo.place(in_=frameOne, anchor="c", relx=.5, rely=.5)
frameButtons.place(in_=frameOne, anchor="c", relx=.5, rely=.91)# http://stackoverflow.com/questions/4241036/how-do-i-center-a-frame-within-a-frame-in-tkinter
window.mainloop()

