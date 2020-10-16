#!/usr/bin/env python

from gimpfu import *

def deep_fry(img, layer, red_noise, green_noise, blue_noise, sharpen_percent, posterize_levels) :
    gimp.progress_init("Deep frying " + layer.name + "...")
    pdb.gimp_image_undo_group_start(img)
    pdb.plug_in_rgb_noise(img, layer, True, False, red_noise, green_noise, blue_noise, 0)
    pdb.plug_in_sharpen(img,layer,sharpen_percent)
    pdb.gimp_drawable_posterize(layer,posterize_levels)
    pdb.gimp_image_undo_group_end(img)
    pdb.gimp_progress_end()

register(
    "deep_fry",
    "Deep fries image",
    "Deep fries image",
    "Kysonn Dela Cerna",
    "MIT",
    "2020",
    "<Image>/Filters/Meme/Deep fry",
    "RGB, RGB*",
    [
        (PF_SLIDER, "r", "Red Channel Noise", 0.05, (0,1,0.01)),
        (PF_SLIDER, "g", "Green Channel Noise", 0.05, (0,1,0.01)),
        (PF_SLIDER, "b", "Blue Channel Noise", 0.05, (0,1,0.01)),
        (PF_SLIDER, "s", "Sharpen Percentage", 75, (0,100,1)),
        (PF_SLIDER, "p", "Posterize Levels", 2, (2,255,1)),
    ],
    [],
    deep_fry)

main()