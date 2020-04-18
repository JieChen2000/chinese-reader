import random
f = open('input.txt')
words = f.read().rstrip()
words = words.replace('\n','')
words_shuffle = ''.join(random.sample(words, len(words)))
print(set(words_shuffle))   # set make it unique