# !usr/bin/python
# Author: Kevin McCormack
# Description: Script to determine all possible words and point values given scrabble tiles


from bs4 import BeautifulSoup
import urllib3

# Read Scrabble dictionary from Github

def read_file():
    http = urllib3.PoolManager()
    url = 'https://raw.githubusercontent.com/jonbcard/scrabble-bot/master/src/dictionary.txt'
    response = http.request('GET', url)
    data = BeautifulSoup(response.data, features="html.parser")
    master_data = str(data)
    filename = "smalldictionary.txt"
    outfile = open(filename, "w")
    outfile.write(master_data)
    outfile.close()

#Sort user input into alphabetical order for easy comparison

def letter_sorted_string(string): 
    word = list(string)
    word.sort()
    word = ''.join(word)
    word = word.lower()
    return word


#Calculate point total for each possible word, returns dictionary of word:point totals

def point_total(results):
    letters = {"a":1, "b":3, "c":3, "d":2, "e":1, "f":4, "g":2, "h":4, "i":1, "j":8,
               "k":5, "l":1, "m":3, "n":1, "o":1, "p":3, "q":10, "r":1, "s":1, "t":1,
               "u":1, "v":4, "w":4, "x":8, "y":4, "z":10, "blank":0}
    my_dict = {}
    points = 0
    for x in results:
        for i in range(len(x)):
            points += letters.get(x[i].lower())
        my_dict[x] = points
        points = 0
    return my_dict


#Open and read text file CHANGE FOR SIMPLICITY, returns two lists, one of sorted terms

def read_file():
    filename="smalldictionary.txt"
    originals = []
    anagrams = []
    outfile = open(filename, "r")
    line = outfile.readline()
    while line != '':
        line = line.strip('\n')
        originals.append(line)
        line_a = ''.join(sorted(line))
        anagrams.append(line_a.lower())
        line = outfile.readline()
    outfile.close()
    return (originals, anagrams)


#Compares the sorted list to the term and adds the sorted word to a list of possibiles.

def compare(list1, list2, word):
    results = []
    for i in range(len(list2)):
        if list2[i] in word:
            match = list1[i]
            results.append(match.lower())
    return results


# Main script

def main():
    choice = 0
    while choice != '':
        string = input("Enter your tiles here for Scrabble Combinations: ")
        word = letter_sorted_string(string)
        (originals, anagrams) = read_file()
        results = compare(originals, anagrams, word)
        results.sort(key=len)
        print(point_total(results))
        choice = input("\nPress any key to check for more Anagrams! If you'd like to quit press enter: ")

read_file()
main()
