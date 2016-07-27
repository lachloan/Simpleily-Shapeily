from sys import argv

shape = input("Shape to create? ")

target = open(shape + '.py', 'w')

add_line = "ok"

line = []

line.append('elif shape == "' + shape + '":')
line.append('\tshape_canvas_' + shape + ' = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,highlightthickness=0, relief="ridge")')
line.append('\tshapes_shapes.append(shape_canvas_' + shape + '.create_polygon(10, 85, 85, 10, 160, 85, 85, 160, fill=shape_colour,outline=global_background))  # ' + shape + '')
line.append('\tshape_canvas_' + shape + '.grid(row=1, column=count, padx=shape_padx)')
line.append('shape_canvas_' + shape + '.bind("<ButtonPress-1>", on_click_' + shape + ')')
line.append('\n')

line.append('def on_click_' + shape + '_name(event):')
line.append('\tglobal name_canvas_' + shape + ', clickedcurrentlyNames')
line.append('\n')
line.append('\tif clickedcurrentlyNames == 0:')
line.append('\t\tclickedcurrentlyNames = "' + shape + '"')
line.append('\t\tname_' + shape + '_box = name_canvas_' + shape + '.create_rectangle(0,0,119,74, fill="", outline=border_colour)')
line.append('\t\tname_' + shape + '_box = name_canvas_' + shape + '.create_rectangle(55, 65, 65, 75, fill=border_colour,outline=border_colour)')
line.append('\n')
line.append('def on_click_' + shape + '(event):')
line.append('\tglobal shape_canvas_' + shape + ', clickedcurrentlyShapes')
line.append('\n')
line.append('\tif clickedcurrentlyShapes == 0:')
line.append('\t\tclickedcurrentlyShapes = "' + shape + '"')
line.append('\t\tshape_canvas_' + shape + '.create_rectangle(0,0,169,169, fill="", outline=border_colour)')
line.append('\t\tcheck_shapes()')
line.append('\n')
line.append('\n')
line.append('\n')
line.append('\t')






for i in line:
    target.write(i)
    target.write('\n')


target.close()