# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.

# Phrases = jobs, freedom, MAGA - I predict freedom will appear most

import json
import matplotlib.pyplot as plt

tweets = []                                  

for year in range(2009, 2019):                
    filename = f'master_{year}.json'          
    with open(filename, encoding='utf-8') as f:
        year_tweets = json.load(f)            # this file's list of tweets
    tweets += year_tweets                     # add them to the big list

print(len(tweets))


phrases = ['obama', 'trump', 'mexico', 'russia', 'fake news', 'freedom', 'maga', 'jobs']
counts = {}                       # a dictionary: phrase -> count
for phrase in phrases:
    counts[phrase] = 0         

for tweet in tweets:
    if 'full_text' in tweet:
        message = tweet['full_text'].lower()
    else:
        message = tweet['text'].lower()      
    for phrase in phrases:
        if phrase in message:
            counts[phrase] += 1
print(phrase, counts[phrase])

percent = {}
for phrase in phrases:
    percent[phrase] = counts[phrase] / len(tweets) * 100 
    print(phrase, percent[phrase])

print('| phrase            | percent of tweets |')
print('| ----------------- | ----------------- |')
for phrase in phrases:
    print(f'| {phrase} | {percent[phrase]:05.2f} |')

fig, ax = plt.subplots()

bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:purple', 'tab:green', 'tab:brown', 'tab:olive']

p = []
for phrase in phrases:
    p.append(counts[phrase])
ax.bar(phrases, p, color=bar_colors)

ax.set_ylabel('Counts')
ax.set_title('Count of Phrases in Trump Tweets 2009-2018')


plt.savefig('tweets.png')
plt.show()

# fig, ax = plt.subplots()

# bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:purple', 'tab:green', 'tab:brown', 'tab:olive']

# p2 = []
# for phrase in phrases:
#    p2.append(percent[phrase])
# ax.bar(phrases, p2, color=bar_colors)

# ax.set_ylabel('Percent of total words')
# ax.set_title('Percentage of Certain Tweeted Phrases Over Total Tweeted Words in Trump Tweets 2009-2018')


# plt.savefig('tweets1.png')
# plt.show()