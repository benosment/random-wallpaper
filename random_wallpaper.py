#! /usr/bin/env python3
#
# Ben Osment
# Thu Jun 12 15:47:16 2014

"""Sets background wallpaper to a randomly chosen image"""

import os
import random
import subprocess


def select_wallpaper(dir='/home/ben/Pictures/Wallpapers'):
    """selects a random wallpaper"""
    return os.path.join(dir, random.choice(os.listdir(dir)))
    
def set_wallpaper(filename):
    """sets the wallpaper. only works in ubuntu (with unity)"""
    command = "gsettings set org.gnome.desktop.background picture-uri file://%s" % filename
    subprocess.check_output(command.split())

if __name__ == '__main__':
    selection = select_wallpaper()
    set_wallpaper(selection)
