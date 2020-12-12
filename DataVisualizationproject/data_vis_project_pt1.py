'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("./TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!

# Textblob sample:
'''
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity) #return the polarity of the statement above. output = .9

listOfPolarity = [] #This list stores polarity (negative or positive numbers tell us data about tweet)
listOfSubjectivity = [] #Deals with opinions, subjective to context

for tweet in tweetData: #for every element in tweedata
    anObject = TextBlob(tweet["text"]) #Getting tweet from TweetData, accessing key from a dictionary. tweet is key, text is value
    listOfPolarity.append(anObject.polarity)
    listOfSubjectivity.append(anObject.subjectivity)
print(listOfPolarity)
#print(listOfSubjectivity)
#Printing the Average

sum = 0
for polarity in listOfPolarity:
    sum = sum + polarity
    print(sum)
avgPolarity = sum/len(listOfPolarity)
print("The average polarity is: %f" %(avgPolarity))

sub_sum = 0
for subjectivity in listOfSubjectivity:
    sub_sum = sub_sum + subjectivity

avgSubjectivity = sub_sum/len(listOfSubjectivity)
print("The average subjectivity is: %f")%(avgSubjectivity)


sub_sum = 0
for subjectivity in listOfSubjectivity:
    sub_sum = sub_sum + subjectivity
print(listOfPolarity)
'''
#This is a histogram for twitterdata
#Create the graph
'''
#Creating a Histogram(Graph) Techincally part 2
plt.hist(listOfPolarity, bins = [-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.1])
plt.xlabel('polarities')
plt.ylabel('Number Of Tweets')
plt.title('Tweet polarity')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()#SHows ours graph
'''
#creating the word cloud
combinedTweets = "" #INitializing an empty string that will hold all of the strings
#Using a for loop to concatinate (add string) the tweets and then place them in the empty variable that will hold those strings.
for tweet in tweetData:
    combinedTweets += tweet['text']
#printCombinedTweets for testing

#Making a textblob of our entire string of tweets
tweetBlob = TextBlob(combinedTweets)#Tweet blkob is all of the tweets in the form of a text blob

#This is a list of words I dont wnat in my word cloud
wordsToFilter = ["about", "https", "in", "the", "thing", "will", "could", "automation", "is", "to", "and", "of"]

filteredDictionary = dict()

#POint of this for-loop is to filter the words in our big tweet
for word in tweetBlob.words: #Use atribute word in tweet blob to access the words from the tweets
    #the following if-statements are conditions for what types of words I want in my word cloud

    #skip small words
    if len(word) < 2:
        continue
    #Skips words with random characters or numbers
    if not word.isalpha():
        continue
    if word.lower() in wordsToFilter:  #lowercase ebverything b/c everything in wordsToFilter is lowercase
        continue
    filteredDictionary[word.lower()] = tweetBlob.word_counts[word.lower()]

    #create the word cloud
    #this is the word cloud variable
wordCloud = WordCloud().generate_from_frequencies(filteredDictionary)
plt.imshow(wordCloud, interpolation= 'bilinear')
plt.axis ("off")
#this shows our word cloud
plt.show()
