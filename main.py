#! /usr/bin/python env

from sys import argv, exit

arguments = argv

if len(argv) > 2 or len(argv) == 1:
    print('Error arguments')
    exit()

if argv[1] == '-ls':
    print('short <')
else:
    print('Neznami agument')