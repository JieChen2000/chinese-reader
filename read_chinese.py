import random
import argparse
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
    for i, val in enumerate(words_set):
        print('word ', i, ':', val)   
        user_input = input()
        # print(user_input)
        if user_input == 'n':
            words_set_not_command.add(val)
    print("Great job, you've commanded ",len(words_set)-len(words_set_not_command), " words out of total ", len(words_set), " or ", 100-len(words_set_not_command)*100./len(words_set), "% completed!")        
    print("Here're the words you need work more on\n", words_set_not_command)
    print("Do you like to save these words to a new words_libaray file? [y/N]:")
    user_input = input()
    if user_input == 'y' or user_input == 'Y':
        text_file = open("input_not_commanded.txt", "w")
        text_file.write(''.join(words_set_not_command))
        print("Commanded words saved to ", text_file.name)
        text_file.close()