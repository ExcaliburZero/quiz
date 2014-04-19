"""
Chapter Generator Program
"""

#Imports
import json

#Print intro
print("-----------------------------------")
print("Welcome to the Chapter generator!")
print("-----------------------------------")

#Gather chapter number
chapter = input("What chapter would you like to initialize?")
print("----------------")

#Ready chapter file
chapter_file_name = "Questions/Chapter " + chapter + ".txt"

#Open and Write to chapter file
info = {"question_count": 0}
json.dump(info, open(chapter_file_name,'w'))
