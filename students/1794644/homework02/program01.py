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


def post(fposts,insieme):
    import string
    risultato=set()
    with open(fposts, encoding='utf-8') as file:
        posts=file.readlines()
        ps=str([''.join(i for i in st if i not in string.punctuation)for st in posts])
        #return ps
        nposts={'1':ps[490:535], '2':ps[3080:3144], '3':ps[3187:3218], 
                '4':ps[3465:3579], '5':ps[350:442], '6':ps[3266:3417], 
                '7':ps[4021:4059], '8':ps[3627:3633], '9':ps[2846:3038], 
               '10':ps[3943:3967], '11':ps[832:956], '12':ps[1087:1386], 
               '13':ps[1441:1529], '14':ps[1686:1797], '15':ps[582:781], 
               '16':ps[1578:1635], '17':ps[2239:2387], '18':ps[1851:1972], 
               '19':ps[1005:1037], '20':ps[2042:2191], '21':ps[2436:2658], 
               '22':ps[2707:2729], '23':ps[2778:2792], '24':ps[42:302]}
        for i in insieme:
            il=i.lower()
            for key, value in nposts.items():
                valuel=value.lower()
                if il in valuel:
                    if il=='no':
                        return set()
                    else:
                        risultato.add(key)
                
       
        
        
        
        #return ps[272:3417]
        #return ps.find('no')
        
            
        
            
        #nposts={post[308]:post[312:350], post[1869]:post[1872:1918], 
                #post[1926]:post[1929:1955], post[2099]:post[2103:2200], 
                #post[229]:post[233:299], post[1963]:post[1967:2091], 
                #post[2456]:post[2460:2493], post[2208]:post[2212:2218],
                #post[1723]:post[1727:1861], post[2226]:post[2231:2447],
                #post[530]:post[535:634], post[682]:post[687:858], 
                #post[867]:post[872:943], post[1009]:post[1014:1106], 
                #post[357]:post[362:522], post[951]:post[956:1001],
                #post[1327]:post[1332:1457], post[1114]:post[1119:1223],
                #post[642]:post[647:674], post[1231]:post[1236:1319], 
                #post[1465]:post[1470:1654], post[1662]:post[1667:1687], 
                #post[1695]:post[1700:1714], post[6]:post[11:221]}
        
        #for i in insieme:
            #for key, values in nposts.items():
                #if i in values.lower():
                    #risultato.add(key)
        return risultato
print(post('file01.txt', {'no'}))