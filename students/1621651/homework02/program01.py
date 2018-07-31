def post(fposts,insieme):  
    import string
    with open(fposts, encoding='utf-8') as forum: 
        init='<POST>'
        linee=forum.readlines()
        diz={}
        listaID=[]
        listaposts=[]
        post=''
        for linea in linee:
            if init in linea:
                ID=''
                if post!='':
                    listaposts.append(post)
                post=''
                for c in linea:
                    if c.isdigit()==True:
                        ID+=c
                listaID.append(ID)
            else:
                post+=linea
        listaposts.append(post)
        diz=dict(zip(listaID, listaposts))
        match=set()
        punct=set(string.punctuation)
        for ID, post in diz.items():
            spost=post.lower().split(' ')
            nopun=' '.join(ch for ch in spost if ch not in punct)
            for w in insieme:
                if w.isalpha()==True:    
                    if w.lower() in nopun:
                        match.add(ID)
        return match