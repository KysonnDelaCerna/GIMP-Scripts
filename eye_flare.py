#!/usr/bin/env python

from gimpfu import *
import subprocess
import os
import sys

def eye_flare(img, layer, radius, hue, face, eyes, eyeglasses) :
    gimp.progress_init("Eye flaring " + layer.name + "...")
    pdb.gimp_image_undo_group_start(img)
    try:
        result = subprocess.Popen([os.environ["PYPATH"], os.path.dirname(os.path.abspath(__file__))+"\\detect_eyes.py", img.filename, str(int(face)), str(int(eyes)), str(int(eyeglasses))],stdout=subprocess.PIPE).communicate()[0]
        eyes = result.split(";")
        for eye in range(len(eyes)-1):
            x, y = eyes[eye].split(" ")
            pdb.plug_in_gflare(img, layer, "GFlare_102", x, y, radius, 0, hue, 60, 1, False, 3, 0.20)
    except:
        pdb.gimp_message("An error occured")
    pdb.gimp_image_undo_group_end(img)
    pdb.gimp_progress_end()

register(
    "eye_flare",
    "Makes eye flares",
    "Auto detects eyes and gives them flares",
    "Kysonn Dela Cerna",
    "MIT",
    "2020",
    "<Image>/Filters/Meme/Eye flare",
    "RGB, RGB*",
    [
        (PF_SLIDER, "r", "Radius", 100, (0,600,1)),
        (PF_SLIDER, "h", "Hue Rotation", 105, (-180,180,1)),
        (PF_SLIDER, "f", "Face Sensitivity", 5, (1,100,1)),
        (PF_SLIDER, "e", "Eyes Sensitivity", 5, (1,100,1)),
        (PF_SLIDER, "g", "Glasses Sensitivity", 5, (1,100,1)),
    ],
    [],
    eye_flare)

main()