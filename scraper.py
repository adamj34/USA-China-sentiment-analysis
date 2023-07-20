import re
import pandas as pd
import snscrape.modules.twitter as sntwitter


# Setting variables to be used below
maxTweets = 800
year_start = 2013
year_end = 2023


# Creating list to append tweet data
china_tweets_list = []

# Loop over each year
for year in range(year_start, year_end):
    # Loop over each month
    for month in range(1, 13):
        if month == 12:
            query = f'#China since:{year}-{month}-02 until:{year+1}-01-01 lang:en'
        else:
            query = f'#China since:{year}-{month}-02 until:{year}-{month+1}-01 lang:en'

        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i >= maxTweets:  # We use 'greater than or equal to' as indices start at 0
                break
            china_tweets_list.append([tweet.date, re.sub(r"http\S+", "", tweet.rawContent)])

# Creating a dataframe from the tweets list above
china_tweets_df = pd.DataFrame(china_tweets_list, columns=['Datetime', 'Content'])

china_tweets_df.to_csv('china_tweets.csv', index=False)



# Creating list to append tweet data
usa_tweets_list = []

# Loop over each year
for year in range(year_start, year_end):
    # Loop over each month
    for month in range(1, 13):
        if month == 12:
            query = f'(#theus OR #america) since:{year}-{month}-02 until:{year+1}-01-01 lang:en'
        else:
            query = f'(#theus OR #america) since:{year}-{month}-02 until:{year}-{month+1}-01 lang:en'

        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i >= maxTweets:  # We use 'greater than or equal to' as indices start at 0
                break
            usa_tweets_list.append([tweet.date, re.sub(r"http\S+", "", tweet.rawContent)])

# Creating a dataframe from the tweets list above
usa_tweets_df = pd.DataFrame(usa_tweets_list, columns=['Datetime', 'Content'])

usa_tweets_df.to_csv('usa_tweets.csv', index=False)