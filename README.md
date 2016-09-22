#Tip of the Stats 2016

###*Unofficial* Statistics Collected for Tip of the Hats 2016

I collected some data on this year's [Tip of the Hats](https://tipofthehats.org), a charity livestream put on by the Team Fortress 2 community benefitting [One Step Camp](http://www.onestepcamp.org/). Some stats from last year can be found [here](https://github.com/stensonowen/toth_stats) (and reddit discussion [here](https://redd.it/3ly23g))

I used a combination of programs to collect data: 
* a [large multi-purpose Rust project](https://github.com/stensonowen/page-mon/tree/git) I wrote over the summer; here it logged Twitch viewers and [toth donations](https://tipofthehats.com/stats) to a git repo (config file [here](/code/config)), 
* a gross [shell script](/code/log.sh) I threw together that does exactly the same thing as the Rust project just in case (and because I wasn't sure it would be ready on time) to monitor the same data, 
* and [irssi](https://irssi.org/), a command-line IRC client, to record the Twitch chat.

Neither the rust project nor the shell hack ended up breaking horribly, so I ended up using both.

