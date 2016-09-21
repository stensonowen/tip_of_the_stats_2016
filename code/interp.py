#!/usr/bin/python3 # Extract data from a git repo into a csv

# This file is a template that extracts tipofthehats.org/stats from the log.sh git repo

# git --git-dir=/... foo

from subprocess import PIPE, Popen, STDOUT
from datetime import datetime
import re

outfile = "donations_pm2.data"
#infile  = "toth_stats"
infile  = "tipofthehats.org~stats~360128143.cache"
#infile  = "tipofthehats.org~stats~579716887.cache"
#repo    = "shell.git"   #python3 code/interp.py
repo    = "page_mon.git"   #python3 code/interp.py

(outfile, infile, repo) = ("donations_shell_whole.data", "toth_stats", "shell.git")
(outfile, infile, repo) = ("donations_pm1_whole.data", "tipofthehats.org~stats~360128143.cache", "page_mon.git")
(outfile, infile, repo) = ("donations_pm2_whole.data", "tipofthehats.org~stats~579716887.cache", "page_mon.git")

(outfile, infile, repo) = ("viewers_shell_whole.data", "twitch_stats", "shell.git")

(outfile, infile, repo) = ("viewers_shell_live.data", "twitch_stats", "shell.git")
(outfile, infile, repo) = ("viewers_pm_live.data", "api.twitch.tv~krakenstreamstipofthehats~725618889.cache", "page_mon.git")

(outfile, infile, repo) = ("donations_shell_live.data", "toth_stats", "shell.git")
(outfile, infile, repo) = ("donations_pm_live1.data", "tipofthehats.org~stats~360128143.cache", "page_mon.git")

(outfile, infile, repo) = ("donations_shell_all.data", "toth_stats", "shell.git")
(outfile, infile, repo) = ("donations_pm_all.data", "tipofthehats.org~stats~360128143.cache", "page_mon.git")



ALLOW_DAY_OVERFLOW = False

def extract_viewers(text):
    #get 'viewers' from twitch api call
    search = re.search('"viewers":(\d+)', text)
    if search is None:
        #print("Invalid:")
        #print(text)
        return None
    else:
        n = search.group(1)
        return str(int(n))

def extract_donations(text):
    #get relevant data
    #TODO: change this for each file you extract data from
    #text = text[2:-1]   #strip `b""`
    if 'NaN' in text or text == '':     #lol
        return None
    search = re.search("[\d,]+", text)
    if search is None:
        print("Invalid:")
        print(text)
        #exit(0)
        return None
    else:
        n = search.group()
        n = n.replace(",", "")
        return str(int(n))  #throw error if this fails

def extract_date(date):
    #input: date string from git
    #output: minutes into the event
        #start of event is 0
        #if one day goes over, then it should leak into the next day
        #unless it's the last day, in which it should just increase
    dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S %z')
    dt_nix = int(dt.timestamp())

    start_nix = 1474041600
    if dt_nix < start_nix:
        #I'm dumb so there's none of these :/ (* in the viewer category)
        return None

    if ALLOW_DAY_OVERFLOW == False:
        #allow 1 hour of overflow at the end
        in_bounds = [start <= dt_nix < end for (start,end) in ((1474041600,1474084800),
                            (1474128000,1474171200),
                            (1474214400,1474261200))]
        if all([ib == False for ib in in_bounds]):
            return None

    #use 6am instead of midnight because stream sometimes passed midnight
    day1_6am      = 1474020000
    day1_midnight = 1473998400
    day_len = 24*60*60
    twelve_hours = 12*60*60

    #how many groups of 24 hours since 6am on the first day
    day_num             = (dt_nix - day1_6am) // day_len
    seconds_since_6am   = (dt_nix - day1_6am) % day_len
    minutes_since_noon  = (seconds_since_6am - 6*60*60)//60

    x_val = minutes_since_noon + day_num * 12*60
    if x_val < 0:
        print("ERROR: ", date, '\t', day_num, '\t', x_val)
        exit(1)
    return str(x_val)
    

def translate_date(date):
    #input: date string from git
    #output: something gnuplot likes
    #TODO: change this to something that makes sense
    #date = date[2:-1]   #strip `b""`
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S %z')
    return str(int(date.timestamp()))

def main():
    #There is absolutely a better way to extract git data rather than
    # `subprocesses` and regexes, but I don't have the time to learn it
    # (also this part doesn't have to be pretty)

    #TODO: remember to change these
    #extract_fn = extract_viewers    #extract_donations
    extract_fn = extract_donations
    datetime_fn = translate_date    #keep all results
    #datetime_fn = extract_date      #only use results while event was live

    f = open(outfile, 'a')
    f.write("#start\n")
    f.write("# timestamp, \tdata\n")

    #keep track of last value: only include updates
    #last = ""

    log = Popen(["git", "--git-dir="+repo, "log"], stdout=PIPE)
    #log = str(log.stdout.read())
    log = log.stdout.read().decode()

    commits = re.findall("commit ([0-9a-f]{40})", log)

    for commit in commits[::-1]:
        proc = Popen(["git", "--git-dir="+repo, "show", commit+':'+infile], stdout=PIPE)
        #text = str(proc.stdout.read().strip())
        text = proc.stdout.read().strip().decode()

        text = extract_fn(text)

        #skip if this isn't new info
        if text is None: # or text == last:
            #print("Same: ", last, commit)
            continue
            #pass
        #else:
        #    last = text[:]
        proc = Popen(["git", "--git-dir="+repo, "show", "-s", "--format=%ci", commit], stdout=PIPE)
        #date = str(proc.stdout.read().strip())
        date = proc.stdout.read().strip().decode()
        date = datetime_fn(date)
        if date is None:
            continue
        #f.write(str(int(date)) + ",\t" + text + "\n")
        f.write(date + ",\t" + text + "\n")

    f.close()
    print("Processed ", len(commits), " commits")
    print("Wrote to file: " + outfile)

if __name__=="__main__":
    main()
