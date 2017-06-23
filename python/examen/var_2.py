import re
import os
  
##   1 задание     
def sent_count():
    path = './news/'
    for root, dirs, files in os.walk(path):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding = 'cp1251') as t:
                text = t.read()
                mass = []
                mass = text.split('\n')
                s_count = 0
                for i in mass:
                    if re.search('</se>', i):
                        s_count += 1
                with open('result.txt', 'a', encoding = 'utf-8') as file:
                    file.write(f +'\t' + str(s_count) + '\n')

##  2 задание (не успела доделать)
def write_csv():
    with open('result.csv', 'w', encoding = 'utf-8') as file:
        output = csv.writer(file, delimiter = ',')
        head = ['Название файла', 'Автор', 'Тематика текста']
        
    path = './news/'
    for root, dirs, files in os.walk(path):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding = 'utf-8') as t:
                text = t.read()
                if re.search('<meta content=\"(.*)\" name=\"author\"', text) and re.search('<meta content=\"(.*)\" name=\"topic\">', text):
                    auth = re.search('<meta content=\"(.*)\" name=\"author\"', text).group(1)
                    topic = re.search('<meta content=\"(.*)\" name=\"topic\">', text).group(1)
                    
        
def main():
    sent_count()

main()
