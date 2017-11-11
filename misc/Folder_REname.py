import re
import os
tag = re.compile('^n*\d*-')
space = re.compile('_')
a = os.listdir()
for x in a:
	s = tag.sub('',x)
	s = space.sub(' ',s)
	#print(x,s)
	os.rename(x,s.title())