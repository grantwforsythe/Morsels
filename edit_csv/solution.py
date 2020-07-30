import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument('old_file')
parser.add_argument('new_file')
parser.add_argument('--in-delimiter=', dest='delim')
parser.add_argument('--in-quote=', dest='quote')  # automatically defaults to ''
args = parser.parse_args()

with open(args.old_file, 'r') as f:  # with blocks automatically close when Python is done with them
	arguments = {}  # empty dict
    if args.delim:
        arguments['delimiter'] = args.delim
    if args.quote:
    	arguments['quotechar'] = args.quote
    if not args.delim and not args.quote:  
        arguments['dialect'] = csv.Sniffer().sniff(f.read())  # searchs through the whole file
        f.seek(0)  # seeks back to the beginning of the file so we can read from it
    reader = csv.reader(f, **arguments)  

    with open(args.new_file, 'w') as new_f:
        writer = csv.writer(new_f)  # automatically uses ',' as the delimiter
        for row in reader:
            writer.writerow(row)