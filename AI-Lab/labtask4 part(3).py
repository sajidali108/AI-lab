string= 'word'
liststr=list(string)
print(liststr)
new=''

for a in liststr[:-1]:
  for b in liststr[:-2]:
    if liststr[b] > liststr[b+1]:
      new=liststr[b]
      liststr[b]=liststr[b+1]
      liststr[b+1]= new
sorted_text = ''.join(liststr)
print(sorted_text)

