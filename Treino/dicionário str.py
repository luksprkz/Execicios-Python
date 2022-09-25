text = '''

I'd one drink, drink but no more

I was rambling, enjoying the bright moonlight

I was numb with fear, but still


And I danced, and I pranced
They were undead, all of them

I ran like hell, faster than the wind

'''
text=text.replace(',','')
text=text.replace('.','')
word_count = {}
for word in text.lower().split():
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

 
print (word_count)