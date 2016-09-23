#Pie chart of emote distribution
# used dev.print() because it's pretty late

data <- read.csv("../data/top_15_emotes.data", sep=",", header=F, col.names=c('count','emote','pct'));
cols <- rainbow(nrow(data));
lbls <- paste(data$emote, ' (', data$pct, '%)', sep='')
chart <- pie(data$count, labels=lbls, col=cols, radius=1.08);
title("Emote Distribution")


