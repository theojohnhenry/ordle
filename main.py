# process massive file
# read from massive file with all 5 letter words [x]
# randomize a word [x]
# take input [x]
# create functions to determine if letter is in word. and if letter is in right place.
# control flow [x]
# count guesses [x]
#
#
# optional - 
# make a gui 
# leaderboard
# make it a website
# system som gör så att det inte blir samma ord flera gånger på en månad
# available word system
# byt till kellylistan och formattera / dra en chatgpt prompt

import json
import random
import os

# --- COLORS ---
CGREEN = '\033[42m'
CYELLOW = '\033[43m'
CGREY = '\033[100m'
CEND = '\033[0m'

# ---    SETTINGS ---

TRIES = 6
WORDLENGTH = 5
with open("json/sample.json", "r") as f:
    DATA = json.load(f)
AVAILABLE = "abcdefghijklmnopqrstuvwxyzåäö"

# --- Functions ---

def getWotd():
        randint = random.randint(0, len(DATA)-1)
        wotd = DATA[randint]
        return wotd

def getValidGuess():
    while True:
        guess = input("Gissning: ").lower()
        if any(chr.isdigit() for chr in guess):
            print("Gissningen får inte innehålla siffror")
            continue
        if len(guess) != WORDLENGTH:
            print(f"Gissningen måste vara {WORDLENGTH} bokstäver.")
            continue
        if guess not in DATA:
            print(f"Gissningen är inte ett riktigt ord.")
            continue
        else:
            break
    return guess

def verifyWord(guess, wotd):
    colors = ["NaN", "NaN", "NaN", "NaN", "NaN"]
    global AVAILABLE
    for i, c in enumerate(guess):
        if c == wotd[i]:
            colors[i] = CGREEN
            continue
        if c in wotd and (c != wotd[i]):
            colors[i] = CYELLOW
            continue
        if c not in wotd:
            colors[i] = CGREY
            AVAILABLE = AVAILABLE.replace(c,' ')
    
    if all(status == CGREEN for status in colors):
        return "won", (f"{colors[0]}{guess[0]}{CEND}{colors[1]}{guess[1]}{CEND}{colors[2]}{guess[2]}{CEND}{colors[3]}{guess[3]}{CEND}{colors[4]}{guess[4]}{CEND}")
    else:
        return "ongoing", (f"{colors[0]}{guess[0]}{CEND}{colors[1]}{guess[1]}{CEND}{colors[2]}{guess[2]}{CEND}{colors[3]}{guess[3]}{CEND}{colors[4]}{guess[4]}{CEND}")


#  --- Main ---

def main():
    wotd = getWotd()
    tries = TRIES
    rowList = []
    global AVAILABLE
    print(f"word of the day is \"{wotd}\"")

    game = "ongoing"

    while game == "ongoing":
        if tries > 0:
            guess = getValidGuess()
            os.system('clear')
            game, row = verifyWord(guess, wotd)
            rowList.append(row)
            for row in rowList:
                print(row)
            print(f"gissningar kvar: {tries}")
            print(AVAILABLE)
            tries = tries - 1
        else:
            game == "lost"

    if game == "won":
        print("you won!, thanks for playing")
    if game == "lost":
        print("you lost!, thanks for playing")
main()
