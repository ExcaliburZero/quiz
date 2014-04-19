"""
Question Generator Program
"""

#Imports
import json

#Set global question number
global question_number
question_number = 0

#Define function to get chapter questions
def get_chapter_questions(chapter):
    global info
    info = json.load(open("Questions/Chapter " + chapter + ".txt"))

#Define function for creating a question
def make_question(chapter, author, question_number):
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

    #Store question as a list
    my_question = [author, question, choice1, choice2, choice3, choice4, answer]

    #Confirm that entered info is correct
    finished = input("Is this info correct? (y/n)")
    if finished == "y":

        #Add question to question database
        if question_number == 0:
            question_number = info["question_count"] + 1
        else:
            question_number = question_number + 1

        #Put question into dictionary
        info[question_number] = my_question

        #Set question_count to new value
        info["question_count"] = question_number

        #Check to see if user wants to add more questions to chapter
        nt_done = input("Would you like to make any other questions for this chapter? (y/n)")
        if nt_done == "y":
            #Make new question
            make_question(chapter, author, question_number)
        else:
            #Write to chapter file
            json.dump(info, open("Questions/Chapter " + chapter + ".txt",'w'))
    else:
        #Re-do question
        make_question(chapter, author, question_number)
    
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
make_question(chapter, author, question_number)
