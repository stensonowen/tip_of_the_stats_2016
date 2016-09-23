# Template for graphing over like 10 days # Col 0: UNIX timestamp
# Day borders in EST

set title "Total Donations (USD)"
filename = "total_donations_all.png"

# xrange: beginning of Friday 9/9 to end of Monday 9/20
set xrange [1473393600:1474344000]
set yrange [0:200000]

set size ratio 1920/1080
unset key

day_len = 60*60*24  #seconds per day

#fix x-axis labeling
set xtics ""
set format x ""
set xtics offset 4.7 add ( "Fri" 1473393600+day_len*0, \
                "Sat" 1473393600+day_len*1, \
                "Sun" 1473393600+day_len*2, \
                "Mon" 1473393600+day_len*3, \
                "Tue" 1473393600+day_len*4, \
                "Wed" 1473393600+day_len*5, \
                "Thu" 1473393600+day_len*6, \
                "Fri" 1473393600+day_len*7, \
                "Sat" 1473393600+day_len*8, \
                "Sun" 1473393600+day_len*9, \
                "Mon" 1473393600+day_len*10 )
set grid xtics ls 0

set terminal png size 1920,1080 enhanced
set output filename

plot "data/donations_all_no_overflow.data" lc rgb '#f47425'

