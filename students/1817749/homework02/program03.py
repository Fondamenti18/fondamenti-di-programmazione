def control(codice, line):
    dic = {}
    for index in range(len(line)):
        if codice[index] in dic and dic[codice[index]] != line[index]:
            return False
        dic[codice[index]] = line[index]
    return True


def decod(pfile, codice):
    return set([line[:-1] for line in open(pfile) if len(codice) == len(line[:-1]) and len(set(codice)) == len(set(line[:-1])) and control(codice, line[:-1])])