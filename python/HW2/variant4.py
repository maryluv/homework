mass = [] 
word = input('Введите латинское слово: ') 
while word: 
    mass.append(word) 
    word = input('Введите латинское слово: ') 
for ind in mass: 
    if ind.endswith('re') or ind.endswith('ri') or ind.endswith('isse'): 
        print(ind)
