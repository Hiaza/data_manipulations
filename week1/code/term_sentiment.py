import string
import sys
import json


class JSON(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


def lines(fp):
    print(str(len(fp.readlines())))


def calculator(text, dict):
    result = 0;
    non_senti_words = []
    list_of_words = text.split(' ')
    for word in list_of_words:
        if word in dict:
            result += dict[word]
        else:
            non_senti_words.append(word)
    return result, non_senti_words;


def correct_tweet(word):
    exclude = set(string.punctuation)
    word = ''.join(str(ch) for ch in word.lower() if str(ch) not in exclude)
    return word


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        tweet = JSON(line.encode('utf-8'))
        try:
            good_tweet = correct_tweet(tweet.text)
            calc, words = calculator(good_tweet, scores)
            for w in words:
                print(w + ' ' + str(calc / float(len(good_tweet) - len(words))))
        except:
            pass


if __name__ == '__main__':
    main()
