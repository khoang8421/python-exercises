#Project 9 — Simple Text-Based Sentiment Predictor
#Topics tested: strings, dictionaries, loops, conditionals

#Prompt:
#Write a function sentiment_analysis(text) that:

#Counts positive and negative words from predefined lists:

#positive = ["good", "happy", "great", "excellent", "love", "like"]
#negative = ["bad", "sad", "terrible", "hate", "dislike", "awful"]

#Return dictionary:

#{
#  "positive_count": int,
#  "negative_count": int,
# "overall_sentiment": "Positive"/"Negative"/"Neutral"
#}

#Constraints / Skills Practiced:
#Loops, string handling, dicts
#Ignore punctuation / handle case-insensitive comparison
#Handle empty strings logically

#Extra Challenge:
#Return the top 2 most frequent positive or negative words

import string as st

positive = ["good", "happy", "great", "excellent", "love", "like"]
negative = ["bad", "sad", "terrible", "hate", "dislike", "awful"]

def sentiment_analysis(text) -> dict:
    if text == "":
        return {
    "positive_count": 0,
    "negative_count": 0, 
    "overall_sentiment": "Neutral"
        }
    else:
        words = text.split()
        i = 0
        while i < len(words):
            words[i] = words[i].lower()
            words[i] = words[i].translate(str.maketrans('', '', st.punctuation))
            i += 1
      
        positive_count: int = 0
        for word in words:
            if word in positive:
                positive_count += 1

        negative_count: int = 0
        for word in words:
            if word in negative:
                negative_count += 1
            
        
        def deciding_sentiment(p, n):
            if p > n:
                return "Positive"
            if p < n:
                return "Negative"
            else:
                return "Neutral"

        return {

        "positive_count": positive_count,
        "negative_count": negative_count, 
        "overall_sentiment": deciding_sentiment(positive_count, negative_count)

        }

def main():
    print(sentiment_analysis('I love this product, it is excellent and great'))
    print(sentiment_analysis('This is a bad and terrible experience. I hate hate hate it'))
    print(sentiment_analysis('I like the design but hate the performance'))
    print(sentiment_analysis(""))

if __name__ == '__main__':
    main()

#12/26/2025 Grade 99/100