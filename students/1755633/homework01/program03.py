def  codifica(s,sdc): #definizione funzione decodifica
     ##################dichiarazione e inizializzazione delle variabili
     s=s+'!'
     c=0
     sf=[]  
     sfo=[]
     lsdc=[]
     lista=[]
     stra=''
     ################################
     while(s[c]!=s[-1]):         

          if(s[c]>='a')and(s[c]<='z'):       #escludiamo ogni carattere che non corrisponde ad una lettera del alfabeto(escluse maiuscole)                 
             sf.append(s[c])                 #aggiungiamo alla lista sf il carattere filtrato
   
             for i in range(0,(len(sf)-1)):   
               
                 if sf[i]==sf[len(sf)-1]:    #eliminiamo le occorenze di ciascun carattere, lasciando l ultima
                    sf.remove(sf[i])                  
                    break                    
          c=c+1
             
     #diso=sf           
     sfo=sorted(sf)   #ordiniamo la chiave lavorata
     #sfo=ordi          
    
     for i in range (0,len(sdc)):   #"string to list", testo in chiaro
          lsdc.append(sdc[i])
      
     fine=(len(lsdc))     #calcolato l'ultimo indice della lista lsdc list from string, testo in chiaro
     cont=0
     i=0

     while True:                  
          y=0         
          ce=False

          for y in range(0,len(sf)):     
            
             if lsdc[i]==sfo[y]:#ricerca di ciascun carattere del testo nella chiave ordinata e aggiunto a lista  il carattere della chiave lavorata "associata"
                ce=True               
                lista.append(sf[y])         

          if ce==False:         
             stra=lsdc[i]
       
             if stra.isspace():  #gestione degli spazi
                lista.append(' ')
             
             else:              
                lista.append(lsdc[i]) #lascio nel testo crittografato i caratteri che non sono presenti nella chiave ordinata
              
          cont=cont+1         
          i=i+1
        
          if cont==(fine):   #esco se il contatore è arrivato alla fine, se si scorre tutta la lista lsdc from string, testo in chiaro
             break
     f=0
     strp=''
    
     while True:            
        
          if(f==len(lista)):          
             break
         
          strp=strp+lista[f]             #list to string per il ritorno di una stringa
          f=f+1

     return strp



def  decodifica(s,sdc):  #definizione funzione decodifica
     ##################dichiarazione e inizializzazione delle variabili
     s=s+'!'
     c=0
     sf=[]     
     sfo=[]
     lsdc=[]
     lista=[]
     stra=''        
     ################################
     while True: 
          
          if(s[c]>='a')and(s[c]<='z'):          #escludiamo ogni carattere che non corrisponde ad una lettera del alfabeto(escluse maiuscole)              
             sf.append(s[c])                     #aggiungiamo alla lista sf il carattere filtrato
            
             for i in range(0,(len(sf)-1)): 
                
                 if sf[i]==sf[len(sf)-1]:         #eliminiamo le occorenze di ciascun carattere, lasciando l ultima
                    sf.remove(sf[i])                
                    break
                    
          if (s[c]==s[-1]):
             break 
                 
          c=c+1

     #diso=sf           
     sfo=sorted(sf)   #ordiniamo la chiave lavorata
     #sfo=ordi        

     for i in range (0,len(sdc)):   #"string to list", testo non chiaro
          lsdc.append(sdc[i])

 
     fine=(len(lsdc))           #calcolato l'ultimo indice della lista lsdc list from string, testo non in chiaro
     cont=0
     i=0
     
     while True:         
          y=0        
          ce=False
          for y in range(0,len(sf)):
            
             if lsdc[i]==sf[y]:    #ricerca di ciascun carattere del testo nella chiave lavorata e aggiunto a lista  il carattere della chiave lavorata "associata"
                ce=True               
                lista.append(sfo[y])

          if ce==False:
             stra=lsdc[i]
       
             if stra.isspace():    #gestione degli spazi
                lista.append(' ')    
              
             else:               
                lista.append(lsdc[i])  #lascio nel testo crittografato i caratteri che non sono presenti nella chiave ordinata
           
          cont=cont+1      
          i=i+1         
         
          if cont==(fine):   #esco se il contatore è arrivato alla fine, se si scorre tutta la lista lsdc from string, testo in chiaro
             break

     f=0
     strp=''
    
     while True:
          
          if(f==len(lista)):            
             break
         
          strp=strp+lista[f]    #list to string per il ritorno di una stringa
          f=f+1

     return strp

