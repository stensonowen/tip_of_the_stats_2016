#!/bin/dash
# stupid ugly hack to keep track of web pages until stupid elegant masterpiece is done
# keep track of statistics regarding #Toth2016 in a git repo
# TODO: remember to `git init` first

delay=50   # ≅ 1 min
count=0

while [ true ]
do

    #Collect Stats
    echo "$count:  `date`"

    #toth.org (awesome!)
    wget https://tipofthehats.org/stats             -O toth_stats           2> /dev/null

    #twitch.tv
    curl -H 'Accept: application/vnd.twitchtv.v3+json' -H 'Client-ID: ***REDACTED***' -X GET https://api.twitch.tv/kraken/streams/tipofthehats -o twitch_stats 2> /dev/null
    #scrap.tf
    # didn't know which was which
    wget https://scrap.tf/toth                    -O scraptf_toth           2> /dev/null
    wget https://scrap.tf/tothgiveaways           -O scraptf_tothgiveaways  2> /dev/null
    wget https://scrap.tf/toth/donations          -O scraptf_tothdonations  2> /dev/null
    wget https://scrap.tf/tothgiveaways/donations -O scraptf_tothgiveaways_donations 2> /dev/null

    #git stuff
    #I guess adding individually is the best way to mitigate errors??
    git add toth_stats
    git add twitch_stats
    git add scraptf_toth
    git add scraptf_tothgiveaways
    git add scraptf_tothdonations
    git add scraptf_tothgiveaways_donations

    git commit -m "Commit #$count" > /dev/null


    #Wait for next iter
    echo "    Finished iter $count at `date`"
    count=$((count+1))
    sleep $delay

done


