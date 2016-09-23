# Template for graphing over length of event
# Col 0: minutes into the event:


#gnuplot> load "code/comments_live.gnuplot"
#gnuplot> set terminal png enhanced
#gnuplot> set output filename
#gnuplot> replot
#
# ** Cropped in Gimp, because it's late :/ **

set title "Twitch Comments per Minute"
filename = "comments_per_min_live.png"

set yrange [0:800]
set xrange [0:12*3*60+60]   #minutes of the event 
                            #(allow for overflow on the last day)
set size ratio 1920/1080
unset key


set label 1  "Introduction"     at   30-10,500 rotate by 45 
set label 2  "6v6 NA vs EU"     at  150-10,500 rotate by 45
set label 3  "Communities Pub"  at  270-10,500 rotate by 45
set label 4  "1v1 MGE Tourney"  at  390-10,500 rotate by 45
set label 5  "TF2 Variety Block"at  450-10,500 rotate by 45
set label 6  "Pubs"             at  570-10,500 rotate by 45
set label 7  "Dreamcast"        at  630-10,500 rotate by 45
set label 8  "MvM"              at  690-10,500 rotate by 45

set label 10 "Intro Pubs"       at  750-10,500 rotate by 45
set label 11 "Source Filmmaker" at  810-10,500 rotate by 45
set label 12 "Variety Block"    at  930-10,500 rotate by 45
set label 13 "Pubs"             at  990-10,500 rotate by 45
set label 14 "Ultiduo Tourney"  at  1050-10,500 rotate by 45
set label 15 "Pubs"             at  1110-10,500 rotate by 45
set label 16 "TF2 Surf"         at  1170-10,500 rotate by 45
set label 17 "Co-op Pubbing"    at  1230-10,500 rotate by 45
set label 18 "Jackbox"          at 1290-10,500 rotate by 45
set label 19 "Day 2 Wrap- Pubs" at  1350-10,500 rotate by 45

set label 20 "Intro Pubs"       at  1470-10,500 rotate by 45
set label 21 "Source Filmmaker" at  1530-10,500 rotate by 45
set label 22 "Pubs"             at  1590-10,500 rotate by 45
set label 23 "Jump"             at  1650-10,500 rotate by 45
set label 24 "Pubs"             at  1770-10,500 rotate by 45
set label 25 "Variety Block"    at  1830-10,500 rotate by 45
set label 26 "Pubs"             at  1890-10,500 rotate by 45
set label 27 "Keep Talking and ..." at 1950-10,500 rotate by 45
set label 28 "Dota Fortress"    at  2010-10,500 rotate by 45
set label 29 "Event Wrap"       at  2130-10,500 rotate by 45

set xtics 60*12 #majors: every day
set mxtics 12   #minors: every hour

set style line 42 lc rgb 'black' lt 1 
set style line 43 lc rgb 'black' lt 0
set grid xtics mxtics ls 42, ls 43

#custom labels on x axis
set format x ""
set xtics offset 15 add ("Day 1" 0, "Day 2" 720, "Day 3" 1440)

set terminal png size 1920,1080 enhanced
set output filename
data = "data/comment_freq_all.data"
plot data smooth csplines lc rgb '#6441a4' lw 2.5, \
     data with points lc rgb '#f47425'

