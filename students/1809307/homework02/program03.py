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
    with open(pfile,encoding='utf-8') as f:
        letturafile=f.read()
        stringaturafile=str(letturafile)
        l=[]
        l2=[]
        contL=[]
        cont2=[]
        cont1=[]
        cont1+=codice
        insieme= set()
        i=0
        stringasplit=stringaturafile.split('\n')
        for x in stringasplit:
            l+=x.split()
        l2 = [s for s in l if len(s) is len(codice)]
        for x in l2:
            contL+=x
            
            
            lista1=[]
            [lista1.append(item) for item in contL if item not in lista1]
            
            
            lista2=[]
            [lista2.append(item) for item in cont1 if item not in lista2]
            
            dict1 = dict(zip(lista2, lista1))
            
            for k in codice:
                if k in dict1:
                    
                    cont2+=dict1[k]
           
            if contL == cont2:
                
                b = ''.join(cont2)
                insieme.add(b)
            
            contL=[]
            cont1=[]
            cont1+=codice
            lista1=[]
            lista2=[]
            cont2=[]
        
        return(insieme)
            

                    

            

                
                
        
                
        
                
            
            
    





