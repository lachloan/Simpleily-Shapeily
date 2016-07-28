elif shape == "trapezium":
                shape_canvas_trapezium = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_trapezium.create_polygon(128,11,42,11,0,85,43,159,127,159,170,85, fill=shape_colour,
                                                                outline=global_background))  # Trapezium
                shape_canvas_trapezium.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_trapezium.bind("<ButtonPress-1>", on_click_trapezium)
                
# Trapezium Clicks
    def on_click_trapezium_name(event):
        global name_canvas_trapezium, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "trapezium"
            name_trapezium_box = name_canvas_trapezium.create_rectangle(0,0,119,74, fill="", outline=border_colour)
            name_trapezium_box = name_canvas_trapezium.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                  outline=border_colour)
    def on_click_trapezium(event):
        global shape_canvas_trapezium, clickedcurrentlyShapes

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "trapezium"
            shape_canvas_trapezium.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            check_shapes()

elif name == "trapezium":
                name_canvas_trapezium = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_trapezium.grid(column=count, row=1, padx=padx)
                name_trapezium = name_canvas_trapezium.create_text(60,37.5, text="Trapezium")
                name_canvas_trapezium.itemconfig(name_trapezium, font=("MyriadPro-Regular", 20), fill=text_colour)
                name_canvas_trapezium.bind("<ButtonPress-1>", on_click_trapezium_name)
