from tkinter import ttk
import tkinter
import database

def run():
    global window

    window = tkinter.Tk()
    window.title("Simplily Shapeily")
    window.geometry("1280x720")
    window.resizable(0,0)
    ent = tkinter.Entry(window)

    frameTeacher = tkinter.Frame(window)


    children_dict = database.dbLoad()
    children_pictures = {}
    children_buttons = {}
    children_count = 0

    listbox = tkinter.Listbox(frameTeacher)
    listbox.pack()

    for i in children_dict:
        listbox.insert("end", i)

    frameTeacher.pack()
    window.mainloop()