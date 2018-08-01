

def post(fposts,insieme):
     op_file= open(fposts,"r")
     tst_file='a'
     post='<POST>'
     codes=[]
     lisins=list(insieme)
     insiem=[]
     for i in lisins:
         insiem+=[i.lower()]
     while tst_file!='':
         testo=[]
         parole=''
         tst_file=op_file.readline()
         if(post in tst_file):
             codice=[]
             for z in tst_file:
                 if (z.isnumeric()):
                     codice+=[z]
             codice=''.join(codice)
         for i in tst_file:
             if i.isalpha()==True:
                testo+=[i]
             if i.isalpha()!=True:
                testo+=[' '] 
         parole=''.join(testo)
         parole=parole.lower()
         parole=parole.split()
         for s in insiem:
             if(s in parole):
                    codes+=[codice]
     codices=set(codes)
     return(codices)
     

