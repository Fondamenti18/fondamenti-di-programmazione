

def decod(pfile, codice):
   lung=len(codice)+1
   conta_codice={}
   for num in codice:
       conta_codice[num]=conta_codice.get(num,0)+1
   lcodice=len(conta_codice)
   ls_codice=list(codice)
   correct=set()
   with open(pfile) as doc:
       for line in doc:
           if len(line)==lung:
               correct.add(line.rstrip('\n'))
       corr2=set()
       for i in correct:
           conta_lettere={}
           for lettera in i:
               conta_lettere[lettera]=conta_lettere.get(lettera,0)+1
           li=len(conta_lettere)
           if len(conta_codice)==len(conta_lettere):
                   corr2.add(i)
           else:
               pass
       result=set()
       for word in corr2:
           ls_word=list(word)
           dic={c:v for c,v in zip(ls_codice,ls_word)}
           word_test=[]
           for n in ls_codice:
               word_test.append(dic.get(n))
           a=''.join(word_test)
           if a == word:
               result.add(word)
           else:
               pass
       return result            
               
       
       
       
      
                  
       
        
        
        
    
    
    





