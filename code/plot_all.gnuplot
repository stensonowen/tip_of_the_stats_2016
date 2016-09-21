# Template for graphing over like 10 days # Col 0: UNIX timestamp
# TODO: fix the font

unset key
set title "Total Donations"

# xrange: beginning of Friday 9/9 to end of Monday 9/20
set xrange [1473393600:1474344000]
set yrange [0:200000]

day_len = 60*60*24  #seconds per day

set ylabel "US Dollars Raised"
set xlabel "Day (EST)"

#fix x-axis labeling
set xtics ""
#TODO: fix offset?
set xtics offset 2.3 add (  "Fri" 1473393600+day_len*0, \
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

plot "data/donations_all_no_overflow.data" lc rgb '#f47425'
