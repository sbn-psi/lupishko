#!/usr/bin/env python3

import os
import os.path as path
import sys
import csv
from re import sub
from re import search

# Get/set filename
# Set absolute path
filename = str(sys.argv[1])
abspath = path.abspath(filename)

# path to new file
new_filename = sub( r'.txt', '.csv', abspath)
new_abspath = path.abspath(new_filename)

# if new file already exists, remove it
if os.path.exists(new_abspath):
    os.remove(new_abspath)

MISSING_VALUES = [
    '-',           # column 1
    '-',           # column 2
    '-',           # column 3
    '-999.99',     # column 4
    '-',           # column 5
    '-999.99',     # column 6
    '-999.99',     # column 7
    '-999.99',     # column 8
    '-999.99',     # column 9
    '-999.99',     # column 10
    '-999.99',     # column 11
    '-999.99',     # column 12
    '-999.99',     # column 13
    '-',           # column 14
    '-',           # column 15
]

def formatName( name ):
    return name[0:4] + " " + name[4:len(name)].upper()

### ##### #### ###
### BEGIN MAIN ###
### ##### #### ###
def main( file ):
    # loop through lines in input file
    with open(abspath, newline="\n") as csv_file:
        spamreader = csv.reader(csv_file)

        for row_arr in spamreader:
            row = row_arr[0]

            newrow = [
                row[0:6].strip(),               # column 1
                row[7:20].strip(),              # column 2
                sub( r'--', '-0', sub( r' ', '-', row[21:31].strip() )),                      # column 3
                "0." + row[32:35].strip(),             # column 4
                row[36:41].strip(),             # column 5
                row[41:47].strip(),             # column 6
                row[48:53].strip(),             # column 7
                row[54:58].strip(),             # column 8
                row[59:64].strip(),             # column 9
                row[65:70].strip(),             # column 10
                row[71:76].strip(),             # column 11
                row[77:83].strip(),             # column 12
                row[84:90].strip(),             # column 13
                row[91:103].strip(),            # column 14
                row[105:len(row)].strip()       # column 15
            ]

            for idx, column in enumerate(newrow, start=0):
                if not column:
                    newrow[idx] = MISSING_VALUES[idx]

            # if name is not formatted properly, format it
            name = newrow[1]
            if search(r"\d{4}",name) != None:
                if search(r" ",name) == None:
                    newrow[1] = formatName(name)

            with open(new_abspath, 'a+') as new_csv_file:
                spamwriter = csv.writer(new_csv_file, delimiter=',')
                spamwriter.writerow(newrow)


# Execute main
main( file=abspath )