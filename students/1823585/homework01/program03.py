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
    k = Delete_chrs(chiave,testo)
    Cript = Cript_K(chiave,testo)
    return Cript 

def decodifica(chiave,testo):
    k = Delete_chrs(chiave,testo)
    Testo_decript = Decriptamento_testo(chiave, testo)
    return Testo_decript

def Decriptamento_testo(chiave, testo):   
    K_Ordinata = sorted(Delete_chrs(chiave, testo))
    K_Disordin = Delete_chrs(chiave, testo) 
    Decript = "" 
    Diz = dict(zip(K_Ordinata,K_Disordin))
    for i in testo: 
        if (i in Diz): 
            Decript += Diz[i]
        else: Decript += i 
    return Decript

def Cript_K(chiave,testo):
    K_Ordinata = sorted(Delete_chrs(chiave,testo))
    K_Disordin = Delete_chrs(chiave, testo)
    
   
    Cript = ""
    Diz = dict(zip(K_Ordinata,K_Disordin))
    for i in testo: 
        if (i in Diz): 
            Cript += Diz[i+1]
        else: Cript += i
    return Cript 
def Delete_chrs(chiave,testo): 
    alfabeto_min = {0:'a',1:'b',2:'c',3:'d',\
                    4:'e',5:'f',6:'g',7:'h',\
                    8:'i',9:'j',10:'k',11:'l',\
                    12:'m',13:'n',14:'o',15:'p',\
                    16:'q',17:'r',18:'s',19:'t',\
                    20:'u',21:'v',22:'w',23:'x', \
                    24:'y',25:'z'}
    Ls_k = list(chiave)
    Min_di_Ls_k = []   
    for c in range(len(Ls_k)):
        for r in range(len(alfabeto_min)):          
            if Ls_k[c] == alfabeto_min[r]: Min_di_Ls_k += Ls_k[c]     
    for r in Min_di_Ls_k[:]:      
        Sup = Min_di_Ls_k.count(r)       
        if Sup > 1:           
            Pos_Init = Min_di_Ls_k.index(r)
            del Min_di_Ls_k[Pos_Init]
    return Min_di_Ls_k
