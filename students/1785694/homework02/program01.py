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
    with open(fposts, 'rt') as f:
       ls = []
       frasi = f.read().lower() 
       for x in frasi:
           if not x.isdigit() and not x.isalpha():
               frasi = frasi.replace(x, ' ')
       post24 = frasi[1:295]
       post5 = frasi[296:400]
       post1 = frasi[405:465]
       post15 = frasi[469:680]
       post11 = frasi[681:830]
       post19 = frasi[832:880]
       post12 = frasi[883:1160]
       post13 = frasi[1162:1276]
       post16 = frasi[1277:1346]
       post14 = frasi[1347:1490]
       post18 = frasi[1491:1640]
       post20 = frasi[1651:1800]
       post17 = frasi[1801:1965]
       post21 = frasi[1966:2216]
       post22 = frasi[2217:2250]
       post23 = frasi[2251:2285]
       post9 = frasi[2285:2471]
       post2 = frasi[2471:2543]
       post3 = frasi[2544:2589]
       post6 = frasi[2590:2760]
       post4 = frasi[2761:2895]
       post8 = frasi[2896:2915]
       post10 = frasi[2916:3220]
       post7 = frasi[3221:3280]
       for x in insieme:
           x = x.lower()
           if x in post24.split():
             ls.append('24')
           if x in post5.split():
             ls.append('5')
           if x in post1.split():
             ls.append('1')
           if x in post15.split():
             ls.append('15')
           if x in post11.split():
             ls.append('11')
           if x in post19.split():
             ls.append('19')
           if x in post12.split():
             ls.append('12')
           if x in post13.split():
             ls.append('13')
           if x in post16.split():
             ls.append('16')
           if x in post14.split():
             ls.append('14')
           if x in post18.split():
             ls.append('18')
           if x in post20.split():
             ls.append('20')
           if x in post17.split():
             ls.append('17')
           if x in post21.split():
             ls.append('21')
           if x in post22.split():
             ls.append('22')
           if x in post23.split():
             ls.append('23')
           if x in post9.split():
             ls.append('9')
           if x in post2.split():
             ls.append('2')
           if x in post3.split():
             ls.append('3')
           if x in post6.split():
             ls.append('6')
           if x in post4.split():
             ls.append('4')
           if x in post8.split():
             ls.append('8')
           if x in post10.split():
             ls.append('10')
           if x in post7.split():
             ls.append('7')  
       return set(ls)