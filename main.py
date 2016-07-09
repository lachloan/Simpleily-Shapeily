from tkinter import ttk
import tkinter

def findXCenter(canvas, item):
    coords = canvas.bbox(item)
    xOffset = (1280 / 2) - ((coords[2] - coords[0]) / 2)
    return xOffset

window = tkinter.Tk()
window.title("Simplily Shapeily")
window.geometry("1280x720")
ent = tkinter.Entry(window)

canvas = tkinter.Canvas(window, width=1280, height=720)
canvas.pack()

background_image = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\background.gif')
canvas.create_image(0, 0, image=background_image, anchor="nw")

canvas_id = canvas.create_text(10, 10, anchor="nw")
canvas.itemconfig(canvas_id, text="Simpily Shapeily", width=1280)
canvas.itemconfig(canvas_id, font=("verdana", 25))
xOffset = findXCenter(canvas, canvas_id)
canvas.move(canvas_id, xOffset, 0)

#Sets up the mainloop and frames. Buttons are within frameone and the screen is frametwo.
window.mainloop()

