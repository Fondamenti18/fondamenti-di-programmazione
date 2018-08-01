#lista di conversione e lista dei flags
flags=[]
pref_sing= ['cento','unmila','unmilione','unmiliardo','mille']
pref_plur= ['','mila','milioni','miliardi']
alfa_c= ['zero','dieci','venti','trente','quaranta','cinquanta','sessanta','settanta','ottanta','novanta']
alfa_d= ['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove']
alfa_u= ['zero','uno','due','tre','quattro','cinque','sei', 'sette', 'otto','nove']

#funzione principale di conversione
def conv(n):
    if n<1 or n>=1000000000000:
        return 'errore parametro'

    set_flags(n,flags)
    stringa=''

    #ogni ciclo opera a blocchi di 3 cifre
    while flags[0] >flags[1] :
        n_alfabetico=''
        flags[4]=0
        flags[5]=False 

        n_alfabetico= calcola_centinaia (n_alfabetico,n)
        n_alfabetico= calcola_decine (n_alfabetico,n)
        n_alfabetico= calcola_unita (n_alfabetico,n)
        
        stringa+=n_alfabetico

    del flags[:]
    return stringa

#accoda le centinaia al terzetto alfabetico
def calcola_centinaia(n_alfabetico,n):
    cifra = int(str(n)[flags[1]])
    
    if flags[2] > 1:
        if cifra > 0:
            if cifra != 1:
                n_alfabetico = alfa_u[cifra] + pref_sing[0];
            else:
                n_alfabetico = pref_sing[0];
            flags[4] = 1;
        flags[1]+=1;
        
    return n_alfabetico

#accoda le decine al terzetto alfabetico
def calcola_decine(n_alfabetico,n):
    cifra = int(str(n)[flags[1]])
    
    if flags[2] >= 1:
        if cifra == 1:
            flags[5]=True
        elif cifra > 1:
            if cifra==8:
                n_alfabetico=n_alfabetico[:len(n_alfabetico)-1]
            n_alfabetico += alfa_c[cifra];
            flags[4] = 2;
        flags[1]+=1;
        
    return n_alfabetico

#si occupa di accodare le unita e il suffiso al terzetto alfabetico tramite altre funzione
def calcola_unita(n_alfabetico,n):
    cifra = int(str(n)[flags[1]])
    
    if flags[2]>=0:

        n_alfabetico= aggiungi_unita(n_alfabetico,cifra)
        n_alfabetico= calcola_suffisso (n_alfabetico,cifra)

        flags[3]-=1		
        flags[1]+=1
        flags[2]=2
        
    return n_alfabetico

#accoda le unita al terzetto alfabetico
def aggiungi_unita(n_alfabetico,cifra):
    if flags[5] == True:
        n_alfabetico=n_alfabetico+alfa_d[cifra]
        flags[4]=1
    else:
        n_alfabetico=aggiungi_10_20(cifra, n_alfabetico)
    return n_alfabetico

#accoda, se chiamata, i numeri da 10 a 19
def aggiungi_10_20(cifra, n_alfabetico):
    if (cifra==1 or cifra==8) and flags[4]==2:
        n_alfabetico=n_alfabetico[:len(n_alfabetico)-1]
    if (cifra==1 and flags[4]>0) or flags[3]==0 or cifra>1:
        n_alfabetico=n_alfabetico+alfa_u[cifra]
    return n_alfabetico

#calcola il suffisso del terzetto
def calcola_suffisso(n_alfabetico,cifra):
    if  cifra!=0 or flags[3]==3 or flags[5] == True or flags[4]>0:
        n_alfabetico=aggiungi_suffisso(n_alfabetico,cifra)
        n_alfabetico=correggi_mille(n_alfabetico)

    return n_alfabetico

#accoda il prefisso al terzetto alfabetico
def aggiungi_suffisso(n_alfabetico,cifra):
    if flags[4]==0 and cifra==1:
        n_alfabetico+=pref_sing[int(flags[3])]
    else:
        n_alfabetico+=pref_plur[int(flags[3])]
    return n_alfabetico

#se esce fuori mila senza numero prima, corregge in mille
def correggi_mille(n_alfabetico):
    if flags[1]==0 and (n_alfabetico==pref_plur[1] or n_alfabetico==pref_sing[1]):
        n_alfabetico = pref_sing[4]  
    return n_alfabetico

#iniziallizza i valori dei flags
def set_flags(n,flags):
	flags+=[len(str(n))] #numero di cifre del numero
	flags+=[0] #posizione della cifra attuale
	flags+=[(flags[0]-1)%3] # colonna (di riferimento): cent dec o unita
	flags+=[(flags[0]-1)/3] # blocchi: il numero dei blocchi da 3 cifre del num [c,d,u]
	flags+=[0] #se attivo indica che o nelle cent o nelle dec ce un numero diverso da 0
	flags+=[False] #se attivo indica che nelle decine ce l' 1
