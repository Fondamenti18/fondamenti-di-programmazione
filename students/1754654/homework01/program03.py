
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
    alphabet_dictionary = {'f': '', 'z': '', 'r': '', 'e': '', 'd': '', 'b': '', 'x': '', 'q': '', 'c': '', 's': '', 'm': '', 'u': '', 'o': '', 'j': '', 'h': '', 'y': '', 'v': '', 'g': '', 'a': '', 'p': '', 'n': '', 'l': '', 'i': '', 'k': '', 't': '', 'w': ''}
    lst = [_ for _ in list(chiave) if _ >= 'a' and _ <= 'z']

    reversed_lst = []
    for _ in reversed(lst):
        if _ not in reversed_lst:
            reversed_lst.append(_)

    app_lst = [i_ for i_ in reversed(reversed_lst)]

    order_sequence_char = sorted(app_lst)
    for index, letter in enumerate(order_sequence_char):
        alphabet_dictionary[letter] = app_lst[index]

    testo_app = list(testo)
    for index,characters in enumerate(testo_app):
        if 'a' <= characters <= 'z' and alphabet_dictionary[characters] != '' and characters in alphabet_dictionary:
            testo_app[index] = alphabet_dictionary[characters]

    crypto_text = ''.join(testo_app)

    return crypto_text


def decodifica(chiave, testo):
    dictionary = {'f': '', 'z': '', 'r': '', 'e': '', 'd': '', 'b': '', 'x': '', 'q': '', 'c': '', 's': '', 'm': '', 'u': '', 'o': '', 'j': '', 'h': '', 'y': '', 'v': '', 'g': '', 'a': '', 'p': '', 'n': '', 'l': '', 'i': '', 'k': '', 't': '', 'w': ''}
    lst_ = [ _ for _ in list(chiave) if _ >= 'a' and _ <= 'z']

    rlst_ = []
    for letter in reversed(lst_):
        if letter not in rlst_:
            rlst_.append(letter)

    chr_in_list = [i_ for i_ in reversed(rlst_)]
    sorted_key = sorted(chr_in_list)

    for num , item in enumerate(sorted_key):
        dictionary[item] = chr_in_list[num]

    dictionary2 = {}
    for key_ , value_ in dictionary.items():
        if value_ != '':
            dictionary2[value_] = key_

    text_in_list = list(testo)
    for index_of, character in enumerate(text_in_list):
        if 'a' <= character <= 'z' and character in dictionary2:
            text_in_list[index_of] = dictionary2[character]

    decrypto_text = ''.join(text_in_list)
    return decrypto_text


if __name__ == '__main__':
    print(codifica('Monti Spognardi e Sterbini','Sterbini Spognardi e Monti'))
