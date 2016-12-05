arr = [] 
with open('text.txt','r', encoding = 'utf-8') as t: 
    text = t.read() 
    text = text.replace('\n', ' ') 
    arr = text.split(' ') 

k = 0 
for word in arr: 
    if (word[-1] != '.') and (word[-1] != ',') and (word[-1] != '!'): 
        k +=1 

words = len(arr) 
percent = k/words * 100
print(words)
print(k)

print('Процент слов, не оканчивающихся на знак препинания, равен ', percent, ' %')
