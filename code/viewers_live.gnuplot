# Template for graphing over length of event
# Col 0: minutes into the event:

set title "Twitch Viewers"
filename = "twitch_viewers_live.png"

set yrange [0:8000]
set xrange [0:12*3*60+60]   #minutes of the event 
                            #(allow for overflow on the last day)
set size ratio 1920/1080
unset key


set label 1  "Introduction"     at   30,150 rotate by 90 
set label 2  "6v6 NA vs EU"     at  150,150 rotate by 90
set label 3  "Communities Pub"  at  270,150 rotate by 90
set label 4  "1v1 MGE Tourney"  at  390,150 rotate by 90
set label 5  "TF2 Variety Block"at  450,150 rotate by 90
set label 6  "Pubs"             at  570,150 rotate by 90
set label 7  "Dreamcast"        at  630,150 rotate by 90
set label 8  "MvM"              at  690,150 rotate by 90

set label 10 "Intro Pubs"       at  750,150 rotate by 90
set label 11 "Source Filmmaker" at  810,150 rotate by 90
set label 12 "Variety Block"    at  930,150 rotate by 90
set label 13 "Pubs"             at  990,150 rotate by 90
set label 14 "Ultiduo Tourney"  at  1050,150 rotate by 90
set label 15 "Pubs"             at  1110,150 rotate by 90
set label 16 "TF2 Surf"         at  1170,150 rotate by 90
set label 17 "Co-op Pubbing"    at  1230,150 rotate by 90
set label 18 "Jackbox"          at 1290,150 rotate by 90
set label 19 "Day 2 Wrap- Pubs" at  1350,150 rotate by 90

set label 20 "Intro Pubs"       at  1470,150 rotate by 90
set label 21 "Source Filmmaker" at  1530,150 rotate by 90
set label 22 "Pubs"             at  1590,150 rotate by 90
set label 23 "Jump"             at  1650,150 rotate by 90
set label 24 "Pubs"             at  1770,150 rotate by 90
set label 25 "Variety Block"    at  1830,150 rotate by 90
set label 26 "Pubs"             at  1890,150 rotate by 90
set label 27 "Keep Talking and ..." at 1950,150 rotate by 90
set label 28 "Dota Fortress"    at  2010,150 rotate by 90
set label 29 "Event Wrap"       at  2130,150 rotate by 90

set xtics 60*12 #majors: every day
set mxtics 12   #minors: every hour

set style line 42 lc rgb 'black' lt 1 
set style line 43 lc rgb 'black' lt 0
set grid xtics mxtics ls 42, ls 43

set format x ""
set xtics offset 16 add ("Day 1" 0, "Day 2" 720, "Day 3" 1440)

set terminal png size 1920,1080 enhanced
set output filename

plot "data/viewers_live_no_overflow.data" lc rgb '#f47425'
