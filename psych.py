#!/bin/usr/env python

"""
A simple 'personality test'.
"""

import time

def main():
    notes = open('psychnotes.txt','r+')
    notes.read()
    print "Please answer all the following questions as honestly as possible."
    raw_input("Press enter to begin.")
    
    print "What is your first name?"
    asknote(notes)
    print "What is your date of birth?"
    asknote(notes)
    print "What is your favorite color?"
    asknote(notes)
    print "If you could change your first name, what would it be?"
    asknote(notes)
    print "What is your favorite animal?"
    asknote(notes)
    print "What adjective do you think would describe you the best?"
    asknote(notes)
    print "What do you think is your best trait? Please be specific."
    asknote(notes)
    print "In school, what subject do you get the best grades in?"
    asknote(notes)
    print "What subject do you get the worst grades in?"
    asknote(notes)
    print "What is your favorite genre of music?"
    asknote(notes)
    print "Finally, in one sentence, how do you think other people see you?"
    asknote(notes)
    notes.close()

    raw_input("Questionnaire finished. Press enter to display your results.")
    time.sleep(1.0)
    print "Compiling traits..."
    time.sleep(2.0)
    print "Assembling chains..."
    time.sleep(2.0)
    print "Creating archetypes..."
    time.sleep(2.0)
    print "Constructing backgrounds..."
    time.sleep(2.0)
    print "Refactoring..."
    time.sleep(2.0)
    print "Eliminating duds..."
    time.sleep(2.0)
    print "Finalizing..."
    time.sleep(5.0)
    raw_input("Finished! Press enter to view your results.\n\n")

    print "\tYou have a need for other people to like and admire you, and yet you tend to be critical of yourself. While you have some personality weaknesses, you are generally able to compensate for them. You have considerable unused capacity that you have not turned to your advantage. Disciplined and self-controlled on the outside, you tend to be worrisome and insecure on the inside. At times you have serious doubts as to whether you have made the right decision or done the right thing. You prefer a certain amount of change and variety and become dissatisfied when hemmed in by restrictions and limitations. You also pride yourself as an independent thinker and do not accept others' statements without satisfactory proof. But you have found it unwise to be too frank in revealing yourself to others. At times you are extroverted, affable, and sociable, while at other times you are introverted, wary, and reserved. Some of your aspirations tend to be rather unrealistic." 
    print "\n\n"

    print "Please do not share your results with others. Knowledge of the test may compromise others' results!" 

def asknote(note):
    n = raw_input("> ")
    note.write(n + "\t")

if __name__ == '__main__':
    main()
