#!/usr/bin/env python

from gimpfu import *
import math, os


def do_stuff(img, drw, mindeg, maxdeg, inc, toggle, times2, fname, path) :
    i = mindeg
    last_i = 0
    nn = 0

    pdb.gimp_undo_push_group_start(img)

    if inc > 0 or maxdeg < mindeg:
        while i <= maxdeg :
            copy = pdb.gimp_layer_copy(drw, True)
            pdb.gimp_image_insert_layer(img, copy, None, 1)
            pdb.gimp_item_transform_rotate(copy, (i) * (math.pi / 180) ,True,300,300)
            pdb.gimp_layer_resize_to_image_size(copy)
            last_i = i
            i += inc
            if toggle == 1:
                filename = fname + "_" + str(nn) + ".png"
            if toggle == 0:
                #if times2 == 0:
                    filename = fname + "_" + str(i-inc) + ".png"
                #if times2 == 1:
                    #filename = fname + "_" + str((2*i)-(2*inc)) + ".png" #TODO násobení čísla dvouma
            fullpath = os.path.join(path, filename)
            pdb.gimp_file_save(img, copy, fullpath, filename)
            pdb.gimp_image_remove_layer(img, copy)
            nn += 1
    else:
        gimp.message("Wrong input values!")
    

    pdb.gimp_undo_push_group_end(img)


register(
    "python_fu_rotate_and_save",
    "Rotate and save",
    "Longer description of doing stuff",
    "Marek Nesvadba",
    "Marek Nesvabda",
    "2018",
    "Rotate and save...",
    "*",
    [
        (PF_IMAGE, "img", "Input image", None),
        (PF_DRAWABLE, "drw", "Input layer", None),
        (PF_INT32, "mindeg", "Min angle:", 0),
        (PF_INT32, "maxdeg", "Max angle:", 0),
        (PF_INT, "inc", "Increment:", 1),
		(PF_TOGGLE, "toggle", "Number after the filename. 1 = order,0 = angle:", 1),
		(PF_TOGGLE, "times2", "Previous number times 2 (works only for angle):", 0),
		(PF_STRING, "fname", "Filename:", "test"),
        (PF_DIRNAME, "path", "Output directory:", os.getcwd()),
    ],
    [],
    do_stuff,
    menu="<Image>/Filters"
    )

main()