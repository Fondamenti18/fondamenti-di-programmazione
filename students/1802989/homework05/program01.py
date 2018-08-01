from random import choice, sample
from itertools import combinations, permutations

working_ls = list()
x = list()
n = 0
indice = 1

def decodificatore(config):
    length = len(config)
    global indice
    if length == 1:
        #Base case
        global x, n
        indice = 1
        n = config[0]
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        return base_case()

    elif length == 2:
        #All possible combinations
        global working_ls
        ab_tuple = config[1][1][0] + config[1][1][1]
        subseq_len =  n - ab_tuple
        working_ls = gen_combinations(subseq_len, config[1][0], ab_tuple, working_ls)
        item, value = config[indice]
        working_ls = possible_solutions(item, value)
        return choice(working_ls)

    else:
        #Inductive step
        indice += 1
        item, value = config[indice]
        working_ls = possible_solutions(item, value)
        return choice(working_ls)

def base_case():
    'This function plays a random attempt'
    rnd_attempt = []
    for _ in range(n):
        y = choice(x)
        rnd_attempt.append(y)
        x.remove(y)
    return rnd_attempt

def gen_combinations(subseq_len, config, ab_tuple, working_ls):
    'Function that generates all possible solutions, relating to first attempt'
    for element in combinations(config, ab_tuple):
        for leftover in combinations(x, subseq_len):
            working_ls += permutations(element+leftover)
    return [el for el in working_ls if len(el) == n]

def possible_solutions(item, value):
    "Function that filters results based on simulatore's feedbacks"
    ls = list()
    v = set(value)
    for proposal in working_ls:
        a,b = 0,0
        for i in range(n):
            if proposal[i] == item[i]: a += 1
            elif proposal[i] in item: b += 1
        if set((a,b)) == v: ls.append(proposal)
    return ls