import string
import sys
import json


class JSON(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


def fill_a_dict(words, dic):
    list_of_words = words.split(' ')
    for word in list_of_words:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    return dic


def calculator(text, dict):
    result = 0
    list_of_words = text.split(' ')
    for word in list_of_words:
        if word in dict:
            result += dict[word]

    return result


def correct_tweet(word):
    exclude = set(string.punctuation)
    word = ''.join(str(ch) for ch in word.lower() if str(ch) not in exclude)
    return word


def main():
    tweet_file = open(sys.argv[1])
    my_dict = {}  # initialize an empty dictionary
    for line in tweet_file:
        tweet = JSON(line.encode('utf-8'))
        try:
            good_tweet = correct_tweet(tweet.text)
            my_dict = fill_a_dict(good_tweet, my_dict)
        except:
            pass

    all_val = sum(my_dict.values())

    for x in my_dict:
        print(str(x.strip().encode('utf-8')) + ' ' + str(float(my_dict[x] / float(all_val))))


if __name__ == '__main__':
    main()
