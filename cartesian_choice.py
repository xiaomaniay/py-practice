import random
import numpy as np


def find_interval(x, partition):
    """
    find_interval finds the index where partition[index] < x < partition[index + 1]
    """
    for i in range(len(partition)):
        if x < partition[i]:
            return i - 1
    return -1


def weighted_choice(sequence, weights, secure=True):
    """
    weighted_choice selects a random element of the sequence according to
    the list of weights
    """
    if secure:
        crypto = random.SystemRandom()
        x = crypto.random()
    else:
        x = np.random.random()
    cum_weights = [0] + list(np.cumsum(weights))
    index = find_interval(x, cum_weights)
    return sequence[index]


def weighted_cartesian_choice(*iterables):
    """
    A list with weighted random choices from each iterable of iterables
    is being created in respective order
    """
    res = []
    for population, weight in iterables:
        lst = weighted_choice(population, weight)
        res.append(lst)
    return res


determiners = (["The", "A", "Each", "Every", "No"],
               [0.3, 0.3, 0.1, 0.1, 0.2])
colours = (["red", "green", "blue", "yellow", "grey"],
           [0.1, 0.3, 0.3, 0.2, 0.2])
nouns = (["water", "elephant", "fish", "light", "programming language"],
         [0.3, 0.2, 0.1, 0.1, 0.3])
nouns2 = (["of happiness", "of chocolate", "of wisdom", "of challenges", "of air"],
         [0.5, 0.2, 0.1, 0.1, 0.1])
verb_phrases = (["smells", "dreams", "thinks", "is made of"],
         [0.4, 0.3, 0.2, 0.1])


print("It may or may not be true: ")
sentences = []
for i in range(10000):
    res = weighted_cartesian_choice(determiners, colours, nouns, verb_phrases, nouns2)
    sentences.append(" ".join(res) + ".")
words = ["smells", "dreams", "thinks", "is made of"]


from collections import Counter


c = Counter()
for sentence in sentences:
    for word in words:
        if word in sentence:
            c[word] += 1
wsum = sum(c.values())

for key in c:
    print(key, c[key] / wsum)
