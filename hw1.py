"""
This file will take in a start word, a target word, and a dictionary.
It will find the shortest path from the start word to the target word,
where each intermediary only one letter is changed into a word in the dict.

Author: Ming Creekmore mec5765
Date 31 January 2023
"""

import sys

alphabet = set()
dictionary = set()

"""
Given a file, will determine the alphabet of the entire set
and will add each line into global set dictionary as a word in the dict
@param filename: file to read as a dictionary
"""
def makeDict(filename):
    file = open(filename, encoding="utf-8")
    global alphabet, dictionary

    #to get a set of all characters used
    alphabet = set(file.read())
    alphabet.discard("\n")
    file.seek(0)

    #to read in dictionary words
    line = file.readline()
    while line:
        dictionary.add(line.strip())
        line = file.readline()

    file.close()

"""
Given a word, will return a set of all successors, where a 
successor is a change in one letter in the word, making a 
new word that is in the dictionary
@param word: word to get successors of
@return set of all successors
"""
def getSuccessors(word):
    successors = set()
    for i in range(len(word)):
        for char in alphabet:
            if char != word[i]:
                newWord = word[:i] + char + word[i+1:]
                if newWord in dictionary:
                    successors.add(newWord)
    return successors

"""
Uses Breadth First Search, global dictionary, and global alphabet
to find a targeted word given a start word
@param start: the starting word
@param goal: the word to reach
"""
def BFS(start, goal):
    frontier = [start]
    successormap = {start: None}
    goalreached = False

    #searching for goal
    while(len(frontier) != 0):
        current = frontier.pop(0)
        if current == goal:
            goalreached = True
            break
        successors = getSuccessors(current)
        for succ in successors:
            if succ not in successormap:
                successormap[succ] = current
                frontier.append(succ)

    #makes a solution path if goal is reached
    if goalreached:
        path = [current]
        predecessor = successormap[current]
        while(predecessor != None):
            path.insert(0, predecessor)
            predecessor = successormap[predecessor]
        return path

    #if no solution
    return []

"""
Using the system arguments, will read a file as a dictionary
and use the dictionary to find the shortest path between
two given words, where one valid step is a change of one letter 
making a valid word in the dictionary
"""
def main():
    if(len(sys.argv) != 4):
        print("usage: hw1.py filename word1 word2")
    else:
        makeDict(sys.argv[1])
        sol = BFS(sys.argv[2], sys.argv[3])
        if(len(sol) == 0):
            print("No solution!")
        else:
            for word in sol:
                print(word)

if __name__ == '__main__':
    main()
