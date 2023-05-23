import string
import re

# get input
sentence = input("Text :")
# count words
countWords = len(sentence.split())
# count letters/ sentence without punctuation
countLetters = len(sentence.translate(
    str.maketrans("", "", ", " + string.punctuation)))
# count sentences
countSentences = len(re.split(r'[.!?]+', sentence)) - 1
# calculate L
averageNumberOfLetters = countLetters / countWords * 100
# calculate S
averageNumerOfWords = countSentences / countWords * 100
# calculate grade
index = 0.0588 * averageNumberOfLetters - 0.296 * averageNumerOfWords - 15.8
# print
if round(index) < 1:
    print("Before Grade 1")
elif round(index) > 16:
    print("Grade 16+")
else:
    print("Grade ", round(index))
