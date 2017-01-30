"""Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"}
and use it to translate your Christmas cards from English into Swedish. That is, write a function
translate() that takes a list of English words and returns a list of Swedish words."""

pyDic = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}

lis = []
n = int(input('Enter Number of elements in list:'))
for x in range(n):
    lis.append(input('Enter Values:'))
