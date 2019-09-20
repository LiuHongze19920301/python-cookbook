# example.py
#
# Determine the most common words in a list
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
# outputs [('eyes', 8), ('the', 5), ('look', 4)]
print(top_three)
top_three_map = {key: val for key, val in top_three}
print(top_three_map)

# Example of merging in more words

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts.update(morewords)
new_word_count = word_counts.most_common(3)
print(new_word_count)
new_word_count_map = {key: val for key, val in new_word_count}
print(new_word_count_map)


all_count_map = {key: val for key, val in word_counts.items()}
print(all_count_map)

