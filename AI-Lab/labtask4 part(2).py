userin=input('enter any string with punctuation marks: ')
result=userin
punctuation= '`!@#$^&;:?,/%'
for i in punctuation:
    result=result.replace(i,'')
print(result)