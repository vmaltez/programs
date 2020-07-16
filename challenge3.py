#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# %load /home/vivienm/Desktop/IAI8-master/IAI8.py
import random
import numpy as np

GREEK_SYMBOLS = [
u"\u03B1",
u"\u03B2",
u"\u03B3",
u"\u03B4",
u"\u03B5",
u"\u03B6",
u"\u03B7",
u"\u03B8",
u"\u03B9",
u"\u03BA",
u"\u03BB",
u"\u03BC",
u"\u03BD",
u"\u03BE",
u"\u03BF",
u"\u03C0",
u"\u03C1",
u"\u03C2",
u"\u03C3",
u"\u03C4",
u"\u03C5",
u"\u03C6",
u"\u03C7",
u"\u03C8",
u"\u03C9"
]

ProbInitialSurvival_min = 1
ProbInitialSurvival_a = 1
ProbInitialSurvival_Lambda = 3

ProbCapitalisation = 0.5
ProbTitleCase = 0.4

ProbInsertionMutation = 0.25


ProbAddGreek = 0.3
ProbAddNum = 0.3




##############################################################################
Phrase = input("What immunology word string drives you crazy?: ")
#Phrase = "iehfc icsao saiohh soiach awsciah9 csaouih csaoih"
print("You're right to be annoyed by: ", Phrase)

if len(Phrase.split()) == 0:
        print("What you talkin bout!")
        quit()


####################################
#STEP 1
####################################

def KeepLetters(Phrase):
        SplitWord = Phrase.split()
        ListOfProbabilities = np.array([])
        NumWords = len(SplitWord)
        for i in range(NumWords):
                Prob1 = ProbInitialSurvival_min - ProbInitialSurvival_a*i*(1 - i/(NumWords-1))
                Prob2 = (ProbInitialSurvival_Lambda)**len(SplitWord[i]) * np.math.exp(-ProbInitialSurvival_Lambda) / np.math.factorial(len(SplitWord[i])) + 0.5
                ListOfProbabilities = np.append(ListOfProbabilities, [[Prob1*Prob2]])
        if np.min(ListOfProbabilities) < 0:
                ListOfProbabilities -= np.min(ListOfProbabilities)

        ListOfProbabilities /= ListOfProbabilities[0]
        return ListOfProbabilities


Initialism = ""
WhichLetters = []
Probs = KeepLetters(Phrase)
for i in range(len(Phrase.split())):
        if random.random() < Probs[i]**0.5:
                Initialism += Phrase.split()[i][0]
                WhichLetters.append(i)



####################################
#STEP 2
####################################

u = random.random()
NumInserted = random.randint(2,3)

PrT = ProbInsertionMutation**NumInserted

if len(Phrase.split()[0]) < 3:
        pass
else:
        if u < PrT:
                pos1 = random.randint(0, len(Phrase.split()[0])-NumInserted)
                if WhichLetters[0] == 0:
                        Initialism = Phrase.split()[0][pos1:pos1+NumInserted] + Initialism[1:]
                else:
                        Initialism = Phrase.split()[0][pos1:pos1+NumInserted] + Initialism







####################################
#STEP 3
####################################

if Phrase[0] != Initialism[0]:
        Initialism = Phrase[0] + Initialism

u = random.random()
if u < ProbCapitalisation:
        Initialism = Initialism.upper()
elif u < ProbCapitalisation + ProbTitleCase:
        Initialism = Initialism.title()

u = random.random()
if u < ProbAddGreek:
        Initialism += "-"+random.choice(GREEK_SYMBOLS)
elif u < ProbAddGreek + ProbAddNum:
        Initialism += "-"+str(random.randint(0, 9))




print("Now no one will know what you mean: ", Initialism)
        


# In[ ]:




