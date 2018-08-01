def decod(pfile, codice):
   ins=set()
   if codice.isdigit() == True :
       with open(pfile, encoding='utf-8') as vcb:
           linee=vcb.readlines()
           for linea in linee:
               linea=linea.lower()
               linea=linea.replace('\n', '')
               if len(linea)==len(codice):
                   for x in range(len(linea)):
                       insert=False
                       occ=linea.count(linea[x])
                       occ2=codice.count(codice[x])  
                       if (occ==1 and occ2>=2) or (occ>=2 and occ2==1):
                           insert=False
                           break
                       if occ>=2 and occ2>=2:
                           cont=0
                           cont2=0
                           for y in range(len(linea)):
                               if cont==cont2:
                                   if linea[y]==linea[x]:
                                       cont+=1
                                   if codice[y]==codice[x]:
                                       cont2+=1
                                   if cont!=cont2:
                                       insert=False
                                       break
                           if cont!=cont2:
                               insert=False
                               break
                           else:
                               insert=True
                       else:
                           insert=True
                   if insert==True:
                       ins.add(linea)
   return ins

