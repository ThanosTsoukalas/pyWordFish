from collections import defaultdict
import random
import string
import math

# just opening and reading the training data
trainingfile = open("training.txt")
training_text = trainingfile.read()
trainingfile.close()

count = defaultdict(dict)
ending = '~END~'

for c in string.punctuation:
    training_text = training_text.replace(c, '')

words = training_text.split()

for i, word in enumerate(words):
    if i == len(words) - 1:
        count[word][ending] = count[word].get(ending, 0) + 1
        break
    count[word][words[i + 1]] = count[word].get(words[i + 1], 0) + 1

def predictNextWord(prev:str, temp:float):
    random_range = 1 + temp * (len(count[prev]) - 1)
    wordlist = []
    for i in range(int(random_range)):
        max_freq = 0
        max_char = None
        for word in count[prev].keys():
            if word in wordlist:
                continue
            if count[prev][word] > max_freq:
                max_char = word
                max_freq = count[prev][word]
        wordlist.append(max_char)
        max_freq = 0
        max_char = None
    return random.choice(wordlist)

# make sentences
def predictNextWordCluster(prev:str, size:float, cluster_type:str, temp:float):
    # size is the rough number of words we want to predict

    # prev is the previous word cluster(s). For now, we only use the previous 
    # word cluster as context reference; we are too dumb to do it all at once

    # cluster_type defines the style of the sentence
    # "average"     - sentence contains 15 to 20 words
    # "short"       - sentence contains 12 to 15 words
    # "academic"    - sentence contains 20 to 25 words

    if cluster_type == "average":
        num_of_generated_words = int((random.randint(15, 20) * (size + 0.7))*(random.randint(100, 120)/100))
    elif cluster_type == "short":
        num_of_generated_words = int((random.randint(12, 15) * (size + 0.7))*(random.randint(100, 120)/100))
    elif cluster_type == "academic":
        num_of_generated_words = int((random.randint(20, 25) * (size + 0.7))*(random.randint(100, 120)/100))
    else:
        raise ValueError

    temp_string = prev.title() + ' '
    previous = prev
    for i in range(num_of_generated_words):
        curr = predictNextWord(previous, temp)
        temp_string = temp_string + curr.lower() + ' '
        previous = curr
        if i == num_of_generated_words - 1:
            temp_string = temp_string[:-1] + "."
    return temp_string

    


# make contextual paragraphs


# tie it all together!


# understand a prompt


# print(count)

for i in range(5):
    print(predictNextWordCluster('The', 0.75, 'average', 0.75))