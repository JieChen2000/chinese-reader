import random
import argparse
import os
from datetime import datetime 
if __name__ == '__main__':
    """
    Randomly display a word(from arg words_lib_name file) to check if student knows it. 
    Put the unknown words to a optional file "input_not_commanded.txt" if user requests.
    """
    # Parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--words_lib_name',
        help='word libaray name',
        required=False,
        default='input.txt'
    )
    args = parser.parse_args()
    arguments = args.__dict__    
    input_file_name = arguments['words_lib_name']
    f = open(input_file_name)
    words = f.read().rstrip()
    f.close()
    words = words.replace('\n','')
    words_shuffle = ''.join(random.sample(words, len(words)))
    words_set = set(words_shuffle) # set make it unique
    words_set_not_command = set()
    print("We have ", len(words_set), " words learned, let's review them one by one, enter n if you don't know it")
    text_file = open("input_not_commanded.txt", "a")

    for i, val in enumerate(words_set):
        print('word ', i, '/', len(words_set), ':', val)   
        user_input = input()
        # print(user_input)
        if user_input == 'n':
            words_set_not_command.add(val)
            text_file.write(val)

    print("Great job, you've commanded ",len(words_set)-len(words_set_not_command), " words out of total ", len(words_set), " or ", 100-len(words_set_not_command)*100./len(words_set), "% completed!")        
    print("Here're the words you need work more on\n", words_set_not_command)
    print("You only need work on these ", len(words_set_not_command), " words next time, Congratulations!")
    text_file.close()
    now = datetime.now()
    dest_file_name = 'data/input_'+now.strftime("%m%d%Y_%H%M%S")+'.txt'
    if not os.path.isdir('data'):
        os.system('mkdir data')

    os.rename('input.txt', dest_file_name)
    os.rename('input_not_commanded.txt', 'input.txt')