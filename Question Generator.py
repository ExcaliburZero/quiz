"""
Question Generator Program
"""

#Imports
import json

#Define function to get chapter questions
def get_chapter_questions(chapter):
    global info
    info = json.load(open("/Questions/Chapter " + chapter + ".txt"))

#Define function for creating a question
def make_question(chapter, author):
    question = input("What is the question?")
    print("----------------")
    choice1 = input("What is the first choice?")
    print("----------------")
    choice2 = input("What is the second choice?")
    print("----------------")
    choice3 = input("What is the third choice?")
    print("----------------")
    choice4 = input("What is the fourth choice?")
    print("----------------")
    answer = input("What is the correct answer? (1,2,3, or 4)")
    print("----------------")
    print(question)
    print("1. " + choice1)
    print("2. " + choice2)
    print("3. " + choice3)
    print("4. " + choice4)
    print("Answer: " + answer)
    print("----------------")

    #Confirm that entered info is correct
    finished = input("Is this info correct? (y/n)")
    if finished == "y":
        done = input("Would you like to make any other questions for this chapter? (y/n)")
        if done == "y":
            make_question(chapter, author)
        else:
            #Write to chapter file
            json.dump(info, open("/Questions/Chapter " + chapter + ".txt",'w'))
    else:
        make_question(chapter, author)
    
#Print intro
print("-----------------------------------")
print("Welcome to the Question generator!")
print("-----------------------------------")

#Gather author name
author = input("What is your name?")
print("----------------")

#Gather chapter number
chapter = input("What chapter would you like to make questions for?")
print("----------------")

#Get pre-existing chapter questions
get_chapter_questions(chapter)

#Make new question(s)
make_question(chapter, author)
