#!/usr/bin/python3

#count the number of emotes per minute for each minute the stream was live
#output in gnuplot-friendly format

import sys, re

def main():
    if len(sys.argv) != 3:
        print("USAGE: python3 comment_count.py irssi_log out_file")
        exit(1)
    
    log_file = open(sys.argv[1], 'r')
    out_file = open(sys.argv[2], 'w')

    #seek to first day
    for line in log_file:
        if line.strip() == "--- Day changed Fri Sep 16 2016":
            break

    #iterate through lines
    last_time = (None, None)    # (hour, minute)
    date = 16
    freqs = [[[0]*60]*24]*4     # freq[date-16][hour][minute] = 0 (but don't offset hour)
    count = 0
    for line in log_file:
        if line[:15] == "--- Day changed":
            m = re.search("^--- Day changed ... Sep (\d+) 2016", line)
            date = int(m.group(1))
            print("Moved on to date: " + str(date))
            #break
        parts = line.split()
        #line.split()[0] is the time
        #line.split()[1] is '<'
        #line.split()[2] is the username + '>'
        #line.split()[3:] is the message
        if parts[1] != '<':     #e.g. == '-!-'
            continue
        hour    = int(parts[0][:2])
        minute  = int(parts[0][3:])
        if (hour >= 12 and 16 <= date <= 18) or (hour == 0 and date == 19):
            #valid times when stream was live that our graph can represent
            freqs[date-16][hour][minute] += 1
    log_file.close()
    #output freqs as numbers that gnuplot likes
    #x value is the number of minutes since the start of the event
    # with breaks when the stream is down for the nights
    for date in range(4):
        date_ = date + 16
        for hour in range(24):
            if False == ((hour >= 12 and 16 <= date_ <= 18) or (hour == 0 and date_ == 19)):
                continue
            for minute in range(60):
                x_val = get_xval(date_, hour, minute)
                y_val = freqs[date][hour][minute]
                out_file.write(str(x_val) + ',\t' + str(y_val) + '\n')
    out_file.close()




def get_xval(date, hour, minute):
    if 16 <= date <= 18:
        return ((date-16)*12 + hour)*60 + minute
    elif date == 19 and hour == 0:
        return 3*12*60 + minute
    else:
        assert(False)
        return None

if __name__=="__main__":
    main()
