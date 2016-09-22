#!/usr/bin/python3

#count the number of emotes per minute for each minute the stream was live
#output in gnuplot-friendly format
#alternately, count the number of times 'query' appears in each minute
#searches for query with whitespace before and after

import sys, re

def cheat():
    # Don't look at me BibleThump
    if len(sys.argv) != 3:
        print("USAGE: python3 comment_count.py irssi_log output") 
        exit(1)
    f_input = open(sys.argv[1], 'r')
    f_output = open(sys.argv[2], 'w')

    full_text = f_input.read()  #wince
    start_index = full_text.index('\n--- Day changed Fri Sep 16 2016\n')
    text = full_text[start_index:]
    parts = text.split('\n--- Day changed') #list of the full text for all days
    print(len(parts))
    # parts[0] = Friday 16th = day 1
    for day in range(16,20):
        day_index = day - 15
        for hour in range(24):
            for minute in range(60):
                time = str(hour).zfill(2) + ':' + str(minute).zfill(2)
                #print("Searching for `" + time + "`")
                #exit(0)
                #n = parts[day_index].count('\n' + time)
                if (16 <= day <= 18 and hour >= 12) or (day == 19 and hour == 0):
                    n = parts[day_index].count(time)
                    #if time in parts[day_index]:
                    #    first = parts[day_index].index(time)
                    #    stop = parts[day_index].index('\n', first)
                    #    print('\t' + parts[day_index][first:stop], "\t(" + str(n) + ")")
                    x = (day_index-1) * 12*60 
                    x += (hour%12) * 60
                    x += minute
                    date = "Sept " + str(day) + ", " + time
                    f_output.write(str(x)+', \t'+str(n)+', \t#'+date+'\n')
    f_output.close()




def main():
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("USAGE: python3 comment_count.py irssi_log out_file query")
        exit(1)
    
    if len(sys.argv) == 3:
        query = None
    else:
        query = sys.argv[3]

    log_file = open(sys.argv[1], 'r')
    out_file = open(sys.argv[2], 'w')

    if query:
        out_file.write("# Counts per minute of `" + query + "`\n")
    else:
        out_file.write("# Number of lines of twitch chat per minute\n")

    #seek to first day
    for line in log_file:
        if line.strip() == "--- Day changed Fri Sep 16 2016":
            print("Found Fri 16th")
            break

    #iterate through lines
    last_time = (None, None)    # (hour, minute)
    date = 16
    freqs = [[[0]*60]*24]*4     # freq[date-16][hour][minute] = 0 (but don't offset hour)
    coords = []
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
        if (date, hour, minute) == (16, 12, 0):
            print('\t', line[:-1])
        if (hour >= 12 and 16 <= date <= 18) or (hour == 0 and date == 19):
            #valid times when stream was live that our graph can represent
            #if hour > 12:
            #    hour -= 12
            if query:
                count = len(re.findall("\s" + query + "\s", line + " "))
                freqs[date-16][hour][minute] += count
            else:
                freqs[date-16][hour][minute] += 1
    log_file.close()
    #output freqs as numbers that gnuplot likes
    #x value is the number of minutes since the start of the event
    # with breaks when the stream is down for the nights
    for date in range(4):
        date_ = date + 16
        for hour in range(24):
            if False == ((hour>=12 and 16<=date_<=18) or (hour==0 and date_==19)):
                continue
            for minute in range(60):
                x_val = get_xval(date_, hour, minute)
                y_val = freqs[date][hour][minute]
                coords.append((x_val, y_val))
                out_file.write(str(x_val) + ',\t' + str(y_val) + '\n')
    out_file.close()
    #return (freqs, coords)




def get_xval(date, hour, minute):
    #if hour > 12:
        #hour -= 12

    if 16 <= date <= 18:
        guess = ((date-16)*12 + hour)*60 + minute
    elif date == 19 and hour == 0:
        guess = 3*12*60 + minute
    else:
        assert(False)
        return None

    return guess
    #if date == 16:
    #    return guess
    #elif date == 17:
    #    return guess - 12*60
    #elif date == 18:
    #    return guess - 24*60
    #elif date == 19:
    #    return guess - 24*60

if __name__=="__main__":
    #main()
    cheat()

#Goddamn this prof has great quotes

#"Computer will be taking over the world unless you understand them!"
# Do you want a computer telling you when to go to the bathroom?

# "Oh man I just thought of a joke... uh... Do we have any deeply religious people here?"

# "In Russia we learned English because it was the language of the enemy. Now we must learn computers to prepare for the war"


