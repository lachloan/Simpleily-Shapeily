elif shape == "pentagon":
	shape_canvas_pentagon = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,highlightthickness=0, relief="ridge")
	shapes_shapes.append(shape_canvas_pentagon.create_polygon(10, 85, 85, 10, 160, 85, 85, 160, fill=shape_colour,outline=global_background))  # pentagon
	shape_canvas_pentagon.grid(row=1, column=count, padx=shape_padx)
shape_canvas_pentagon.bind("<ButtonPress-1>", on_click_pentagon)


def on_click_pentagon_name(event):
	global name_canvas_pentagon, clickedcurrentlyNames


	if clickedcurrentlyNames == 0:
		clickedcurrentlyNames = "pentagon"
		name_pentagon_box = name_canvas_pentagon.create_rectangle(0,0,119,74, fill="", outline=border_colour)
		name_pentagon_box = name_canvas_pentagon.create_rectangle(55, 65, 65, 75, fill=border_colour,outline=border_colour)


def on_click_pentagon(event):
	global shape_canvas_pentagon, clickedcurrentlyShapes


	if clickedcurrentlyShapes == 0:
		clickedcurrentlyShapes = "pentagon"
		shape_canvas_pentagon.create_rectangle(0,0,169,169, fill="", outline=border_colour)
		check_shapes()


