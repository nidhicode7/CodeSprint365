''' COUNTING THE NUMBER OF LETTERS
EXAMPLE:BANANA
B-1
A-3
N2
'''

freq={}
for a in str:
  if a in freq:
    freq[a]+=1
  else:
    freq[a]=1
return freq
