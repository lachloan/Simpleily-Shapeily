import tkinter

def run():

    window = tkinter.Tk()
    window.title("Simpiley Shapeily - Testing Panel")
    window.geometry("720x720")
    window.resizable(0,0)
    ent = tkinter.Entry(window)

    wincountNumber = tkinter.StringVar()

    frameWincount = tkinter.Frame(window, bg="white")
    wincountLabelText = tkinter.Label(frameWincount, text="Win Count:", background="white",
                                      font=("MyriadPro-Regular", 15)).pack()
    wincountLabelText = tkinter.Label(frameWincount, textvariable=wincountNumber,background="white").pack()
    wincountNumber.set("0")

    canvases = {}

    shapes = ['circle', 'square']

    for i in shapes:
        canvases[i] = tkinter.Canvas(window, height=100, width=100, background="white")

        name_square = canvases[i].create_text(60, 37.5, text=i.title())
        canvases[i].itemconfig(name_square, font=("MyriadPro-Regular", 20,), fill="black")

        canvases[i].pack()



    frameWincount.pack()
    window.mainloop()



run()