import itertools

combinations = None


def gen_code_from_to(start, end, length):
    if end > 9:
        end = 9
    return [start + x if start + x < end else end for x in range(length)]


def generate_combos(steps, length):
    return [itertools.permutations(combo) for combo in
            [set(itertools.chain.from_iterable(combo)) for combo in itertools.product(
                *[itertools.combinations(set(steps[i][0]), sum(steps[i][1])) for i in range((length + 1) // 3)])] if
            len(combo) == length]


def generate_configurations(steps, length):
    final_set = set()
    for combo in generate_combos(steps, length):
        final_set.update(combo)
    return list(final_set)


def answer(code, lets_try):
    a = sum([code[i] == lets_try[i] for i in range(len(code))])
    return a, len(set(code) & set(lets_try)) - a


def same_result(code, step):
    result = answer(code, step[0])
    return result == step[1] or tuple(reversed(result)) == step[1]


def think(possibility, step):
    possible = [code for code in possibility if same_result(code, step)]
    if step[0] in possible:
        possible.remove(step[0])
    return possible


def gen_starter_code(config_len, code_len):
    if code_len == 8:
        return gen_code_from_to((config_len - 1) * 4, (config_len * 4) - 1, 8)
    return gen_code_from_to((config_len - 1) * 5, (config_len * 5) - 1, code_len)


def first_decode(config, code_len):
    if code_len == 8:
        return think(think(generate_configurations(config[1:4], code_len), config[1]), config[2])
    return think(generate_configurations(config[1:3], code_len), config[1])


def decodificatore(configurazione):
    global combinations
    if len(configurazione) <= (configurazione[0] + 1) // 3:
        return gen_starter_code(len(configurazione), configurazione[0])
    if len(configurazione) == (configurazione[0] + 1) // 3 + 1:
        combinations = first_decode(configurazione, configurazione[0])
    combinations = think(combinations, configurazione[-1])
    return combinations[len(combinations) // 3]
