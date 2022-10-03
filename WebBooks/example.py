def sortirovka(stroka):
    for j in range(len(stroka) - 1):
        for i in range(len(stroka) - 1):
            if int(stroka[i]) > int(stroka[i + 1]):
                stroka[i], stroka[i + 1] = stroka[i + 1], stroka[i]
    return stroka

stroka = input().split(' ')
stroka = list(stroka)
print(sortirovka(stroka))