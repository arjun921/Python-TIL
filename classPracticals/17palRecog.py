"""Write a version of a palindrome recognizer that also accepts phrase palindromes such as
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
"Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
"Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing
are usually ignored."""

s = "Step on no pets"
def reverse(s):
	rev = []
	for x in range(1,len(s)+1):
        	rev.append(s[-x])
	return ''.join(rev)

def removePunc(s,temp):
    """Removes punctuation, capitalization, and spacing"""
    for x in range(len(s)):
        if s[x] not in " ,?.''":
            temp.append(s[x].lower())

def spliter(temp,split1,split2):
    """splits given string into half"""
    for x in range(len(temp)):
            if x<len(temp)/2:
                split1.append(temp[x])
            else:
                split2.append(temp[x])
split1 = []
split2 = []
temp = []

removePunc(s,temp)
spliter(temp,split1,split2)
split1 = str(''.join(split1))
split2 = str(reverse(''.join(split2)))


if split1 == split2:
    print ('True')
else:
    print ('False')
