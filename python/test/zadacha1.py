print("Задача 1")
with open('freq.txt', 'r', encoding = 'utf-8') as s: 
    for line in s: 
        arr = [] 
        arr = line.split(' | ') 
        if arr[1] == 'союз': 
            print (' | '.join(arr))
print("Задача 2")
with open('freq.txt', 'r', encoding = 'utf-8') as s:     
    sum = 0
    mass = []
    usl = []
    for line in s:
        arr = []
        arr = line.split(' | ')
        usl = arr[1].split(' ')
        if (len(usl) > 2) and (usl[2] == 'ед') and  (usl[3] == 'жен'):
            mass.append(arr[0])
            sum += float(arr[2])
    print(', '.join(mass))
    print('Сумма ipm = ', sum)
                
