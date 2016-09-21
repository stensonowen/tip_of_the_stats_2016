#!/use/bin/python3
# Remove "duplicates" in a list of datetimes / values
# A duplicate is indicated by consecutive values

import sys

def main():
    if len(sys.argv) != 3:
        print("USAGE: python3 dedup.py file_in file_out")
        exit(1)
    file_in = sys.argv[1]
    file_out = sys.argv[2]

    fi = open(file_in, 'r')
    fo = open(file_out, 'w')

    last = None

    for line in fi:
        if '#' in line or len(line) < 1:
            #comment/empty
            fo.write(line)
            continue
        value = line.split()[-1] 
        if last == value: 
            continue
        last = value
        fo.write(line)
    fi.close()
    fo.close()

if __name__=="__main__":
    main()
