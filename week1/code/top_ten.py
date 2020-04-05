import string
import sys
import json
import operator


class JSON(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


def upd_dict(h_tags, h_dict):
    for hashtag in h_tags:
        if hashtag in h_dict:
            h_dict[hashtag] += 1
        else:
            h_dict[hashtag] = 1


def correct_tweet(word):
    exclude = set(string.punctuation)
    word = ''.join(str(ch) for ch in word.lower() if str(ch) not in exclude)
    return word


def main():
    tweet_file = open(sys.argv[1])
    dict = {}  # initialize an empty dictionary
    for line in tweet_file:
        tweet = JSON(line.encode('utf-8'))
        try:
            hashtags = (tweet.entities)['hashtags']
            h_tags = []
            for tags in hashtags:
                h_tags.append(correct_tweet(tags['text']))
            upd_dict(h_tags, dict)
        except:
            pass

    dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(10):
        print(dict[i][0] + ' ' +str(dict[i][1]))


if __name__ == '__main__':
    main()
