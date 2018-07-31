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
def check_Equal(str1, str2):
      out=False
      if(len(str1)==len(str1)):
            out=True
      else:
            out=False

      return out

def Sort_Set(str1, str2):
      
      strin1=list(sorted(set(str1), key=str1.index))
      strin2=list(sorted(set(str2), key=str2.index))

      return strin1,strin2




def decod(pfile, codice):
      
       import string
       #out for output function
       out=set()
       #Read File and line by line
       with open(pfile) as f:
              for line in f:
                     line=line.strip()
                     if check_Equal(line,codice):
                            strin1,strin2=Sort_Set(line,codice)
                            if(len(strin1)==len(strin2)):
                                   i=0
                                   word=line
                                   for ch in strin1:
                                          word=word.replace(ch, strin2[i])
                                          i+=1
                                   if word==codice:
                                         out.add(line)
                            

       return out





