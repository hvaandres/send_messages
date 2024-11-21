import os
import config

"""
We understand that Spamming people is wrong but if you would like to do this for fun, you will have to test it with your own telephone number.
At this point, I'm not responsible for the bad usage of this script!

"""


def get_words(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()[0]
        words = text.split()
    return words

def get_lines(file_path):
    with open(file_path, 'r') as f:
        text = f.readlines()
    return text

def send_message(phone_number, message):
    os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

if __name__ == '__main__':
    #words = get_words('ly.txt')
    #for word in words:
        #send_message('[INSERT_TELEPHONE_NUMBER]', word)


    text = get_lines('ly.txt')
    for line in text:
        send_message('insert_phone_number', line)
