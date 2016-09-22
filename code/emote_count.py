#!/usr/bin/python3
# wget https://twitchemotes.com/api_cache/v2/global.json
# wget https://twitchemotes.com/api_cache/v2/subscriber.json
# Takes about 20 minutes to run on an i5 2300
#sort -h -r results > emote_counts.data

import re, json

f1 = open('subscriber.json', 'r')
f2 = open('global.json', 'r')
f3 = open('results', 'w')

sub_emotes = re.findall('{"code":"(\w+)"', f1.read())
glb_emotes = list(json.loads(f2.read())['emotes'])
smileys = [">\(",":D",":z","o_O",":B\)", "<3", "R\)", ":\(", ":\)", ":P", ":o", ":\\", ";p", ";\)"]
#lol gotta escape parens or regex gets screwed up 99% of the way through
emotes = sub_emotes + glb_emotes + smileys

print("Sub emotes: " + str(len(sub_emotes)))
print("All emotes: " + str(len(glb_emotes)))
print("Lil faces:  " + str(len(smileys)))
print("Total: " + str(len(emotes)))

f1.close()
f2.close()

log = open('data/#tipofthehats.log', 'r').read()
log = log.replace("\n", " \n")  #makes it easier to search for emotes

print("And here... we..... go")

#counts = []
for emote in emotes:
    #ignore super short emotes because they're not what people were using
    #this ignores the faces though...
    #should just omit counts less than 12 or something
    #if len(emote) < 4:
        #continue
    #count must be case sensitive (i.e. ignore typos)
    #count = log.count(" " + emote)  #start with a space  $omits overlaps 
    count = len(re.findall(' ' + emote + ' ', log))
    if count == 0:
        continue
    #counts.append(count)
    f3.write(str(count) + ',\t' + emote + '\n')

f3.close()



