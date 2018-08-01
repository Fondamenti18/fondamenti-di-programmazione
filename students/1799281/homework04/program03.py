

from  my_html import HTMLNode, fparse
import re
stringa=''
stringa2=''      #flags 
c=0
canc=0
def divisione_stringa(selettore):
    global stringa
    global stringa2
    stringa=''
    stringa2=''
    temp=''
    simbolo=''
    for i in selettore:          #ancora non funziona con più elementi concatenati
        if temp=='' and (i=='='or i==' ') :
            temp=i
        if not i.isalpha() and not i.isnumeric():
            if simbolo!='@' and simbolo!='>' and simbolo !='#' and simbolo !='.':          
                simbolo=i
        else:
            if temp!='=' and temp!=' ':
                    stringa+=(i)
            elif temp=='=' or temp==' ':
                
                if i.isalpha() or i.isnumeric():
                    stringa2+=(i)
    return(simbolo)
    
def conta_nodi(fileIn, selettore):
    global stringa
    global stringa2
    global c
    d= fparse(fileIn)
    simbolo=''
    stringa=''
    stringa2=''
    c=0
    simbolo=divisione_stringa(selettore)
    print(stringa,stringa2,simbolo)
    altro(d,simbolo)
    return(c)
def altro(d,simbolo):
    global c
    global tempo
    global canc
    canc=0
    for i in d.content:
        if not i.istext():
            if simbolo=='#':           #ricerca id
                if stringa in i.attr.values() and 'id' in i.attr.keys():
                        c=c+1
            elif simbolo=='.':         #ricerca delle classi
                if 'class' in i.attr.keys():
                    if stringa in i.attr['class']:
                            c=c+1
            elif simbolo=='':       #ricerca di semplici tag
                if stringa in i.tag:
          
                    c+=1
            elif simbolo=='@':     #ricerca attributi
                if stringa2 in i.attr.values() and stringa in i.attr.keys():

                        c=c+1
            elif simbolo==' ':     #avo 
                if stringa in i.tag and len(stringa)==len(i.tag):
                    scorri(i,0)
                   # break
            elif simbolo=='>':
                              #figlio
              if stringa in i.tag and len(stringa)==len(i.tag):
                  scorri(i,1)
                  break
     
            altro(i,simbolo)
    
def scorri(i,cont):
    global c
    for h in i.content:
        if not h.istext():
          
           if cont!=0:            #padre figlio
               if stringa2 not in h.tag :
                   return()
               else:
                    if canc==0:
                        c=c+1
                    else:
                        del h
                    return()
           if stringa2 in h.tag and len(stringa2)==len(h.tag):       #discendente, avo
               if canc==0:
       
                    c=c+1
               else:
                   del h
                   break
           scorri(h,cont)
    


def elimina_nodi(fileIn, selettore, fileOut):
    global c
    global canc
    canc=1
    c=0
    d=fparse(fileIn)
    simbolo=divisione_stringa(selettore)
    altro(d,simbolo)
    c=d.to_string()
    f=open(fileOut,'w')
    f.write(c)
    f.close()
    
   # '''Elimina dall'albero tutti i nodi che soddisfano il selettore CSS (compreso il loro contenuto)'''
    #Inserite qui il vostro codice

def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    #'''Modifica tutti i nodi dell'albero che soddisfano il selettore CSS'''
    d=fparse(fileIn)
    simbolo=divisione_stringa(selettore)
    #print(simbolo)
    #print(stringa,stringa2)
    cambia(d,simbolo,chiave,valore)
    c=d.to_string()
    f=open(fileOut,'w')
    f.write(c)
    f.close()
def cambia(d,simbolo,chiave,valore):
    global c
    global tempo
    global canc
    canc=0
    for i in d.content:
        if not i.istext():
           # print(i.tag)
            if simbolo=='#':           #ricerca id
                if stringa in i.attr.values() and 'id' in i.attr.keys():
                        c=c+1
            elif simbolo=='.':         #ricerca delle classi
                if 'class' in i.attr.keys():
                    if stringa in i.attr['class']:
                            c=c+1
            elif simbolo=='':       #ricerca di semplici tag
                if stringa in i.tag:
          
                    c+=1
            elif simbolo=='@':     #ricerca attributi
                if stringa2 in i.attr.values() and stringa in i.attr.keys():

                        c=c+1
            elif simbolo==' ':     #avo 
                if stringa in i.tag and len(stringa)==len(i.tag):
                    #print("ejaweh")
                    sco(i,chiave,valore)
                   # break
            elif simbolo=='>':
                              #figlio
              if stringa in i.tag and len(stringa)==len(i.tag):
                  sco(i,chiave,valore)
                  #break
     
            cambia(i,simbolo,chiave,valore)
def sco(i,chiave,valore):
    global c
    for h in i.content:
        if not h.istext():
               # print(h.tag,h.attr)
                  #padre figlio
                #if stringa2 not in h.tag :
                   #return()
                if stringa2 in h.tag and len(stringa2)==len(h.tag):       #discendente, avo
                   
                   h.attr[chiave]=valore
                   #print("wewe",h.attr)
                
                sco(h,chiave,valore)
    























