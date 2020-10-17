#!/usr/bin/env python

from gimpfu import *
import math

def fry_oil(img, layer) :
    gimp.progress_init("Aberrating chromas on " + layer.name + "...")
    pdb.gimp_image_undo_group_start(img)
    pos = pdb.gimp_image_get_layer_position(img, layer)
    magenta = pdb.gimp_layer_copy(layer, True)
    pdb.gimp_layer_set_name(magenta, layer.name + " Magenta")
    pdb.gimp_layer_set_mode(magenta, 34)
    cyan = pdb.gimp_layer_copy(layer, True)
    pdb.gimp_layer_set_name(cyan, layer.name + " Cyan")
    pdb.gimp_layer_set_mode(cyan, 34)
    img.add_layer(cyan, pos)
    img.add_layer(magenta, pos)
    pdb.plug_in_colors_channel_mixer(img, magenta, False, 1, 0, 0, 0, 0, 0, 0, 0, 1)
    pdb.plug_in_colors_channel_mixer(img, cyan, False, 0, 0, 0, 0, 1, 0, 0, 0, 1)
    pdb.gimp_layer_set_offsets(magenta, math.floor(0.015*layer.width), math.floor(0.015*layer.height))
    pdb.gimp_layer_set_offsets(cyan, math.floor(0.01*layer.width), math.floor(0.01*layer.height))
    pdb.gimp_image_undo_group_end(img)
    pdb.gimp_progress_end()

register(
    "fry_oil",
    "Makes the oil",
    "Creates deep fried oil effect",
    "Kysonn Dela Cerna",
    "MIT",
    "2020",
    "<Image>/Filters/Meme/Fry Oil",
    "RGB, RGB*",
    [],
    [],
    fry_oil)

main()