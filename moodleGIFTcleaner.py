"""
moodleGIFTcleaner.py
Processes all text files in a specified folder to
clean all of the extra gunk Moodle adds to exported
GIFT format exam questions. Needs to be run in the same
folder as the files you want processed.
"""

import os
import re
import time
import argparse

# TODO: add ability to add CL arguments for directory
# TODO: add parsing of individual questions before cleaning

def file_cleaning(dirty_file):
    """Searches through the file using regex to find the gunk"""

    opened_file = open(dirty_file, encoding="utf-8")
    contents = opened_file.read()
    opened_file.close()

    category_regex = re.compile(r'\$.*\n')
    new_contents = category_regex.sub('', contents)

    titles_regex = re.compile(r'\:\:.*\:\:')
    #new_contents = titles_regex.sub('::question::\n', new_contents) # add in generic question name for Schoolhouse Test
    new_contents = titles_regex.sub('', new_contents) # remove question titles

    moodle_info_regex = re.compile(r'\/\/.*\n')
    new_contents = moodle_info_regex.sub('', new_contents)

    brace_regex = re.compile(r'(.)\{')
    new_contents = brace_regex.sub(r'\1\n{', new_contents)

    html_regex = re.compile(r'<.*?>')
    new_contents = html_regex.sub('', new_contents)

    bracket_regex = re.compile(r'\[.*\]')
    new_contents = bracket_regex.sub('', new_contents)

    opened_file = open(dirty_file.strip(".txt")+"_cleaned.txt", 'w')
    opened_file.write(new_contents)
    opened_file.close()

    open_yes_no = input("Would you like to open this cleaned file? (y/n)")
    if open_yes_no == "y":
        os.startfile(dirty_file.strip(".txt")+"_cleaned.txt")



FILES = os.listdir(os.getcwd())


for file in FILES:
    if not file.endswith('.txt') or 'cleaned' in file:
        continue
    while True:
        yesno = input(
            "Is "+file+" a GIFT-formatted text file you would like cleaned? (y/n)")
        if yesno == "y":
            print(" \nProcessing...\n")
            file_cleaning(file)
            time.sleep(0.2)
            break
        elif yesno == "n":
            break
        else:
            print("Please enter either 'y' or 'n'")
            time.sleep(0.2)

print("Process Complete.")
