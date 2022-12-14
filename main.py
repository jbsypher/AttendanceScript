import pytesseract
import pyautogui
from cv2 import cv2
import time
from pynput import keyboard
import datetime
from tkinter import *
import os

directory = os.getcwd()
os.chdir(os.getcwd() + "\\Participants")
for x in os.listdir(os.getcwd()):
    os.remove(x)
os.chdir(directory)    

def on_release(key):
    if key == keyboard.Key.enter:
        l.stop()

pytesseract.pytesseract.tesseract_cmd = os.getcwd() + "\\Tesseract-OCR\\tesseract.exe"

studentText = ""
text = ""
print("Copyright 2021, Toph Dorry, All rights reserved.")
print("Press enter once you have zoom open. (This program does not have to be on the display to detect the keypress)")
# Waits for enter to be pressed
with keyboard.Listener(on_release=on_release) as l:
    l.join()

# Starts screenshots
import screenshots

# Checks the class period

while True:
    try:
        print()
        period = int(input("What class period? (1-8) "))
        break
    except:
        print("Enter one number")

# Loop through images in Folder
directory = os.getcwd()
os.chdir(os.getcwd() + "\\Participants")
for x in os.listdir(os.getcwd()):
    if x.endswith("png"):
        img = cv2.imread(x)
        text = text + " " + pytesseract.image_to_string(img)
os.chdir(directory)
# Creates class 
directory = os.getcwd()
if period == 1:
    os.chdir(directory+r"\Classes")
    studentText = open('1.txt', 'r').read()
    os.chdir(directory)
if period == 2:
    os.chdir(directory+r"\Classes")
    studentText = open('2.txt', 'r').read()
    os.chdir(directory)
if period == 3:
    os.chdir(directory+r"\Classes")
    studentText = open('3.txt', 'r').read()
    os.chdir(directory)
if period == 4:
    os.chdir(directory+r"\Classes")
    studentText = open('4.txt', 'r').read()
    os.chdir(directory)
if period == 5:
    os.chdir(directory+r"\Classes")
    studentText = open('5.txt', 'r').read()
    os.chdir(directory)
if period == 6:
    os.chdir(directory+r"\Classes")
    studentText = open('6.txt', 'r').read()
    os.chdir(directory)
if period == 7:
    os.chdir(directory+r"\Classes")
    studentText = open('7.txt', 'r').read()
    os.chdir(directory)
if period == 8:
    os.chdir(directory+r"\Classes")
    studentText = open('8.txt', 'r').read()
    os.chdir(directory)
# Processes zoom and class
studentText = studentText.lower()
text = text.lower()
studentText = " ".join(studentText.split())
studentList = studentText.split()
textList = text.split()
#Make studentText into list with 2 names per item
for x in textList:
    if(x == "(guest)" or x == "(host, me)" or x == "(me)" or x == "(host)"):
        textList.remove(x)

i = 0
#compares students in the zoom call with total students
for x in textList:
    if(i%2==1):
        if(x in studentList):
            index = studentList.index(x)
            if index:
                studentList.pop(index)
                studentList.pop(index-1)
    i+=1

print("Students not found in zoom:")

if(len(studentList)) > 0:
    print(" ".join(studentList))
else:
    print("No students missing from zoom")
print("\n \n")
if len(studentList) > 0:
    print("Enter students last names to remove them from the list")
    while True:
        name = input("Enter a student's last name to remove them: ")
        for x in name.split():
            if(x in studentList):
                index = studentList.index(x)
                if index:
                    studentList.pop(index)
                    studentList.pop(index-1)
        print(" ".join(studentList))
        if len(studentList) == 0:
            print("No students missing from zoom")
            break

input("Press enter to exit")