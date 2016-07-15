from tkinter import ttk
import tkinter
import database

window = tkinter.Tk()
window.title("Simpiley Shapeily")
window.geometry("1280x720")
window.resizable(0,0)
ent = tkinter.Entry(window)

frameOne = tkinter.Frame(window)


children_dict = database.dbLoad()
children_pictures = {}
children_buttons = {}
children_count = 0

for i in children_dict:
    print(i)
    children_pictures[i] = tkinter.PhotoImage(
        file='J:\\School\\Year 11\\Software Design and Development\\Simpily-Shapeily\\resources\\child' + i + '.gif')
    children_buttons[i] = ttk.Button(frameOne, image=children_pictures[i], command=lambda: print(i)).grid(column=children_count, row=0)
    children_count = children_count + 1

frameOne.pack()
window.mainloop()