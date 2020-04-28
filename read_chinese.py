import random
f = open('input.txt')
words = f.read().rstrip()
words = words.replace('\n','')
words_shuffle = ''.join(random.sample(words, len(words)))
words_set = set(words_shuffle) # set make it unique
words_set_not_command = set()
print("We have ", len(words_set), " words learned, let's review them one by one, enter n if you don't know it")
for val in words_set:
    print(val)   
    user_input = input()
    # print(user_input)
    if user_input == 'n':
        words_set_not_command.add(val)
print("Here're the words you need work more on\n", words_set_not_command)