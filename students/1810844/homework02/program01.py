'''
I post di un forum sono raccolti in alcuni file che hanno il seguente formato. 
Un file contiene uno o piu' post, l'inizio di un post e' marcato da una linea che contiene
in sequenza le due sottostringhe "<POST>" ed "N" (senza virgolette) eventualmente 
inframmezzate, precedute e/o seguite da 0,1 o piu' spazi. 
"N" e' l'ID del post (un numero positivo).  
Il contenuto del post e' nelle linee successive fino alla linea che marca il prossimo post 
o la fine del file (si veda ad esempio il file "file01.txt"). 
E' assicurato che la stringa "<POST>" non e' contenuta in nessun post.

Nel seguito per parola intendiamo come al solito una qualsiasi sequenza di caratteri
alfabetici di lunghezza massimale. I caratteri alfabetici sono quelli per cui
ritorna True il metodo isalpha().

Scrivere una funzione post(fposts,insieme) che prende in input:
- il percorso di un file (fposts) 
- ed un insieme  di parole (insieme)
e che restituisce un insieme (risultato).

L'insieme restituito (risultato) dovra' contenere gli identificativi (ID) dei post 
che contengono almeno una parola dell'inseme in input.
Due parole sono considerate uguali anche se  alcuni caratteri alfabetici compaiono in una 
in maiuscolo e nell'altra in minuscolo.

Per gli esempi vedere il file grade.txt

AVVERTENZE:
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''
def divisione_post(nome_file):
    file = open(nome_file);
    
    #Variabili
    ini = 0;
    fin = 0;
    post = [];
    app = '';
    i = 0;
    
    f = file.read();
    ini = f.find("<POST>");
    fin = f.find("<POST>",ini+1);
    
    while i < len(f):
        j = ini;
        
        if fin == -1:
            while j < len(f):
                app += f[j];
                j += 1;
        else:
            while j < fin:
                app += f[j];
                j += 1;
        
        post.append(app);
        app = '';
        ini = fin;
        fin = f.find("<POST>",ini+1);
        i = j+1;
        
    file.close();
    return post;

def controlla(lista,insieme):
    p = list(insieme);
    insieme2 = set();
    num_post = 0;
    #Trasformo tutte le parole dell'insime in minuscole
    for x in range(0,len(p)):
        p[x] = p[x].lower();
        insieme2.add(p[x]);
    #Controllo se qualla parola è presente nell'insieme
    for x in range(0,len(lista)):
        if lista[x].lower() in insieme2:
            num_post = lista[1];
            break;
    return num_post;

#Creo una mia funzione split che funziona come si deve
def my_split(stringa):
    lista = [];
    
    i = 0;
    app = "";
    while i < len(stringa):
        if (ord(stringa[i])>64 and ord(stringa[i])<91) or (ord(stringa[i])>96 and ord(stringa[i])<123) or (ord(stringa[i])>47 and ord(stringa[i])<58):
            app += stringa[i];
        elif app != "":
            lista.append(app);
            app = "";
        i += 1;
    return lista;
    
def post(fposts,insieme):
    ''' implementare qui la funzione'''
    insiemone = set()
    posts = divisione_post(fposts);
    
    for x in range(0,len(posts)):
        p = my_split(posts[x]);
        app = controlla(p,insieme);
        if app != 0:
            insiemone.add(app);
    return insiemone;
#a = divisione_post("file01.txt");
#print(a)
#print(a[10].split())