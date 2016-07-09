from tkinter import ttk
import tkinter


colourBackground = "#dedede"
window = tkinter.Tk()
window.title("Simplily Shapeily")
window.geometry("1280x720")
window.configure(background=colourBackground)
ent = tkinter.Entry(window)

background_image = tkinter.PhotoImage(file = 'D:\\School\\Year 11\\Software Design and Development\\SimpleilyShapeily\\Simpleily-Shapeily\\resources\\background.gif')
background_label = tkinter.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


frameOne = tkinter.Frame(window, bg = colourBackground, pady=50)

titleHero = ttk.Label(frameOne, background="white", text="Simplily Shapeily", font=("Verdana", 25))\
    .grid(column = 1)
titleSub = ttk.Label(frameOne, background="white", text="A fun, simple shape matching game!", font=("Verdana", 15))\
    .grid(column = 1, row = 2)


window.wm_attributes("-transparentcolor", "white")

#Sets up the mainloop and frames. Buttons are within frameone and the screen is frametwo.
frameOne.pack()
window.mainloop()

