#! /usr/bin/env python3
"""
Problem Statement

This exercise includes 1 bonuses and 5 hints (hover over the hint links before clicking on them).

I'd like you to create a program, ini2csv.py, which accepts an INI-like file and converts it to a CSV-like file.

The input files will look like this (this is an EditorConfig file):

[*.py]
indent_style = space
indent_size = 4

[*.js]
indent_style = space
indent_size = 2

Given that input file, .editorconfig, executing our program like this:

$ python ini2csv.py .editorconfig editorconfig.csv

Will produce an output file, editorconfig.csv, like this:

*.py,indent_style,space
*.py,indent_size,4
*.js,indent_style,space
*.js,indent_size,2

Note that the order of lines in this CSV file should match the order of sections and properties in the given INI file.

Bonus

There's just one bonus this week. For the bonus, I'd like you to accept a --collapsed argument that, when present, will collapse the rows to one row per section.

So this:

$ python ini2csv.py --collapsed .editorconfig editorconfig.csv

Will result in a editorconfig.csv file that contains this:

header,indent_style,indent_size
*.py,space,4
*.js,space,2
"""
import csv
import sys
import os
import configparser

filename = sys.argv[1]
config_csv = sys.argv[2]

config = configparser.ConfigParser()
config.read(filename)

def main():
    with open(config_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        for section in list(config.sections()):
            for key, value in zip(list(config[section].keys()), 
                                list(config[section].values())
                                ):
                writer.writerow((section, key, value))

if __name__ == '__main__':
    main()