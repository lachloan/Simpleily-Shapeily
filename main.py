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

canvasTitle = tkinter.Canvas(frameOne, width=1280, height=720)
canvasTitle.pack()



background_image = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\background.gif')
canvasTitle.create_image(0, 0, image=background_image, anchor="nw")

canvas_id = canvasTitle.create_text(10, 10, anchor="nw")
canvasTitle.itemconfig(canvas_id, text="Simpily Shapeily", width=1280)
canvasTitle.itemconfig(canvas_id, font=("verdana", 25))
xOffset = findXCenter(canvasTitle, canvas_id)
canvasTitle.move(canvas_id, xOffset, 75)

childSam = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\childSam.gif')
childLamb = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\childLamb.gif')
childDamn = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\childDamn.gif')
childGram = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\childGram.gif')

image_childSam = tkinter.Label(frameTwo, image=childSam).grid(column = 0, row = 0)
image_labelchildLamb = tkinter.Label(frameTwo, image=childLamb).grid(column = 1, row = 0)
image_labelchildDamn = tkinter.Label(frameTwo, image=childDamn).grid(column = 2, row = 0)
image_labelchildGram = tkinter.Label(frameTwo, image=childGram).grid(column = 3, row = 0)

frameOne.pack()
frameTwo.place(in_=frameOne)
window.mainloop()

