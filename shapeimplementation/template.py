elif shape == "diamond":
                shape_canvas_diamond = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_diamond.create_polygon(10, 85, 85, 10, 160, 85, 85, 160, fill=shape_colour,
                                                                outline=global_background))  # Diamond
                shape_canvas_diamond.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_diamond.bind("<ButtonPress-1>", on_click_diamond)
                
# Diamond Clicks
    def on_click_diamond_name(event):
        global name_canvas_diamond, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "diamond"
            name_diamond_box = name_canvas_diamond.create_rectangle(0,0,119,74, fill="", outline=border_colour)
            name_diamond_box = name_canvas_diamond.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                  outline=border_colour)
    def on_click_diamond(event):
        global shape_canvas_diamond, clickedcurrentlyShapes

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "diamond"
            shape_canvas_diamond.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            check_shapes()

elif name == "diamond":
                name_canvas_diamond = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_diamond.grid(column=count, row=1, padx=padx)
                name_diamond = name_canvas_diamond.create_text(60,37.5, text="Diamond")
                name_canvas_diamond.itemconfig(name_diamond, font=("MyriadPro-Regular", 20), fill=text_colour)
                name_canvas_diamond.bind("<ButtonPress-1>", on_click_diamond_name)
