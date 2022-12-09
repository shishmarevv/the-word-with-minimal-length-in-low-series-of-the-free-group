import time


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
        tstring = tstring[3:]
        all.append(tstring.split(";"))
    result = []
    resultline = str(counter + 1) + '::'
    file.close()
    file = open("memory0.txt", 'a')
    filec = open('memory1.txt', 'a')
    commutatorsline = str(counter + 1) + '::'
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


def compete():
    file1 = open("memory0.txt", 'r')
    file2 = open("memory1.txt", 'r')
    file3 = open("memory3.txt", 'a')
    dict = {'a': 'a', 'b': 'b', 'ABab': '[a,b]', 'BAba': '[b,a]'}
    period = []
    words_list = []
    counter = 0
    for line in file1:
        tstring = line.rstrip('\n')
        period.append(counter)
        tstring = tstring.replace(' ', '')
        tstring = tstring[3:]
        tlist = tstring.split(";")
        for x in tlist:
            words_list.append(x)
            counter += 1
    commutators_list = []
    for line in file2:
        tstring = line.rstrip('\n')
        tstring = tstring.rstrip(' ')
        tstring = tstring[3:]
        tlist = tstring.split(";")
        for x in tlist:
            y = x.replace("[", "")
            y = y.replace("]", '')
            y = y.replace(" ", '')
            y = y.split(",")
            commutators_list.append(y)
    for i in range(4, len(words_list)):
        dict[words_list[i]] = '[' + dict[commutators_list[i][0]] + ',' + dict[commutators_list[i][1]] + ']'
    result = ""
    counter = 2
    for i in range(len(words_list)):
        result = result + dict[words_list[i]] + ";"
        if i + 1 in period:
            result = result[:-1] + '\n' + str(counter) + "::"
            counter += 1
    file3.write(result)
    file3.close()
    file2.close()
    file1.close()


# Функция, печатающая n-ый элемент ряда X
def print_x(n):
    file = open("memory0.txt", 'r')
    xnline = file.readlines()[n - 1]
    xn = xnline.split(';')
    for el in xn:
        print(el)
    file.close()


# Функция, сохраняющая все элементы минимальной длины в X_n
def find_min_length_in_x(n):
    file = open("memory0.txt", 'r')
    file_com = open("memory1.txt", 'r')
    file_com2 = open("memory3.txt", 'r')
    xn_line = file.readlines()[n - 1]
    xn_line = xn_line.rstrip('\n')
    xn_line = xn_line[3:]
    com_line = file_com.readlines()[n - 1]
    com_line = com_line.rstrip('\n')
    com_line = com_line[3:]
    com2_line = file_com2.readlines()[n - 1]
    com2_line = com2_line.rstrip('\n')
    com2_line = com2_line[3:]
    xn = xn_line.split(';')
    com_slice = com_line.split(';')
    com2_slice = com2_line.split(';')
    min_length = len(xn[0])
    i = 0
    min_index = 0
    for el in xn:
        if len(el) < min_length:
            min_length = len(el)
            min_index = i
        i += 1
    file_min = open("memory2.txt", 'a')
    save_line = '\n' + str(n) + str(min_length) + '::'
    for i in range(len(xn)):
        if len(xn[i]) == min_length:
            save_line = save_line + xn[i] + "||" + com_slice[i] + '||' + com2_slice[i] + ';'
    save_line = save_line[:-1]
    file_min.write(save_line)
    file.close()
    file_com.close()
    file_min.close()


def main():
    s = input()
    if s == 'create':
        n = int(input('Сколько еще элементов ряда нужно сгенерировать?'))
        for i in range(n):
            create_x()
    elif s == 'min':
        find_min_length_in_x(int(input("Минимальная длина какого элемента?")))
    elif s == 'print':
        print_x(int(input()))
    elif s == 'commute':
        s1 = input("Первый коммутируемый")
        s2 = input("Второй коммутируемый")
        s3 = commute(s1, s2)
        print(s3)
        print(len(s3))
    elif s == 'comp':
        compete()
        print("competed")
    else:
        print("XD")


starttime = time.time()
main()
print("--- %s seconds ---" % (time.time() - starttime))
