"""
Processes all text files in a specified folder to
clean all of the extra gunk Moodle adds to exported
GIFT format exam questions
"""

import os
import re
import time

#TODO: add an example file to the main directory

# I save my exam questions in a different folder which is ignored by Git.
# If you want, you can do the same, or you can comment out the following
# line of code to search for text files in the same directory as removemoodleformatting.py
os.chdir(os.getcwd() + "/ExamQuestions")
# TODO: add ability to add CL arguments for directory


FILES = os.listdir(os.getcwd())

def filecleaning(dirtyfile):

    """Searches through the file using regex to find the gunk"""

    openedfile = open(dirtyfile)
    contents = openedfile.read()
    openedfile.close()

    categoryRegex = re.compile(r'\$.*\n')
    newcontents = categoryRegex.sub('', contents)

    titlesRegex = re.compile(r'\:\:.*\:\:')
    newcontents = titlesRegex.sub('', newcontents)

    moodleInfoRegex = re.compile(r'\/\/.*\n')
    newcontents = moodleInfoRegex.sub('', newcontents)

    htmlRegex = re.compile(r'<.*?>')
    newcontents = htmlRegex.sub('', newcontents)

    bracketRegex = re.compile(r'\[.*\]')
    newcontents = bracketRegex.sub('', newcontents)

    openedfile = open(dirtyfile.strip(".txt")+"_cleaned.txt", 'w')
    openedfile.write(newcontents)
    openedfile.close()

    openyesno = input("Would you like to open this cleaned file? (y/n)")
    if openyesno =="y":
        os.startfile(dirtyfile.strip(".txt")+"_cleaned.txt")

for file in FILES:
    if not file.endswith('.txt') or 'cleaned' in file:
        continue
    while True:
        yesno = input("Is "+file+" a GIFT-formatted text file you would like cleaned? (y/n)")
        if yesno == "y":
            print(" \nProcessing...\n")
            filecleaning(file)
            time.sleep(0.2)
            break
        elif yesno == "n":
            break
        else:
            print("Please enter either 'y' or 'n'")
            time.sleep(0.2)

print("Process Complete.")



