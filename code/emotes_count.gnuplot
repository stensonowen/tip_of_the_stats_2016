# Template for graphing over length of event
# Col 0: minutes into the event:


#gnuplot> load "code/comments_live.gnuplot"
#gnuplot> set terminal png enhanced
#gnuplot> set output filename
#gnuplot> replot
#
# ** Cropped in Gimp, because it's late :/ **

set title "Different Twitch Emotes per Hour"
filename1 = "emotes_per_hour_live_A.png"
filename2 = "emotes_per_hour_live_B.png"
set key left top

set logscale y
set yrange [1:10000]
set xrange [0:12*3*60+60]   #minutes of the event 
                            #(allow for overflow on the last day)
set size ratio 1920/1080


set label 1  "Introduction"     at   30,01.1 rotate by 90 
set label 2  "6v6 NA vs EU"     at  150,1.1 rotate by 90
set label 3  "Communities Pub"  at  270,1.1 rotate by 90
set label 4  "1v1 MGE Tourney"  at  390,1.1 rotate by 90
set label 5  "TF2 Variety Block"at  450,1.1 rotate by 90
set label 6  "Pubs"             at  570,1.1 rotate by 90
set label 7  "Dreamcast"        at  630,1.1 rotate by 90
set label 8  "MvM"              at  690,1.1 rotate by 90

set label 10 "Intro Pubs"       at  750,1.1 rotate by 90
set label 11 "Source Filmmaker" at  810,1.1 rotate by 90
set label 12 "Variety Block"    at  930,1.1 rotate by 90
set label 13 "Pubs"             at  990,1.1 rotate by 90
set label 14 "Ultiduo Tourney"  at  1050,1.1 rotate by 90
set label 15 "Pubs"             at  1110,1.1 rotate by 90
set label 16 "TF2 Surf"         at  1170,1.1 rotate by 90
set label 17 "Co-op Pubbing"    at  1230,1.1 rotate by 90
set label 18 "Jackbox"          at 1290,1.1 rotate by 90
set label 19 "Day 2 Wrap- Pubs" at  1350,1.1 rotate by 90

set label 20 "Intro Pubs"       at  1470,1.1 rotate by 90
set label 21 "Source Filmmaker" at  1530,1.1 rotate by 90
set label 22 "Pubs"             at  1590,1.1 rotate by 90
set label 23 "Jump"             at  1650,1.1 rotate by 90
set label 24 "Pubs"             at  1770,1.1 rotate by 90
set label 25 "Variety Block"    at  1830,1.1 rotate by 90
set label 26 "Pubs"             at  1890,1.1 rotate by 90
set label 27 "Keep Talking and ..." at 1950,1.1 rotate by 90
set label 28 "Dota Fortress"    at  2010,1.1 rotate by 90
set label 29 "Event Wrap"       at  2130,1.1 rotate by 90

set xtics 60*12 #majors: every day
set mxtics 12   #minors: every hour

set style line 42 lc rgb 'black' lt 1 
set style line 43 lc rgb 'black' lt 0
set grid xtics mxtics ls 42, ls 43

#custom labels on x axis
set format x ""
set xtics offset 15 add ("Day 1" 0, "Day 2" 720, "Day 3" 1440)

data = "data/pop_emote_variation.data"
set terminal png size 1920,1080 enhanced

set output filename1
plot    data using 1:2 smooth csplines lw 2 title 'PogChamp'     , \
        data using 1:5 smooth csplines lw 2 title 'GivePLZ'      , \
        data using 1:7 smooth csplines lw 2 title 'Kappa'

set output filename2
plot    data using 1:3 smooth csplines lw 2 title 'BibleThump'   , \
        data using 1:6 smooth csplines lw 2 title 'PipeHype'     , \
        data using 1:8 smooth csplines lw 2 title 'tothHeart'    , \
        data using 1:4 smooth csplines lw 2 title '<3'
