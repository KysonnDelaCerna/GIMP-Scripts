#!/usr/bin/env python

from gimpfu import *

def meme(img, layer, text, font, size, border) :
    gimp.progress_init("Making meme " + layer.name + "...")
    pdb.gimp_image_undo_group_start(img)
    text_layer = pdb.gimp_text_fontname(img, None, 0, 0, text, border, True, float(size), 0, font.title())
    pdb.gimp_text_layer_set_color(text_layer, (0,0,0))
    pdb.gimp_text_layer_resize(text_layer, img.width-border, img.height)
    pdb.plug_in_autocrop_layer(img, text_layer)
    pdb.gimp_image_resize(img, img.width, img.height+text_layer.height+2*border, 0, 0)
    for l in img.layers:
        if l!=text_layer:
            pdb.gimp_layer_set_offsets(l, l.offsets[0], l.offsets[1]+text_layer.height+2*border)
    background = pdb.gimp_layer_new(img, img.width, img.height, 0, "Background", 100, 0)
    pdb.gimp_image_insert_layer(img, background, None, len(img.layers))
    pdb.gimp_drawable_edit_bucket_fill(background, 2, 0, 0)
    pdb.gimp_image_undo_group_end(img)
    pdb.gimp_progress_end()

register(
    "meme",
    "Make meme",
    "Make meme",
    "Kysonn Dela Cerna",
    "MIT",
    "2020",
    "<Image>/Filters/Meme/Make Meme",
    "RGB, RGB*",
    [
        (PF_STRING, "t", "Text", "Big meme"),
        (PF_FONT, "f", "Font", "Comic Sans MS"),
        (PF_INT32, "s", "Size", 12),
        (PF_INT32, "b", "Text Border", 10),
    ],
    [],
    meme)

main()