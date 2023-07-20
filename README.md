# USA-China-sentiment-analysis

The aim of the project is to examine how the global community's attitude towards China and the USA has changed over the past 10 years (i.e., from 2013 to 2023). Sentiment analysis was conducted using tweets gathered with the help of snscrape library. Each country was analyzed based on approximately 96,000 tweets collected using the hashtags #america, #theus and #china.

The following tools were used to conduct the analysis:
* NLTK Vader - performs tokenization, lemmatization, and stop words removal on the tweets, while also categorizing them as negative, neutral, or positive
* DistilBERT fine-tuned for sentiment analysis - classifies tweets as either positive or negative
* DistilBERT Emotion - assignes one of the following emotions: joy, anger, fear, sadness, surprise, love to each tweet 