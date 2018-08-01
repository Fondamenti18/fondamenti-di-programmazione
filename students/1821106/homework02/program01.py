import re

def initialize(file):
    file = open(file,"r")
    l = []
    for line in file:
        l.append(line)
    return l

def post(fposts,insieme):
    list = initialize(fposts)
    post_number = 0
    s = set()
    for i in range(0,len(list)):
        if "<POST>" in list[i]:
            post_number = re.search('[0-9]+',list[i]).group(0)
        for word in insieme:
            test = re.compile(r'\b%s\b' % word, re.I)
            if word.lower() in list[i].lower():
                if test.search(list[i]):
                    s.add(post_number)
    return s