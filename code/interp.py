#!/usr/bin/python3
# Extract data from a git repo into a csv

# This file is a template that extracts tipofthehats.org/stats from the log.sh git repo

from subprocess import PIPE, Popen, STDOUT
from datetime import datetime
import re

outfile = "donations.data"
infile  = "toth_stats"
repo    = "shell.git"   #python3 code/interp.py

def extract(text):
    #get relevant data
    #TODO: change this for each file you extract data from
    #text = text[2:-1]   #strip `b""`
    if 'NaN' in text or text == '':     #lol
        return None
    search = re.search("[\d,]+", text)
    if search is None:
        print("Invalid:")
        print(text)
        exit(0)
    else:
        n = search.group()
        n = n.replace(",", "")
        return str(int(n))  #throw error if this fails

def translate_date(date):
    #input: date string from git
    #output: something gnuplot likes
    #TODO: change this to something that makes sense
    #date = date[2:-1]   #strip `b""`
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S %z')
    return str(date)

def main():
    #There is absolutely a better way to extract git data rather than
    # `subprocesses` and regexes, but I don't have the time to learn it
    # (also this part doesn't have to be pretty)

    f = open(outfile, 'a')
    f.write("#start\n")
    f.write("# timestamp, \tdata\n")

    log = Popen(["git", "--git-dir="+repo, "log"], stdout=PIPE)
    #log = str(log.stdout.read())
    log = log.stdout.read().decode()

    commits = re.findall("commit ([0-9a-f]{40})", log)

    for commit in commits[::-1]:
        proc = Popen(["git", "--git-dir="+repo, "show", commit+':'+infile], stdout=PIPE)
        #text = str(proc.stdout.read().strip())
        text = proc.stdout.read().strip().decode()
        text = extract(text)
        if text is None:
            continue
        proc = Popen(["git", "--git-dir="+repo, "show", "-s", "--format=%ci", commit], stdout=PIPE)
        #date = str(proc.stdout.read().strip())
        date = proc.stdout.read().strip().decode()
        date = translate_date(date)
        f.write(date + ",\t" + text + "\n")

    f.close()
    print("Processed ", len(commits), " commits")

if __name__=="__main__":
    main()
