import collections

def initialize(file):
    file = open(file,"r")
    l = []
    for line in file:
        l.append(line)
    return l

def decod(pfile, codice):
    s = set()
    list = initialize(pfile)
    for item in list:
        if len(item)-1 == len(str(codice)):
            item = item[:-1]
            key = [ord(test) for test in item]
            diz = dict(zip(collections.OrderedDict.fromkeys(key), collections.OrderedDict.fromkeys(str(codice))))
            test = item.translate(diz)
            if test.isdigit():
                test = int(test)
                codice = int(codice)
            if isinstance(test, int) and isinstance(codice, int):
                if int(test) == int(codice):
                    s.add(item)
    return s