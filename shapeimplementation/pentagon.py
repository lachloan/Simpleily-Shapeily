elif shape == "pentagon":
                shape_canvas_pentagon = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_pentagon.create_polygon(10, 85, 85, 10, 160, 85, 85, 160, fill=shape_colour,
                                                                outline=global_background))  # Pentagon
                shape_canvas_pentagon.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_pentagon.bind("<ButtonPress-1>", on_click_pentagon)
                
# Pentagon Clicks
    def on_click_pentagon_name(event):
        global name_canvas_pentagon, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "pentagon"
            name_pentagon_box = name_canvas_pentagon.create_rectangle(0,0,119,74, fill="", outline=border_colour)
            name_pentagon_box = name_canvas_pentagon.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                  outline=border_colour)
    def on_click_pentagon(event):
        global shape_canvas_pentagon, clickedcurrentlyShapes

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "pentagon"
            shape_canvas_pentagon.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            check_shapes()

elif name == "pentagon":
                name_canvas_pentagon = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_pentagon.grid(column=count, row=1, padx=padx)
                name_pentagon = name_canvas_pentagon.create_text(60,37.5, text="Pentagon")
                name_canvas_pentagon.itemconfig(name_pentagon, font=("MyriadPro-Regular", 20), fill=text_colour)
                name_canvas_pentagon.bind("<ButtonPress-1>", on_click_pentagon_name)
