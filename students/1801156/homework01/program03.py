
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

dizionario = {}

def controllo_lettere(chiave):
    '''controllare se le lettere sono contenute tra l'intervallo a:z'''
    lista_chiave = [x for x in list(chiave) if x >= 'a' and x <= 'z']
    return lista_chiave

def elimina_occorrenze(lista_chiave):
    '''eliminare tutte le lettere uguali tranne le ultime occorrenze'''
    lista = []
    for x in range(len(lista_chiave)-1, -1, -1):
        if lista_chiave[x] not in lista:
            lista.append(lista_chiave[x])
    return lista[::-1]
    
def controllo_uguale(lista_testo, y, chiave_in, chiave_out):
    '''controllare se ci sono caratteri uguali tra il testo e la chiave in input'''
    if lista_testo[y] in chiave_in:
        for x in range(0, len(chiave_in)):
            if lista_testo[y] == chiave_in[x]:
                lista_testo[y] = chiave_out[x]
                return 0

def modifica_testo(chiave_in, chiave_out, testo):
    '''data una chiave in input, modificare il testo tramite la chiave di output'''
    lista_testo = list(testo)
    for y in range(0, len(lista_testo)):
        controllo_uguale(lista_testo, y, chiave_in, chiave_out)
    return ''.join(lista_testo)

def chiave_dis_ord(chiave):
    '''ottenere la chiave disordinata e la chiave ordinata'''
    chiave_disordinata = elimina_occorrenze(controllo_lettere(chiave))
    chiave_ordinata = sorted(chiave_disordinata)
    return chiave_disordinata, chiave_ordinata

def codifica(chiave, testo):
    '''codifica di un testo data una chiave'''
    chiave_disordinata, chiave_ordinata = chiave_dis_ord(chiave)
    return modifica_testo(chiave_ordinata, chiave_disordinata, testo)
    
def decodifica(chiave, testo):
    '''decodifica di un testo data una chiave'''
    chiave_disordinata, chiave_ordinata = chiave_dis_ord(chiave)
    return modifica_testo(chiave_disordinata, chiave_ordinata, testo)