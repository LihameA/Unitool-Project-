# In this program, we print ut all the text data from our twitter JSON file.
import json
# Open JSON file. Tag file as "r" read only becasue we are only looking at the data.
tweetFile = open("../TwitterData/tweets_small.json","r") #r means we can only read/extract info, cant alter it (w) does that/
# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile) #load function is found in Json, so json.load.
#You NEED to close the file now that we have locally stored the data and later on could mess up code if open.
tweetFile.close()

#Print the data of ONE tweet
#The [0] denotes the *first* tweet object. In jason 'dictionary's are objects
print("Tweet.id", tweetData[0]["id"])

#Print text of first object
print("Tweet text:", tweetData[0]["text"])

for idx in range(len(tweetData)):
    print("Tweet text: " + tweetData[idx]["text"])
