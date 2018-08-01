
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
    '''inserire qui la vostra implementazione'''
    # 1.Si eliminano tutti i caratteri che non sono lettere minuscole
    # 2.Si cancellano tutte le occorrenze delle lettere uguali in una parola, lasciandone solamente una, l'ultima
    # 3.Si ordina la sequenza ottenuta dai punti 1. e 2.
    # 4.Si associa la sequenza ordinata con quella disordinata creando coppie (ottengo delle tuple) tra elementi corrispondenti
    chiave = chiave.split()
    for elemento in chiave:
        # controlla ed elimina tutto ciò che non sia una lettera minuscola
        if elemento.isalpha() != True and elemento.islower() != True:
            chiave.remove(elemento)
    chiave2 = ''.join(chiave)
    lista = []
    for el in chiave2:
        lista.extend(el)
    for lettera in lista:
        # creo una lista per gestire le occorrenze delle lettere
        while lista.count(lettera) > 1:
            lista.remove(lettera)
            # rimuovo le lettere che hanno occorrenza > 1, lasciando l'ultima lettera
    chiave_dis = ''.join(lista)
    # chiave_dis: creo la chiave disordinata
    lista.sort()
    chiave_ord = ''.join(lista)
    # chiave_ord: ordinando la chiave disordinata creo la chiave ordinata
    lista_t = []
    # lista_t: lista che conterrà le coppie di lettere delle chiavi (dis,ord)
    tupla = ()
    for i,j in zip(chiave_dis,chiave_ord):
        tupla = (i,j)
        # tupla: coppia lettera sequenze dis,ord
        lista_t.append(tupla)
        # metto la tupla nella lista
    to_code = testo
    # to_code: creo una variabile di appoggio per non modificare direttamente il valore passato ddalla funzione
    lista_fin= []
    for lettera in to_code:
        if lettera == " " :
        # con questo gestisco gli spazi
            lista_fin += " "
        for tupla in lista_t:
            if lettera == tupla[1]:
                l_mod = lettera.replace(lettera,tupla[0])
                lista_fin += l_mod
                # salvo il risultato in una lista altrimenti andrebbe perso
    testo = "".join(lista_fin)  #creo un testo con le lettere modificate della mia lista
    return(testo)

def decodifica(chiave, testo):
    '''inserire qui la vostra implementazione'''
    # identica a codifica, solo che in decodifica devo mettere in relazione nelle tupla le coppie ordinata-disordinata
    chiave = chiave.split()
    for elemento in chiave:
        if elemento.isalpha() != True and elemento.islower() != True:
            chiave.remove(elemento)
    chiave2 = ''.join(chiave)
    lista = []
    for el in chiave2:
        lista.extend(el)
    for lettera in lista:
        while lista.count(lettera) > 1:
            lista.remove(lettera)
    chiave_dis = ''.join(lista)
    lista.sort()
    chiave_ord = ''.join(lista)
    lista_t = []
    tupla = ()
    for i,j in zip(chiave_ord,chiave_dis):
        tupla = (i,j)
        lista_t.append(tupla)
    to_code = testo
    lista_fin= []
    for lettera in to_code:
        if lettera == " " :
            lista_fin += " "
        for tupla in lista_t:
            if lettera == tupla[1]:
                l_mod = lettera.replace(lettera,tupla[0])
                lista_fin += l_mod
    testo = "".join(lista_fin)
    return(testo)
