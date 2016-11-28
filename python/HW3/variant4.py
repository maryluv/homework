word = input("Введите слово: ")
for k in range(len(word)):
    newword = (word[-k: ] + word[ :-k])
    print(newword)
