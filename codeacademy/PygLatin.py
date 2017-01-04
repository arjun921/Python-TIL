words = str(input('Enter word'))
first = words[0]
pyg = []
for x in range(1,len(words)):
    pyg.append(words[x])

pyg.insert(len(words),first)
pyg.append('ay')
words = ''.join(pyg)
print (words)
