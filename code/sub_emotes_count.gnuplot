# Template for graphing over length of event
# Col 0: who 'owns' the emotes

# ** Cropped in Gimp, because it's late :/ **

set title "Number of Twitch Emotes Used Belonging to a Popular Streamer"
filename = "sub_emotes_total.png"
unset key

#set logscale y
#set yrange [1:50000]
set yrange [0:4000]

set size ratio 1920/1080
set terminal png size 1920,1080 enhanced
set output filename

set boxwidth 0.6
set style fill solid

#plot "data/emote_sub_breakdown_.data" using 1:3:xtic(2) with boxes lc rgb '#f47425'
#set label "16915" at -0.3,4050

data = "data/emote_sub_breakdown.data"
plot data using 1:3:xtic(2) with boxes lc rgb '#f47425', \
    data using 1:(75):(sprintf("%d",$3)) with labels notitle
    #data using 1:($3+75):(sprintf("%d",$3)) with labels notitle

