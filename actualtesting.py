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



    frameWincount.pack()
    window.mainloop()



run()