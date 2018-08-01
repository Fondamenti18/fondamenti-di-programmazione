from math import sqrt
def modi(ls,k):
    '''Per ogni elemento della lista, controlla se i suoi divisori propri siano quanti richiesti,
    altrimenti l'elemento viene eliminato dalla lista. In seguito ritorna una lista formata dai soli elementi primi della lista iniziale'''
    num_primi=[]
    lista_sottraendo=[] 
    for elemento in ls:
        div_propri=0   
        primo=True
        analizza_lista(elemento,k,div_propri,primo,num_primi,lista_sottraendo)
    for elemento in lista_sottraendo:ls.remove(elemento)
    return num_primi

def analizza_lista(elemento,k,div_propri,primo,num_primi,lista_sottraendo):
    for divisore in range(2,int(sqrt(elemento))+2):
        if elemento%divisore == 0:
            div_propri+=1
            primo=False
            if not divisore == elemento/divisore: div_propri+=1
            if div_propri>k: break
    genera_liste(elemento,k,div_propri,primo,num_primi,lista_sottraendo)
    
def genera_liste(elemento,k,div_propri,primo,num_primi,lista_sottraendo):
    if not div_propri == k:lista_sottraendo.append(elemento)        
    if primo ==True:num_primi.append(elemento)