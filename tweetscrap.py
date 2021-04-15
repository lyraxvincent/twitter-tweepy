import tweepy

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

# Authorization to consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Access to user's access key and access secret
auth.set_access_token(access_key, access_secret)

# Calling api
api = tweepy.API(auth)

def get_tweets(username):
    tweets = api.user_timeline(screen_name=username)  # Use count='' to specify no. of tweets to extract
    tmp = []

    # create array of tweet information:
    # tweet id(tweets.id), date/time(tweets.created_at, text(tweets.text)
    # location(tweets.location), geo enabled?(tweets.geo_enabled)
    # verified?(tweets.verified), description(tweets.description)
    # retweet count(tweets.retweet_count), likes(tweets.favorite_count)

    tweets_text = [tweet.text for tweet in tweets]  # CSV file created
    for j in tweets_text:
        # Appending tweets to the empty array tmp
        tmp.append(j)

        # Printing the tweets
    print(tmp)

# Calling the function
#get_tweets('lyraxvincent')

def tweets_by_word_search(word):
    # Cursor(pagination)
    result = tweepy.Cursor(api.search, q=word).items(3) # adjust items accordingly
    tweets = []
    for tweet in result:
        tweets.append(tweet.text)

    # printing the tweets
    print(tweets)

# Calling the function
#tweets_by_word_search('coronavirus')

def get_tweets_country(country_code):
    places = api.geo_search(query=country_code, granularity="country")
    place_id = places[0].id

    tweets = api.search(q="place:%s" %place_id, count=10)

    tweets_data = []
    for tweet in tweets:
        tweets_data.append(tweet.text)

    # printing the tweets
    print(tweets_data)

# Calling the function
get_tweets_country("KE")
