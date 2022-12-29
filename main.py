myFile = open("Shakespeare.txt") 
d = { } #dictionary with no words in it yet 
newDict = { }

for line in myFile :  
  line = line.split()
  for word in line:
    word = word.lower()
    if word not in d: #if the new word is NOT in the dictionary...
      d[word] = 1 #store a dictionary entry for the pair by using the word as the key and the integer 1 as the value
    else:
      currentValue = d.get(word) # get the value for this word
      d[word] = currentValue + 1 #update the existing key value pair by incrementing its current value by 1
      if currentValue > 3: #new dictionary created to prioritize those words that are repeated the most, given the limited view space of the console
        newDict[word] = currentValue 

myFile.close() 
  
sortedDict = sorted(newDict.items(), key = lambda x: x[1], reverse = True)
for item in sortedDict:
  print(item)
  print()