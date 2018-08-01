def post(fposts,insieme):
    with open(fposts,"r") as temp:
        txt=temp.readlines()
    risultato,badchar=[],[".",",",":",";",""," ","\n","?","!"]
    for x in insieme:
        for y in txt:
            if "<POST>" in y:
                N_POST="".join(ch for ch in y if ch.isdigit())
            if x.lower() in y.lower() and justrying(x,y,0,0,badchar)==True:
                risultato.append(N_POST)
    return set(risultato)

def justrying(x,y,_ind,ind_,badchar):
    try:
        y=y.lower()[ind_:]
        _ind=((y.lower()).index(x.lower()))-1
        ind_=((y.lower()).index(x.lower()))+(len(x.lower()))
        if y.lower()[_ind] in badchar and y.lower()[ind_] in badchar:
            return True
        else:
            return (justrying(x,y,_ind,ind_,badchar))
    except:
        return False
