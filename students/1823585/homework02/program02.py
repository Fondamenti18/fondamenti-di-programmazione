import json


def pianifica(fcompiti, insi, fout):
    '''Implementare qui la funzione'''
    with open(fcompiti, 'r') as f:
        a = f.readlines()
        for i in range(len(a)):
            a[i] = a[i].replace('\n', '').strip()
            if 'comp' in a[i]:
                a[i] = list(a[i])
                a[i].insert(4, ' ')
            else:
                a[i] = list(a[i])
                a[i].insert(3, ' ')
            a[i] = ''.join(a[i])
    diz = dict()
    num = []
    for indice in range(len(a)):
        appoggio = ''
        for i in range(len(a[indice])):
            if a[indice][i].isdigit():
                appoggio += a[indice][i]
        else:
            if 'comp' in a[indice]:
                num.append('comp' + appoggio)
            else:
                num.append('sub' + appoggio)
    num.append(' ')
    for index in range(len(num)):
        if 'comp' in num[index]:
            if 'sub' in num[index + 1]:
                diz[num[index]] = num[index + 1]
            elif 'comp' in num[index + 1]:
                diz[num[index]] = ''
        else:
            pass

    if 'comp' in num[-2]:
        diz[num[-2].replace(' ', '')] = ''

    finale = {}
    for elemento in insi:
        elemento = 'comp'+elemento
        if elemento in diz:
            sub = diz[elemento]
            ret = [sub.replace('sub', '')]
            while sub is not '':
                sub = diz[sub.replace('sub', 'comp')]
                ret.insert(0, sub[3:])
            finale[elemento[4:]] = ret[1:]

    json.dump(finale, open(fout, 'w'))