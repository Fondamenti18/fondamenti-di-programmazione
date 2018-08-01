import bisect
import json


def genera_sottoalbero(fnome, x, fout):
    json.dump(stick_together(json.loads(open(fnome).read()), x, {}), open(fout, 'w'))


def stick_together(total, element, to_ret):
    to_ret[element] = total[element]
    for arg in total[element]:
        stick_together(total, arg, to_ret)
    return to_ret


def cancella_sottoalbero(fnome, x, fout):
    json.dump(havana(sleep_an(json.loads(open(fnome).read()), x), x), open(fout, 'w'))


def havana(total, erg):
    for key in total:
        if erg in total[key]:
            total[key].remove(erg)
            return total


def sleep_an(total, element):
    for arg in total[element]:
        sleep_an(total, arg)
    del total[element]
    return total


def get_dict_root(dictionary, start):
    for key, value in dictionary.items():
        if start in value:
            return get_dict_root(dictionary, key)
    return start


def dizionario_livelli(fnome, fout):
    dictionary = json.loads(open(fnome).read())
    json.dump(potato_head(dictionary, get_dict_root(dictionary, next(iter(dictionary.keys()))), 0, {}), open(fout, 'w'))


def potato_head(dictionary, key, level, to_ret):
    if level not in to_ret:
        to_ret[level] = []
    bisect.insort(to_ret[level], key)
    for arg in dictionary[key]:
        potato_head(dictionary, arg, level + 1, to_ret)
    return to_ret


def dizionario_gradi_antenati(fnome, y, fout):
    dictionary = json.loads(open(fnome).read())
    json.dump(kill_the_lights(dictionary, get_dict_root(dictionary, next(iter(dictionary.keys()))), y, 0, {}), open(fout, 'w'))


def kill_the_lights(dictionary, key, baka, level, to_ret):
    to_ret[key] = level
    if len(dictionary[key]) == baka:
        level += 1
    for arg in dictionary[key]:
        kill_the_lights(dictionary, arg, baka, level, to_ret)
    return to_ret
