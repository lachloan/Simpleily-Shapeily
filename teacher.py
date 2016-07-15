from tkinter import ttk
import tkinter
import database

def run():
    global window

    window = tkinter.Tk()
    window.title("Simpiley Shapeily - Teacher Panel")
    window.geometry("720x720")
    window.resizable(0,0)
    ent = tkinter.Entry(window)

    frameTeacher = tkinter.Frame(window)


    children_dict = database.dbLoad()
    children_pictures = {}
    children_buttons = {}
    children_count = 0

    frameTeacher.pack()
    window.mainloop()


    listbox = tkinter.Listbox(frameTeacher)
    listbox.pack()

    for i in children_dict:
        listbox.insert("end", i)

    passwordguess = tkinter.Entry(frameTeacher, show="*").pack()