#! /usr/bin/env python3
#
# Ben Osment
# Thu Jun 12 15:47:16 2014

"""Sets background wallpaper to a randomly chosen image"""

import os
import random
import subprocess

def set_env_variables():
    """CRON uses a very restricted set of env variables so we must set the rest"""
    os.environ['DISPLAY'] = ':0'
    os.environ['GSETTINGS_BACKEND'] = 'dconf'
    pid = subprocess.getoutput('pgrep gnome-session')
    command = "grep -z DBUS_SESSION_BUS_ADDRESS /proc/%s/environ" % pid
    output = subprocess.getoutput(command)
    os.environ['DBUS_SESSION_BUS_ADDRESS'] = output[output.find('=')+1:].strip('\0')
    
def select_wallpaper(dir='/home/ben/Pictures/Wallpapers'):
    """selects a random wallpaper"""
    return os.path.join(dir, random.choice(os.listdir(dir)))
    
def set_wallpaper(filename):
    """sets the wallpaper. only works in ubuntu (with unity)"""
    command = "gsettings set org.gnome.desktop.background picture-uri file://%s" % filename
    subprocess.check_output(command.split())

if __name__ == '__main__':
    set_env_variables()
    set_wallpaper(select_wallpaper())
