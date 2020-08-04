import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('old_file')
parser.add_argument('new_file')
parser.add_argument('--in-deilimeter', dest='deilimeter')
parser.add_argument('--in-quote', dest='quote')

