
'''Dato un testo da codificare ed una chiave si propone il seguente schema crittografico:

- dalla chiave vengono eliminati  tutti i caratteri C per cui C<'a' o C>'z'. 
- di ciascuno dei caratteri restanti vengono cancellate dalla chiave tutte le occorrenze 
  tranne l'ultima, ottenendo una sequenza DISORDINATA. 
- i caratteri presenti nella stringa cosi' ripulita saranno i soli caratteri del testo 
  ad essere codificati ovvero sostituiti nel testo crittografato (gli altri resteranno invariati). 
- la sequenza ORDINATA dei caratteri rimasti nella chiave viene messa in corrispondenza 
  con la sequenza DISORDINATA dei caratteri ottenuti al passo precedente.

Come esempio di applicazione  consideriamo la chiave
 "sim sala Bim!"
a seguito delle eliminazioni la chiave produce la sequenza DISORDINATA
 "slaim"
 
I soli caratteri del testo  a subire una codifica sarano 's','l', 'a' 'i' ed 'm'. 
Per sapere con cosa verranno codificati questi caratteri si considera la seguente corrispondenza
tra sequenze:
    "ailms" (sequenza ordinata degli stessi caratteri)
    "slaim" (sequenza disordinata ottenuta dalla chiave)
questo determina gli accoppiamenti (a,s), (i,l) (l,a), (m,i) ed (s,m)
la 'a' dunque sara' codificata con 's', la 'i' con 'l' e cosi' via.

Utilizzando la chiave "sim sala Bim!" per codificare il testo  "il mare sa di sale" si 
 otterra' il seguente testo crittografato:
    "il mare sa di sale"   (testo in chiaro)
    "la isre ms dl msae"   (testo crittografato)

La decodifica del testo crittografato opera sulla stessa chive ma sostituisce le lettere
presenti nella sequenza disordinata con quelle della sequenza ordinata.
Quindi nell'esempio precedente le sostituzioni sono invertite:
 (s, a), (l, i) (a, l), (i, m) ed (m, s)

Per altri esempi vedere il file grade03.txt

Implementate le due funzioni
    codifica(chiave, testo_in_chiaro) -> testo_crittografato
    decodifica(chiave, testo_crittografato) -> testo_in_chiaro

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''

def codifica(chiave, testo):
    l = no_spazi(chiave)
    o = no_simboli(l)
    j = no_upper(o)
    chiave = no_occorrenze(j)
    ls =[]
    for i in range(len(chiave)):
        ls.append(chiave[i])
        ls.sort()
    chiave_ordinata = ''
    for el in ls:
        chiave_ordinata += el
    ls_tuple=[]
    for i in range(len(chiave_ordinata)):
        ls_tuple.append((chiave_ordinata[i], chiave[i]))
    s = ''
    if ls_tuple==[]:
        s += testo
        return s
    else:
        for i in range(len(testo)):
            for el in ls_tuple:
                if testo[i] == el[0]:
                    m = testo[i].replace(testo[i], el[1])
                    s += m
                    break
                if el == ls_tuple[len(ls_tuple) - 1]:
                    s += testo[i]
                    break
        return s

def decodifica(chiave, testo):
    l = no_spazi(chiave)
    o = no_simboli(l)
    j = no_upper(o)
    chiave = no_occorrenze(j)
    ls =[]
    for i in range(len(chiave)):
        ls.append(chiave[i])
        ls.sort()
    chiave_ordinata = ''
    for el in ls:
        chiave_ordinata += el
    ls_tuple=[]
    for i in range(len(chiave_ordinata)):
        ls_tuple.append((chiave[i], chiave_ordinata[i]))
    s = ''
    if ls_tuple==[]:
        s += testo
        return s
    else:
        for i in range(len(testo)):
            for el in ls_tuple:
                if testo[i] == el[0]:
                    m = testo[i].replace(testo[i], el[1])
                    s += m
                    break
                if el == ls_tuple[len(ls_tuple) - 1]:
                    s += testo[i]
                    break
        return s


def no_spazi(chiave):
    for i in range(len(chiave)):
        if chiave[i] == ' ':
            l = chiave.replace(' ', '')
            chiave = l
        else:
            return chiave

def no_simboli(l):
    i = 0
    if not l.isalpha():
        while i < len(l):
            if l[i].isalpha():
                i += 1
            else:
                n = l.replace(l[i], '')
                l = n
                i = i
        return l
    else:
        return l

def no_upper(o):
    el = 0
    if not o.isupper():
        while el < len(o):
            if not o[el].isupper():
                el += 1
            else:
                m = o.replace(o[el], '')
                o = m
                el = el
        return o
    elif o.isupper():
        return ''

def no_occorrenze(j):
    cont = 0
    el = 0
    while el < len(j):
        cont = j.count(j[el])
        cont1 = cont - 1
        count = cont - cont1
        if cont > 1:
            l = j.replace(j[el], '', count)
            j = l
            el = 0
        elif cont == 1:
            el += 1
    return j
    
