# import sys
# import json
# import string
#
#
# def construct_dict(sentiment_score_file):
#     senti_file = open(sentiment_score_file)
#     scores = {}  # initialize an empty dictionary
#     for line in senti_file:
#         term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
#         scores[term] = int(score)  # Convert the score to an integer.
#     return scores
#
#
# def norm_word(word):
#     exclude = set(string.punctuation)
#     word = ''.join(str(ch) for ch in word.lower() if str(ch) not in exclude)
#     return word
#
#
# def get_senti(senti_dict, line):
#     senti_score = 0
#     for word in line.split(' '):
#         if word in senti_dict:
#             senti_score += senti_dict[word]
#     return senti_score
#
#
# def main():
#     senti_dict = construct_dict(sys.argv[1])
#     tweet_file = open(sys.argv[2])
#     for line in tweet_file:
#         d = json.loads(line)
#         if 'text' in d.keys():
#             norm_tweet = norm_word(d['text'])
#             print(get_senti(senti_dict, norm_tweet))
#
#
# if __name__ == '__main__':
#     main()
import string
import sys
import json


class JSON(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)

def lines(fp):
    print (str(len(fp.readlines())))

def calculator(text,dict):
    result = 0;
    list_of_words = text.split(' ')
    for word in list_of_words:
        if word in dict:
            result += dict[word]
    return result;

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
            print(calculator(good_tweet, scores))
        except:
            pass

if __name__ == '__main__':
    main()
