#Tip of the Stats 2016

###*Unofficial* Statistics Collected for Tip of the Hats 2016

I collected some data on this year's [Tip of the Hats](https://tipofthehats.org), a charity livestream put on by the Team Fortress 2 community benefitting [One Step Camp](http://www.onestepcamp.org/). Some stats from last year can be found [here](https://github.com/stensonowen/toth_stats) (and reddit discussion [here](https://redd.it/3ly23g))

I used a combination of programs to collect data: 
* a [large multi-purpose Rust project](https://github.com/stensonowen/page-mon/tree/git) I wrote over the summer; here it logged Twitch viewers and [toth donations](https://tipofthehats.com/stats) to a git repo (config file [here](/code/config)), 
* a gross [shell script](/code/log.sh) I threw together that does exactly the same thing as the Rust project just in case (and because I wasn't sure it would be ready on time) to monitor the same data, 
* and [irssi](https://irssi.org/), a command-line IRC client, to record the Twitch chat.

Neither the rust project nor the shell hack ended up breaking horribly, so I ended up using both.

The python code mostly exists to transfer data from git repos into csv's simple enough for gnuplot can use. It's not particularly elegant python, but it did its job; it's probably not interesting or helpful enough to actually delve into, but I figured I'd upload it in case I made a mistake somewhere, so that it would be easier to track down.

I ended up using R for the [pie chart of the most popular emotes](/graphics/emote_distribution.png) because gnuplot seems to have some troubs with pie charts. Other than that, though, all the graphing is gnuplot.

(Apologies for missing some viewer data in the beginning of the event (again); twitch changed their api to require an oauth / client id for all requests, which I didn't realize, and surprisingly my 4am fix had a mistake)

All the rendered images can be found in [/graphics](/graphics). 
The code used to generate those images can be found in [/code/\*.gnuplot](/code) (and [/code/\*.R](/code)). 
The data those programs depend on are in [/data](/data). 
The programs used to collect that data are [/code/config](/code/config) and [/code/log.sh](/code/log.sh) (and [page-mon](https://github.com/stensonowen/page-mon)).

Shoutout Tip of the Hats.

