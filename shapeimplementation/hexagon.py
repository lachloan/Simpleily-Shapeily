elif shape == "hexagon":
                shape_canvas_hexagon = tkinter.Canvas(frameShapes, width=170, height=170, bg=global_background, bd=0,
                                                      highlightthickness=0, relief="ridge")
                shapes_shapes.append(shape_canvas_hexagon.create_polygon(10, 85, 85, 10, 160, 85, 85, 160, fill=shape_colour,
                                                                outline=global_background))  # Hexagon
                shape_canvas_hexagon.grid(row=1, column=count, padx=shape_padx)
                shape_canvas_hexagon.bind("<ButtonPress-1>", on_click_hexagon)
                
# Hexagon Clicks
    def on_click_hexagon_name(event):
        global name_canvas_hexagon, clickedcurrentlyNames

        if clickedcurrentlyNames == 0:
            clickedcurrentlyNames = "hexagon"
            name_hexagon_box = name_canvas_hexagon.create_rectangle(0,0,119,74, fill="", outline=border_colour)
            name_hexagon_box = name_canvas_hexagon.create_rectangle(55, 65, 65, 75, fill=border_colour,
                                                                  outline=border_colour)
    def on_click_hexagon(event):
        global shape_canvas_hexagon, clickedcurrentlyShapes

        if clickedcurrentlyShapes == 0:
            clickedcurrentlyShapes = "hexagon"
            shape_canvas_hexagon.create_rectangle(0,0,169,169, fill="", outline=border_colour)
            check_shapes()

elif name == "hexagon":
                name_canvas_hexagon = tkinter.Canvas(frameNames, width=120, height=75, bg=global_background, bd=0,
                                                    highlightthickness=0, relief="ridge")
                name_canvas_hexagon.grid(column=count, row=1, padx=padx)
                name_hexagon = name_canvas_hexagon.create_text(60,37.5, text="Hexagon")
                name_canvas_hexagon.itemconfig(name_hexagon, font=("MyriadPro-Regular", 20), fill=text_colour)
                name_canvas_hexagon.bind("<ButtonPress-1>", on_click_hexagon_name)
