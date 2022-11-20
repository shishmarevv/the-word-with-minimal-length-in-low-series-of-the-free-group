﻿import time


# Функции, сокращающие взаимообратные буквы
def cut(word: str):
    i = 0
    k = len(word)
    while i < k - 1:
        if (word[i] == 'a' and word[i + 1] == 'A') or (word[i] == 'A' and word[i + 1] == 'a') or (
                word[i] == 'b' and word[i + 1] == 'B') or (word[i] == 'B' and word[i + 1] == 'b'):
            word = word[:i] + word[i + 2:]
        k = len(word)
        i += 1
    if (len(word) > 1) and ((word[-2] == 'a' and word[-1] == 'A') or (word[-2] == 'A' and word[-1] == 'a') or (
            word[-2] == 'b' and word[-1] == 'B') or (word[-2] == 'B' and word[-1] == 'b')):
        word = word[:-2]
    return word


def many_cuts(n, word):
    result = word
    for i in range(n):
        result = cut(result)
    return result


# Функция, которая обращает любое слово
def invert(word):
    list_from_word = list(word)
    for i in range(len(list_from_word)):
        if list_from_word[i] == 'a':
            list_from_word[i] = 'A'
        elif list_from_word[i] == 'b':
            list_from_word[i] = 'B'
        elif list_from_word[i] == 'A':
            list_from_word[i] = 'a'
        elif list_from_word[i] == 'B':
            list_from_word[i] = 'b'
    temp = ''.join(map(str, list_from_word))
    return ''.join(reversed(temp))


# Функция, из двух слов делающая их коммутатор по правилу [a,b]=ABab
def commute(word1, word2):
    result = many_cuts(1000, invert(word1) + invert(word2) + word1 + word2)
    return result


# Функция, которая по уже имеющимся в файле элементам ряда X создает следующий
def create_x():
    file = open("memory0.txt", 'r')
    all = []
    counter = 0
    for line in file:
        counter += 1
        tstring = line.rstrip('\n')
        tstring = tstring.rstrip(' ')
        all.append(tstring.split(";"))
    result = []
    resultline = ''
    file.close()
    file = open("memory0.txt", 'a')
    filec = open('memory1.txt', 'a')
    commutatorsline = ''
    for i in range(counter):
        j = counter - i - 1
        for el1 in all[i]:
            for el2 in all[j]:
                if el1 != '' and el2 != '':
                    temp = commute(el1, el2)
                    if temp != '':
                        commutatorsline = commutatorsline + '[' + el1 + ', ' + el2 + '];'
                        result.append(temp)
                        resultline = resultline + temp + ';'
    resultline = resultline[:-1]
    commutatorsline = commutatorsline[:-1]
    file.write('\n' + resultline)
    file.close()
    filec.write('\n' + commutatorsline)
    filec.close()


# Функция, печатающая n-ый элемент ряда X
def print_x(n):
    file = open("memory0.txt", 'r')
    xnline = file.readlines()[n - 1]
    xn = xnline.split(';')
    for el in xn:
        print(el)
    file.close()


def find_min_length_in_x(n):
    file = open("memory0.txt", 'r')
    filec = open("memory1.txt", 'r')
    xnline = file.readlines()[n - 1]
    xnline = xnline.rstrip('\n')
    comline = filec.readlines()[n - 1]
    comline = comline.rstrip('\n')
    xn = xnline.split(';')
    comslice = comline.split(';')
    min_length = len(xn[0])
    min_length_el = xn[0]
    i = 0
    min_index = 0
    for el in xn:
        i += 1
        if len(el) < min_length:
            min_length = len(el)
            min_length_el = el
            min_index = i
    file.close()
    print(min_length)
    print(min_length_el)
    print(comslice[min_index])


def main():
    s = input()
    if s == 'create':
        n = int(input())
        for i in range(n):
            create_x()
    elif s == 'min':
        find_min_length_in_x(int(input()))
    elif s == 'print':
        print_x(int(input()))


starttime = time.time()
main()
print("--- %s seconds ---" % (time.time() - starttime))