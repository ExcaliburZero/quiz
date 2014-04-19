"""
Quiz Generator Program
"""

#Imports
import json
from random import *

#Define function to get chapter questions
def get_chapter_questions(chapter):
    global info
    info = json.load(open("Questions/Chapter " + chapter + ".txt"))

#Define function to get question
def get_question(chapter, answered_questions, question_count, info):
    random_question = randint(1,question_count)
    while random_question in answered_questions:
        random_question = randint(1,question_count)

    #Grab and print question
    current_question = info[str(random_question)]
    print(str(random_question) + ") " + current_question[1])
    print("1. " + current_question[2])
    print("2. " + current_question[3])
    print("3. " + current_question[4])
    print("4. " + current_question[5])
    print("----------------")
    answer = input("What is the answer? (1, 2, 3, or 4)")
    print("----------------")
    if answer == current_question[6]:
        print("Correct!")
    else:
        print("Incorrect! The correct answer is " + current_question[6] + ".")
    print("----------------")
    answered_questions.append(random_question)
    return answered_questions

#Print intro
print("-----------------------------------")
print("Welcome to the Quiz generator!")
print("-----------------------------------")

#Gather chapter number
chapter = input("What chapter would you like questions from?")
print("----------------")

#Gather chapter questions
get_chapter_questions(chapter)

#Get number of questions in chapter
question_count = int(info["question_count"])

#Print our number of questions in chapter
print("There are " + str(question_count) + " questions in Chapter " + chapter + ".")
selected_num_questions = int(input("How many questions would you like?"))
i = selected_num_questions
print("----------------")

#Make sure number of questions requested isn't greater than number availible
while selected_num_questions > question_count:
    print("There aren't that many questions avalible in  the selected chapter")
    print("There are " + str(question_count) + " questions in Chapter " + chapter + ".")
    selected_num_questions = input("How many questions would you like?")
    print("----------------")

#Set up answered questions list
answered_questions = []

#Get questions
while i > 0:
    get_question(chapter, answered_questions, question_count, info)
    i = i - 1
