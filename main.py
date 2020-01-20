#! /usr/bin/python env

from sys import argv, exit
from configparser import ConfigParser as parser
from os import chdir, listdir, path
arguments = argv


def checkParametrs():

    if len(argv) > 2 or len(argv) == 1:
        print('Error arguments')
        exit()

    if argv[1] == '-ls':
        print('short <')
    else:
        print('Neznami agument')

def setConfig():
    config = parser()
    config.read('init.ini')
    if 'PATH' in config:
        return config['PATH']['VideosDir']

def lsVideos(path):
    chdir(path)
    videos = listdir('.')
    for i in videos:
        return i

def getSize(files):
    s = path.getsize(files)
    return s


#lsVideos(setConfig())
s = getSize(lsVideos(setConfig()))
print(s)
