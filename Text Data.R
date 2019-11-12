library(qdap)
library(dplyr)
library(ggthemes)
library(RWeka)
library(reshape2)
library(tm)
library(wordcloud)
library(plotrix)
library(dendextend)
library(ggplot2)
library(SnowballC)

review = read.csv("E:/projectfix/Womens Clothing E-Commerce Reviews.csv", stringsAsFactors = FALSE)

##------ Pie Chart ------##
# most frequent terms
term_freq <- freq_terms(corpus_r, 10)

Review_df <- term_freq %>%
  arrange(desc(WORD)) %>%
  mutate(prop = round(FREQ*100/sum(FREQ), 1),lab.ypos = cumsum(prop) - 0.5*prop)
head(Review_df, 4)

ggplot(Review_df, aes(x = "", y = prop, fill = WORD)) +
  labs(x = NULL, y = NULL, fill = NULL, title = "Top 10 frequent used Words",caption="Source: Kaggle")+
  geom_bar(width = 5, stat = "identity", color = "grey") +
  geom_text(aes(y = lab.ypos, label = paste(round(prop), Sep=" %")), 
            color = "white")+coord_polar("y", start = 0)+ggpubr::fill_palette("jco")+
  theme_classic() +
  theme(axis.line = element_blank(),
        axis.text = element_blank(),
        axis.ticks = element_blank(),
        plot.title = element_text(hjust = 0.5, color = "#666666"))

# Print the word cloud with the specified colors
wordcloud(review_word_freq$term, review_word_freq$num,
          max.words = 50, colors = c("aquamarine","blue","red"))
