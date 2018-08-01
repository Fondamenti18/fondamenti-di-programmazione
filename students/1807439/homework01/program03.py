
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
def disordinamento(stringa):
    '''inserire qui la vostra implementazione'''
    i=len(stringa)-1
    seq_dis=[]
    stringa_dis=''
    while i>=0:
        if 'a'<=stringa[i]<='z':
            seq_dis=[stringa[i]]+seq_dis
            if stringa[i] in seq_dis[1: ]:
                seq_dis.remove(stringa[i])
        i-=1  
    return stringa_dis.join(seq_dis)
def ordinamento(stringa):
    s_ord=''
    a=disordinamento(stringa)
    return s_ord.join(sorted(a))
def coppie(s1):
    d={}
    i=0
    s=disordinamento(s1)
    ss=ordinamento(s1)
    while i<len(s):                 #slaim ailms
        d[ss[i]]=s[i]
        i+=1
    return d
def codifica(chiave,testo):
    d=coppie(chiave)
    t_mod=''
    for x in testo:
        if x not in d.keys():
            t_mod+=x
        else:
            t_mod+=d[x]
    return t_mod
def coppie_reverse(s1):
    d={}
    i=0
    s=disordinamento(s1)
    ss=ordinamento(s1)
    while i<len(s):                 #slaim ailms
        d[s[i]]=ss[i]
        i+=1
    return d
def decodifica(chiave, testo):
    d=coppie_reverse(chiave)
    t_mod=''
    for x in testo:
        if x not in d.keys():
            t_mod+=x
        else:
            t_mod+=d[x]
    return t_mod
    

