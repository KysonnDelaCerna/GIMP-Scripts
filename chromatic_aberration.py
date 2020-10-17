#!/usr/bin/env python

from gimpfu import *
import math

def deep_fry(img, layer, mx, my, cx, cy) :
    gimp.progress_init("Aberrating chromas on " + layer.name + "...")
    pdb.gimp_image_undo_group_start(img)
    pos = pdb.gimp_image_get_layer_position(img, layer)
    magenta = pdb.gimp_layer_copy(layer, True)
    pdb.gimp_layer_set_name(magenta, layer.name + " Magenta")
    pdb.gimp_layer_set_mode(magenta, 36)
    cyan = pdb.gimp_layer_copy(layer, True)
    pdb.gimp_layer_set_name(cyan, layer.name + " Cyan")
    pdb.gimp_layer_set_mode(cyan, 36)
    img.add_layer(cyan, pos)
    img.add_layer(magenta, pos)
    pdb.plug_in_colors_channel_mixer(img, magenta, False, 1, 0, 0, 0, 0, 0, 0, 0, 1)
    pdb.plug_in_colors_channel_mixer(img, cyan, False, 0, 0, 0, 0, 1, 0, 0, 0, 1)
    pdb.gimp_layer_set_offsets(magenta, math.floor(mx*layer.width), math.floor(my*layer.height))
    pdb.gimp_layer_set_offsets(cyan, math.floor(cx*layer.width), math.floor(cy*layer.height))
    pdb.gimp_image_undo_group_end(img)
    pdb.gimp_progress_end()

register(
    "chromatic_aberration",
    "Vaporwave aesthetic",
    "Makes cyan and magenta splits of the image",
    "Kysonn Dela Cerna",
    "MIT",
    "2020",
    "<Image>/Filters/Vaporwave/Chromatic Aberration",
    "RGB, RGB*",
    [
        (PF_SLIDER, "mx", "MX Offset", -0.01, (-1, 1, 0.01)),
        (PF_SLIDER, "my", "MY Offset", -0.02, (-1, 1, 0.01)),
        (PF_SLIDER, "cx", "CX Offset", 0.02, (-1, 1, 0.01)),
        (PF_SLIDER, "cy", "CY Offset", 0.01, (-1, 1, 0.01)),
    ],
    [],
    deep_fry)

main()