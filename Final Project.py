#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:24:19 2023

@author: diadana
SMALL TEXT ONLY
citation:
    1. https://www.nltk.org/install.html
    2. https://www.w3schools.com/python/matplotlib_pie_charts.asp
    3. https://www.tutorialspoint.com/how-can-i-put-two-buttons-next-to-each-other-in-tkinter
    4. https://www.geeksforgeeks.org/how-to-place-a-button-at-any-position-in-tkinter/
    5. https://www.geeksforgeeks.org/how-to-pass-arguments-to-tkinter-button-command/
    6. https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/
"""
import string

#Natural Language Toolkit (NLTK)
from nltk.corpus import stopwords #cite1

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np #cite 3

import tkinter
from functools import partial
from tkinter import ttk
from tkinter import filedialog


def extractingfile(fileName):
    """Extracts the text from file
    Parameter: fileName, name of the file
    return: the text of the file
    """
    try:
        assert fileName.endswith('txt') or fileName.endswith('csv') or fileName.endswith('json')
    except:
        AssertionError, 'Please provide a valid File type: json, csv or txt'
    if fileName != '':
        file = open(fileName,'r')
        text = file.read()
        file.close()
    else:
        return 'Please Select a File'
    return text

def removingPunctuation(fileName):
    """removes Punctuation from the text
    Parameter: fileName, name of the file
    return: the new text without punctuations
    """
    newText = ''
    text = extractingfile(fileName)
    for character in text:
        if character not in string.punctuation and character != "‘" and character != "’":
            newText = newText + character
    return newText

def lowerCaseListing(fileName):
    """lowers cases for all words
    Parameter: fileName, name of the file
    return: the new list without punctuation, lower case, text split into words
    """
    newText = []
    text = removingPunctuation(fileName)
    text = text.split(' ')
    for word in text:
        split = word.split(' ')
        for lines in split:
            newText.extend(lines.split('\n'))
    newText = [word.lower() for word in newText if word != '']
    return newText

def removeStopWords(fileName):
    """removing stop words from list
    Parameter: fileName, name of the file
    return: the list without stop words
    """
    text = lowerCaseListing(fileName)
    finalText = []
    stopWords = stopwords.words('english')
    for word in text:
        if word not in stopWords:
            finalText.append(word)
    return finalText

def normalizeText(fileName):
    """Normalizing the text
    Parameter: fileName, name of the file
    return: final text with no punctuation, stop words and lower case 
    """
    finalText = removeStopWords(fileName)
    return finalText
    
def countingSimilarity(text1,text2):
    """compares words of the two texts and counts the similarity 
    Parameter: text1, list of words of text 1
               text2, list of words of text 2
    return: the percentage of similar words between text 1 and text 2
    """
    similarityCount = 0 
    matched_words = set()
    for word1 in text1:
        for word2 in text2:
            if word1 == word2 and word1 != '' and word2 != '' and (word1, word2) not in matched_words:
                print(word1,word2)
                matched_words.add((word1, word2))
                similarityCount = similarityCount + 1
    print(similarityCount,'simi')
    return similarityCount

def totalWords(text1,text2):
    """calculates the number of words in the list
    Parameter: text1, list of words of text 1
               text2, list of words of text 2
    return: the number of words of the longer text
    """
    words = max(len(text1),len(text2))
    print(words,'words')
    return words


def percentage():
    """Calculates the similarity
    Parameter: None
    return: the percentage of similarity
    """
    percentage = (countingSimilarity(text1,text2)/totalWords(text1,text2)) * 100
    percentage = round(percentage)
    return percentage


def Screenlabel():
    """the title of the screen
    Parameter: fileName, name of the file
    return: final text with no punctuation, stop words and lower case 
    """
    label = ttk.Label(screen, text = 'Files Similarities Percentage', foreground = 'purple', font = ('Arial',20))
    label.pack()
    label.place(x=120,y=10) #cite 4

def File1():
    """GUI screen file buttom
    parameter: path, the uploading_files function used to allow the user to insert the file. In other words, activate the bottons 
    return: the file buttom with the inserted file
    """
    file1 = ttk.Button(screen, text= 'Text 1', style="big.TButton", command = partial(insertFile)) #cite 3, cite 4, cite 5
    file1.pack(ipadx = 70,ipady = 120)
    file1.place(x=100,y=40) #cite 4
    return file1['command']

def File2():
    """GUI screen file buttom
    parameter: path, the uploading_files function used to allow the user to insert the file. In other words, activate the bottons 
    return: the file buttom with the inserted file
    """
    file2 = ttk.Button(screen, text= 'Text 2', style="big.TButton", command = partial(insertFile)) #cite 3, cite 4, cite 5
    file2.pack(ipadx = 70,ipady = 120)
    file2.place(x=300,y=40) #cite 4
    return file2['command']

def insertFile():
    files = filedialog.askopenfilename(title = 'Select a  File')
    return(files)


def get_fileName(filePath):
    """Extracts the file's name from the file's path
    parameter: filePath, the path of the file
    Return: the file's name
    """
    pathList = filePath.split('/')
    fileName = pathList[-1]
    return fileName

def screenPercentage(result):
    """Displaying the percentage on screen
    Parameter: result, the percentage integer
    return: None
    """
    result = ttk.Label(screen, text = result, foreground = 'red', font = ('Arial',20))
    result.pack()
    result.place(x=130,y=100)

def screenGraph(): #cite 6
    """displays the pie graph
    Parameter: None
    return: None
    """
    content = np.array([percentage(), 100 - percentage()])
    mylabels = ['Similar', 'Difference']
    fig, ax = plt.subplots()
    ax.pie(content, labels=mylabels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    canvas = FigureCanvasTkAgg(fig, master=screen)
    canvas.draw()
    canvas.get_tk_widget().pack()
    canvas.get_tk_widget().place(x=100, y=250)

if __name__ == "__main__":
    #GUI
    #setting the screen
    screen = tkinter.Tk()
    screen.geometry('500x750') #cite 3
    screen.title('text Similarite Calculator')
    Screenlabel()
    
    #calling buttons
    file2buttom = File1()
    file2buttom = File2()
    
    #extracting file name
    fileName1 = get_fileName(insertFile())
    fileName2 = get_fileName(insertFile())
    
    #normalizing the texts
    text1 = normalizeText(fileName1)
    text2 = normalizeText(fileName2)
    
    #the results
    result = f'the files are {percentage()}% similar'
    screenPercentage(result)
    
    #the graph
    screenGraph()
    
    screen.mainloop()
