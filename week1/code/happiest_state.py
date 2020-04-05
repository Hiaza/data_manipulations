import string
import sys
import json


class JSON(object):
    def __init__(self, data):
        self.__dict__ = json.loads(data)


def geo_info(tweet):
    try:
        place = tweet.place
        if place['country_code'] == 'US':
            state = place['full_name'][-2:]
            return True, state
    except:
        pass
    return False, ''


def correct_tweet(word):
    exclude = set(string.punctuation)
    word = ''.join(str(ch) for ch in word.lower() if str(ch) not in exclude)

    return word


def calculator(text, dict):
    result = 0
    list_of_words = text.split(' ')
    for word in list_of_words:
        if word in dict:
            result += dict[word]
    return result


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}

    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    state_happy_index = {}
    total_tweet_count = 0

    for line in tweet_file:
        tweet = JSON(line.encode('utf-8'))
        try:
            if tweet.lang == 'en':

                good_tweet = correct_tweet(tweet.text)
                is_US, state = geo_info(tweet)
                if is_US:
                    total_tweet_count += 1
                    senti_score = calculator(good_tweet, scores)
                    if state in state_happy_index:
                        state_happy_index[state] += senti_score
                    else:
                        state_happy_index[state] = senti_score
        except:
            pass

    happiest_state = 'XX'
    happy_score = -1

    for state, score in state_happy_index.items():
        if score > happy_score:
            happy_score = score
            happiest_state = state

    print(happiest_state)


if __name__ == '__main__':
    main()
