#!/usr/bin/env python3

import os
import os.path as path
import sys
import csv
from re import sub

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
    '-',            # column 1
    '-',            # column 2
    '-',            # column 3
    '-999.999',     # column 4
    '-',            # column 5
    '-999.999',     # column 6
    '-999.999',     # column 7
    '-999.999',     # column 8
    '-999.999',     # column 9
    '-999.999',     # column 10
    '-999.999',     # column 11
    '-999.999',     # column 12
    '-999.999',     # column 13
    '-',            # column 14
    '-999.999',     # column 15
    '-',            # column 16
    '-'             # column 17
]


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
                row[0:21].strip(),              # column 1
                row[21:25].strip(),             # column 2
                row[26:28].strip(),             # column 3
                row[29:35].strip(),             # column 4
                row[38:41].strip(),             # column 5
                row[41:47].strip(),             # column 6
                row[48:53].strip(),             # column 7
                row[54:58].strip(),             # column 8
                row[59:64].strip(),             # column 9
                row[65:70].strip(),             # column 10
                row[71:76].strip(),             # column 11
                row[77:83].strip(),             # column 12
                row[84:90].strip(),             # column 13
                row[91:99].strip(),             # column 14
                row[100:103].strip(),           # column 15
                row[105:109].strip(),           # column 16
                row[111:len(row)].strip()       # column 17
            ]
            
            for idx, column in enumerate(newrow, start=0):
                if not column:
                    newrow[idx] = MISSING_VALUES[idx]

            with open(new_abspath, 'a+') as new_csv_file:
                spamwriter = csv.writer(new_csv_file, delimiter=',')
                spamwriter.writerow(newrow)


# Execute main
main( file=abspath )