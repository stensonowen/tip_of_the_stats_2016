#!/usr/bin/python3

#count the number of emotes per minute for each minute the stream was live
#output in gnuplot-friendly format
#alternately, count the number of times 'query' appears in each minute
#searches for query with whitespace before and after

# takes 3 sec for pop emotes on whole chat
# takes 26 sec for whole

import sys, re

def cheat():
    # Don't look at me BibleThump
    # I rewrote this for the purpose of validating results for debugging,
    # bue it's getting late so I'm just going to use it. This is NOT an 
    # effective way of doing things
    if len(sys.argv) != 4:
        print("USAGE: python3 comment_count.py irssi_log emote_file output") 
        exit(1)
    f_input = open(sys.argv[1], 'r')
    f_emotes = open(sys.argv[2], 'r')
    f_output = open(sys.argv[3], 'w')

    emotes = f_emotes.read().split('\n')
    f_output.write('Min,\t' + ', '.join([emote.rjust(16) for emote in emotes]) + '  # Date\n')

    full_text = f_input.read()  #wince
    start_index = full_text.index('\n--- Day changed Fri Sep 16 2016\n')
    text = full_text[start_index:]
    #make things easier to search:
    text = text.replace(' ', '  ').replace('\n', ' \n')   #going to search spaces around emote
    parts = text.split('\n---  Day  changed') #list of the full text for all days
    print(len(parts))
    # parts[0] = Friday 16th = day 1
    for day in range(16,20):
        day_index = day - 15
        for hour in range(24):
            time = str(hour).zfill(2) + ':'
            #relevant_lines = [l if l[:3] == time in parts[day_index]] 
            relevant_lines = []
            for l in parts[day_index].split('\n'):
                if l[:3] == time:
                    relevant_lines.append(l)
            #print(len(relevant_lines))
            if (16 <= day <= 18 and hour >= 12) or (day == 19 and hour == 0):
                #data = [parts[day_index].count(' '+emote+' ') for emote in emotes]
                data = ['\n'.join(relevant_lines).count(' '+emote+' ') for emote in emotes]
                data = ', '.join([str(datum).rjust(16) for datum in data])
                #n = parts[day_index].count('\n' + time)
                minute = 30
                x = (day_index-1) * 12*60 
                x += (hour%12) * 60
                x += minute
                date = "Sept " + str(day) + ", " + time

                line = str(x).zfill(3) + ', ' + data + ',  \t# ' + date + '\n'
                f_output.write(line)
                #f_output.write(str(x)+', \t'+str(n)+', \t#'+date+'\n')
    f_output.close()

if __name__=="__main__":
    cheat()

