'''
Abbiamo una stringa i cui elementi sono cifre tra '0' e '9' (comprese) che rappresenta la struttura di una parola.
La parola contiene al piu' 10 lettere diverse (ma puo' essere piu' lunga di 10 lettere se alcune sono ripetute), 
e la struttura si ottiene dalla parola sostituendo ciascuna lettera con una cifra, secondo le regole:
- a lettera uguale corrisponde cifra uguale
- a lettere diverse corrispondono cifre diverse

Esempio: 'cappello' -> '93447228'
Esempio: 'cappello' -> '12334556'

Sia data una "struttura" ed un insieme di parole. 
Vogliamo ottenere il sottoinsieme delle parole date compatibili con la struttura data.

Esempio: se la struttura e' '1234' e le parole sono { 'cane', 'gatto', 'nasa', 'oca', 'pino'}
le parole dell'insieme che sono compatibili con la struttura sono {'pino', 'cane'}

Scrivere una funzione decod( pfile, struttura) che prende in input:
- il percorso di un file (pfile), contenente testo organizzato in righe ciascuna composta da una sola parola
- una stringa di almeno 1 carattere, composta solo da cifre (la struttura delle parole da cercare)

La funzione  deve restituire l'insieme delle parole di pfile che sono compatibili con la struttura data.

Per gli esempi vedere il file grade03.txt

AVVERTENZE: 
	non usare caratteri non ASCII, come le lettere accentate;
	non usare moduli che non sono nella libreria standard.
NOTA: l'encoding del file e' 'utf-8'
ATTENZIONE: Se un test del grader non termina entro 10 secondi il punteggio di quel test e' zero.
'''


def decod(pfile, codice):
  with open(pfile, encoding='utf8') as f:
    s=str(f.read()).split('\n')
    comp=set()
    lista=[]
    lista+=codice
    sl=[]
    sk=[]
    app=[]
    app2=[]
    for i in s:
      sl.append(i.split())
    for j in sl:
      if len(j) is len(codice):
        sk.append(j)
    for i in sk:
      app.append(i)
      ls=[]
      for j in app:
        if not j in ls:
          ls.append(j)
      
      ls2=[]
      for j in lista:
        if not j in ls2:
          ls2.append(j)
      d=dict(zip(ls2, ls))
      for x in codice:
        if x in d:
          app2+= d[x]
      if app == app2:
        stringa=''.join(app2)
        comp.add(stringa)
      app=[]
      app2=[]
      lista+=codice
      ls=[]
      ls2=[]
    return (comp)        
            
        
          
      
          
        
    
    
      
   





