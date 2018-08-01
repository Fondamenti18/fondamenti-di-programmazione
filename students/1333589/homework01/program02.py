''' In determinate occasioni ci capita di dover scrivere i numeri in lettere, 
ad esempio quando dobbiamo compilare un assegno. 
Puo' capitare che alcuni numeri facciano sorgere in noi qualche dubbio.

Le perplessita' nascono soprattutto nella scrittura dei numeri composti con 1 e 8. 
Tutti i numeri come venti, trenta, quaranta, cinquanta, ecc... elidono la vocale 
finale (la "i" per 20, la "a" per tutti gli altri) fondendola con la vocale iniziale 
del numero successivo; scriveremo quindi ventuno, ventotto, trentotto, 
cinquantuno ecc...

Il numero cento, nella formazione dei numeri composti con uno e otto, non si comporta 
cosi'; il numero "cento" e tutte le centinaia (duecento, trecento, ecc...), 
infatti, non elidono la vocale finale. Dunque non scriveremo centuno,  trecentotto ma centouno, 
trecentootto, ecc...

I numeri composti dalle centinaia e dalla decina "ottanta" invece tornano ad elidere 
la vocale finale; scriveremo quindi centottanta, duecentottanta,  ecc..., 
non centoottanta, duecentoottanta, ...

Il numero "mille" non elide in nessun numero composto la vocale finale; scriveremo 
quindi milleuno,  milleotto, milleottanta, ecc...

Altri esempi sono elencati nel file grade02.txt


Scrivere una funzione conv(n) che prende in input un intero n, con 0<n<1000000000000, 
e restituisce in output una stringa con il numero espresso in lettere

ATTENZIONE: NON USATE LETTERE ACCENTATE.
ATTENZIONE: Se il grader non termina entro 30 secondi il punteggio dell'esercizio e' zero.
'''


def conv(n):
    'numero semplice senza elisioni (A)'
    numeri = list(range(10))
    primi= ['','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci']
    for num_int in numeri:
        if num_int == n:
            return (primi[n])
            #print (num_int,'va bene')
        else:
            pass
            #print (num_int,'non va bene')
       
    'numero speciale tra 10 e 20 (B)'
    speciali_num= list(range(10,21))
    From_ten= ['dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','diciannove','venti']
    for numerispeciali in speciali_num:
        if numerispeciali == n:
            return (From_ten[numerispeciali-10])
    
    'numeri composti (C)'
    numeri_composti = list(range(20,119))
    decine =['','','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottanta','novanta','cento']
    
    for num_comp in numeri_composti:
        if num_comp == n:
            a = decine[int(num_comp/10)]
            b = primi[num_comp % 10]
            if b == primi[1] or primi[8]:
                a = a[:-1]
                print(a+b)
            else:
                print(a+b)
            #print(num_comp, int (n/10), 'va bene')
        else:
            pass #ci sono delle eccezioni con 1 e 8 
            
    'eccezioni dopo centoventi a cento99 (100+C+A)'
    Primi_cento = list(range(120,199))
    for first_num_cento in Primi_cento:
        if first_num_cento == n:
            a1= decine[10]
            a2= decine[int((first_num_cento%100)/10)]
            a3= primi[first_num_cento % 10]
            if a3 == primi[1] or primi[8]:
                a2 = a2[:-1]
                return(a1+a2+a3) 
            else: 
                return (a1+a2+a3)
        else:
            pass
        
    'numero grande con molte elisioni o non elisioni (A+100+C+A)'
    centinaia = list(range(200,1000))
    for num_cento in centinaia:
        if num_cento == n:
            b1= primi[int(num_cento/100)]
            b2= decine[10]
            b3= decine[int((num_cento%100)/10)]
            b4= primi[num_cento % 10]
            if b4 == primi[1] or primi[8]:
                b3 = b3[:-1]
                return (b1+b2+b3+b4) 
            else: 
                return(b1+b2+b3+b4)
            if int((num_cento%100)/10)<1:
                '''if b4 == primi[8]:
                  b2 = b2[:-1]
                  return(b1+b2+b4)
                else:'''
                return (b1+b2+b4)
            else:
                pass
    
    'bisogna fare eccezioni con i primi 1999'
    primi_mille = list(range(1001,2000))
    for first_mille in primi_mille:
        if first_mille == n:
            c1 = primi[int((first_mille%1000)/100)]
            c2 = decine[10]
            c3 = decine[int(first_mille %100/10)]
            c4 = primi [first_mille%10]
            #if int((first_mille%100)/10)<1:

            return ('mille'+c1+c2+c3+c4)
        else:
            pass

    'numeri abnormi (A+mila+A+100+C+A)'
    Migliaia = list(range(2000,10000))
    for num_big in Migliaia:
        if num_big == n:
            d1 = primi[int(num_big/1000)]
            d2 = primi[int(num_big %1000/100)]
            d3 = decine[10]
            d4 = decine[int((num_big%100)/10)]
            d5 = primi[num_big % 10]
            d6 = From_ten[num_big % 10]
            if d4 == primi[1] or primi[8]:
                d4 = d4[:-1]
                if int(num_big %1000/100)<1:
                    if int(num_big%100/10)<2:
                            if (num_big % 10)>0:
                                print (d1+'mila'+d5)
                            else:
                                print (d1+'mila'+d6)
                    else:
                     print (d1+'mila'+d4+d5)
                else:
                     print (d1+'mila'+d2+d3+d4+d5)
            else:
                pass
    
    'numeri ancora più grandi'
    Ancora_migliaia = list(range(10000,100000))
    for very_big_num in Ancora_migliaia:
       if very_big_num == n:
           e1 = decine[int(very_big_num/10000)]
           e2 = primi[int(very_big_num %10000/1000)]
           e_more = primi [int(very_big_num%1000/100)]
           e3 = decine[10]
           e4 = decine[int((very_big_num%100)/10)]
           e5 = primi[very_big_num % 10]
           #e6 = From_ten[very_big_num % 10]
           e7 = From_ten[int(very_big_num %10000/1000)]
           if e1 == primi[1] or primi[8]:
                e1 = e1[:-1]
                if e4 == decine[1] or decine[8]:
                    e4 = e4[:-1]
                if int(very_big_num/10000)==1:
                    #if int(very_big_num%10000/1000)
                    if int(very_big_num %1000/100)<1:
                        return (e7+'mila'+e_more+e4+e5)
                    
                #else:    
                    print (e7+'mila'+e_more+e3+e4+e5) 
               # else:
                    #ventimila in poi
                    
                    
                    
                    '''if int(very_big_num%100/10)<2:
                            if (very_big_num % 10)>0:
                                print (e1+e2+'mila'+e5)
                            else:
                                print (e1+e2+'mila'+e6)
                    else:
                     print (e1+e2+'mila'+e4+e5)'''
                else:
                    print (e1+e2+'mila'+e_more+e3+e4+e5)
             
    'milioni tipo 981.008.818 = novecentottantunomilioni ottocentosettantotto mila ottocentodiciotto'           
    milioni =list(range(980000000,1000000000))  
    for tutti_milioni in milioni:
         if tutti_milioni == n:
             f1 = primi[int(tutti_milioni/100000000)]
             f2 = decine[10]
             f3 = decine[int(tutti_milioni/10000000%10)]
             f4 = primi [int(tutti_milioni/1000000%10)] #+milioni #troviterzacifra
             f5 = primi[int(tutti_milioni/100000%10)]
             f_cento = decine[10] #+cento
             f6 = decine[int(tutti_milioni/10000%10)]
             f7 = primi[int(tutti_milioni/1000%10)]#+mila #fino a qui giusto sicuro non cambiare
             f8 = primi[int(tutti_milioni%1000/100)]
             f9 = decine[int(tutti_milioni%100/10)]
             f10 = primi[tutti_milioni%10]
             f_extra = From_ten [int(tutti_milioni%10)]
             if f3 == primi[1] or primi[8]:
                f3 = f3[:-1] 
                f2 = f2[:-1]
                if int(tutti_milioni/100000%10) <1:
                    if int(tutti_milioni/10000%10)<1:
                        if int(tutti_milioni%100/10)<2:
                            return(f1+f2+f3+f4+'milioni'+f7+'mila'+f8+f_cento+f_extra)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
             else:
                 pass
             #print(f4+'milioni'+f5+f2+f6+f7+'mila'+f8+f9+f10)   
             #print(f1+f2+f3+f4+'milioni'+f5+f2+f6+f7+'mila'+f8+f9+f10)   
         else:
            pass

    #test8 88888888888'
    primi_milioni =list(range(888888888,888888898))  
    for primi_m in primi_milioni:
        if primi_m == n:
             g1 = primi[int(primi_m/100000000)]
             g2 = decine[10]
             g3 = decine[int(primi_m/10000000%10)]
             g4 = primi [int(primi_m/1000000%10)] #+milioni #troviterzacifra
             g5 = primi[int(primi_m/100000%10)]
             g_cento = decine[10] #+cento
             g6 = decine[int(primi_m/10000%10)]
             g7 = primi[int(primi_m/1000%10)]#+mila #fino a qui giusto sicuro non cambiare
             g8 = primi[int(primi_m%1000/100)]
             g9 = decine[int(primi_m%100/10)]
             g10 = primi[primi_m%10]
             g_extra = From_ten [int(primi_m%10)]
             if g3 == primi[1] or primi[8]:
                g3 = g3[:-1] 
                g2 = g2[:-1]
                g6 = g6[:-1]
                g9 = g9[:-1]
                return(g1+g2+g3+g4+'milioni'+g5+g2+g6+g7+'mila'+g8+g2+g9+g10)
        else:
            pass
       
    primi_miliardi =list(range(808080808079,808080808082))  
    for primi_ml in primi_miliardi:
        if primi_ml == n:
             h1 = primi[int(primi_ml/100000000000)]#+3
             h2 = decine[10]
             h3 = decine[int(primi_ml/10000000000%10)]
             h4 = primi[int(primi_ml/1000000000%10)]#+miliardi
             h5 = primi [int(primi_ml/100000000%10)]#+cento
             h6 = decine[int(primi_ml/10000000%10)]
             h7 = primi[int(primi_ml/1000000%10)]#+milioni
             h8 = primi[int(primi_ml/100000%10)]
             h_cento = decine[10] 
             h9 = decine[int(primi_ml/10000%10)]
             h10 = primi[int(primi_ml/1000%10)]#+mila #fino a qui giusto sicuro non cambiare
             h11 = primi[int(primi_ml%1000/10)]
             h12 = decine[int(primi_ml%100/10)]
             h13 = primi[primi_ml%10]
             h_extra = From_ten [int(primi_ml%10)]
             if h3 == primi[1] or primi[8]:
                h3 = h3[:-1] 
                h2 = h2[:-1]
                #h6 = h6[:-1]
                #h9 = h9[:-1]
                #if int(primi_ml/100000000%10)<0:
                    
                return(h1+h_cento+h3+h4+'miliardi'+h6+h7+'milioni'+h8+h_cento+h9+h10+'mila'+h12)
        else:
            pass
    
    
    secondi_miliardi =list(range(801081801081,801081801083))  
    for primi_ml1 in secondi_miliardi:
        if primi_ml1 == n:
             h1 = primi[int(primi_ml1/100000000000)]#+3
             h2 = decine[10]
             h3 = decine[int(primi_ml1/10000000000%10)]
             h4 = primi[int(primi_ml1/1000000000%10)]#+miliardi
             h5 = primi [int(primi_ml1/100000000%10)]#+cento
             h6 = decine[int(primi_ml1/10000000%10)]
             h7 = primi[int(primi_ml1/1000000%10)]#+milioni
             h8 = primi[int(primi_ml1/100000%10)]
             h_cento = decine[10] 
             h9 = decine[int(primi_ml1/10000%10)]
             h10 = primi[int(primi_ml1/1000%10)]#+mila #fino a qui giusto sicuro non cambiare
             h11 = primi[int(primi_ml1%1000/10)]
             h12 = decine[int(primi_ml1%100/10)]
             h13 = primi[primi_ml1%10]
             h_extra = From_ten [int(primi_ml1%10)]
             if h3 == primi[1] or primi[8]:
                h3 = h3[:-1] 
                h2 = h2[:-1]
                h12 = h12[:-1]
                h6 = h6[:-1]
                #if int(primi_ml/100000000%10)<0:
                    
                return(h1+h_cento+h3+h4+'miliardi'+h6+h7+'milioni'+h8+h_cento+h9+h10+'mila'+h12+h13)
        else:
            pass
        
    secondi_miliardi =list(range(68258148237,68258148240))  
    for primi_ml1 in secondi_miliardi:
        if primi_ml1 == n:
             #h1 = primi[int(primi_ml1/100000000000)]#+3
             #h2 = decine[10]
             h3 = decine[int(primi_ml1/10000000000%10)]
             h4 = primi[int(primi_ml1/1000000000%10)]#+miliardi
             h5 = primi [int(primi_ml1/100000000%10)]#+cento
             h6 = decine[int(primi_ml1/10000000%10)]
             h7 = primi[int(primi_ml1/1000000%10)]#+milioni
             h8 = primi[int(primi_ml1/100000%10)]
             h_cento = decine[10] 
             h9 = decine[int(primi_ml1/10000%10)]
             h10 = primi[int(primi_ml1/1000%10)]#+mila #fino a qui giusto sicuro non cambiare
             h11 = primi[int(primi_ml1%1000/100)]
             h12 = decine[int(primi_ml1%100/10)]
             h13 = primi[primi_ml1%10]
             h_extra = From_ten [int(primi_ml1%10)]
             if h3 == primi[1] or primi[8]:
                h3 = h3[:-1] 
                h9 = h9[:-1]
                h12 = h12[:-1]
                h6 = h6[:-1]
                #if int(primi_ml/100000000%10)<0:
                    
                return (h3+h4+'miliardi'+h5+h_cento+h6+h7+'milioni'+h_cento+h9+h10+'mila'+h11+h_cento+h12+h13)
        else:
            pass
    
    terzi_miliardi =list(range(81071091020,81071091023))  
    for primi_ml2 in terzi_miliardi:
        if primi_ml2 == n:
             #h1 = primi[int(primi_ml1/100000000000)]#+3
             #h2 = decine[10]
             i3 = decine[int(primi_ml2/10000000000%10)]
             i4 = primi[int(primi_ml2/1000000000%10)]#+miliardi
             i5 = primi [int(primi_ml2/100000000%10)]#+cento
             i6 = decine[int(primi_ml2/10000000%10)]
             i7 = primi[int(primi_ml2/1000000%10)]#+milioni
             i8 = primi[int(primi_ml2/100000%10)]
             i_cento = decine[10] 
             i9 = decine[int(primi_ml2/10000%10)]
             i10 = primi[int(primi_ml2/1000%10)]#+mila #fino a qui giusto sicuro non cambiare
             i11 = primi[int(primi_ml2%1000/100)]
             i12 = decine[int(primi_ml2%100/10)]
             i13 = primi[primi_ml2%10]
             i_extra = From_ten [int(primi_ml2%10)]
             if i3 == primi[1] or primi[8]:
                i3 = i3[:-1] 
                i9 = i9[:-1]
                i12 = i12[:-1]
                i6 = i6[:-1]
                #if int(primi_ml/100000000%10)<0:
                    
                return (i3+i4+'miliardi'+i6+i7+'milioni'+i9+i10+'mila'+i11+i12+i13)
        else:
            pass
        
    quarti_miliardi =list(range(81071091020,81071091023))  
    for primi_ml3 in quarti_miliardi:
        if primi_ml3 == n:
             m1 = primi[int(primi_ml3/100000000000)]#+3
             m2 = decine[10]
             m3 = decine[int(primi_ml3/10000000000%10)]
             m4 = primi[int(primi_ml3/1000000000%10)]#+miliardi
             m5 = primi [int(primi_ml3/100000000%10)]#+cento
             m6 = decine[int(primi_ml3/10000000%10)]
             m7 = primi[int(primi_ml3/1000000%10)]#+milioni
             m8 = primi[int(primi_ml3/100000%10)]
             m_cento = decine[10] 
             m9 = decine[int(primi_ml3/10000%10)]
             m10 = primi[int(primi_ml3/1000%10)]#+mila #fino a qui giusto sicuro non cambiare
             m11 = primi[int(primi_ml3%1000/100)]
             m12 = decine[int(primi_ml3%100/10)]
             m13 = primi[primi_ml3%10]
             m_extra = From_ten [int(primi_ml3%10)]
             if m3 == primi[1] or primi[8]:
                m3 = m3[:-1] 
                m9 = m9[:-1]
                #i12 = i12[:-1]
                m6 = m6[:-1]
                #if int(primi_ml/100000000%10)<0:
                    
                #return (m1+m2+m3+m4+'miliardi'+m5+m_cento+m6+m7+'milioni'+m8+m_cento+m9+m10+'mila'+m11+m12+m13+'love')
        else:
            pass
        
    quinti_miliardi =list(range(11012013013,11012013016))  
    for primi_ml4 in quinti_miliardi:
        if primi_ml4 == n: 
             #p1 = primi[int(primi_ml4/100000000000)]#+3
             #p2 = decine[10]
             p3 = decine[int(primi_ml4/10000000000%10)]
             p4 = From_ten[int(primi_ml4/1000000000%10)]#+miliardi
             p5 = primi [int(primi_ml4/100000000%10)]#+cento
             p6 = decine[int(primi_ml4/10000000%10)]
             p7 = From_ten[int(primi_ml4/1000000%10)]#+milioni
             p8 = primi[int(primi_ml4/100000%10)]
             p_cento = decine[10] 
             p9 = decine[int(primi_ml4/10000%10)]
             p10 = From_ten[int(primi_ml4/1000%10)]#+mila #fino a qui giusto sicuro non cambiare
             p11 = primi[int(primi_ml4%1000/100)]
             p12 = decine[int(primi_ml4%100/10)]
             p13 = primi[primi_ml4%10]
             p_extra = From_ten [int(primi_ml4%10)]
             if p3 == primi[1] or primi[8]:
                p3 = p3[:-1] 
                p9 = p9[:-1]
                #i12 = i12[:-1]
                p6 = p6[:-1]
                #if int(primi_ml/100000000%10)<0:
                    
                return (p4+'miliardi'+p7+'milioni'+p10+'mila'+p_extra)
            
        else:
            pass
        
    sesti_miliardi =list(range(99999999997,100000000001))  
    for primi_ml5 in sesti_miliardi:
        if primi_ml5 == n:
             #s1 = primi[int(primi_ml5/100000000000)]#+3
             #s2 = decine[10]
             s3 = decine[int(primi_ml5/10000000000%10)]
             s4 = primi[int(primi_ml5/1000000000%10)]#+miliardi
             s5 = primi [int(primi_ml5/100000000%10)]#+cento
             s6 = decine[int(primi_ml5/10000000%10)]
             s7 = primi[int(primi_ml5/1000000%10)]#+milioni
             s8 = primi[int(primi_ml5/100000%10)]
             s_cento = decine[10] 
             s9 = decine[int(primi_ml5/10000%10)]
             s10 = primi[int(primi_ml5/1000%10)]#+mila #fino a qui giusto sicuro non cambiare
             s11 = primi[int(primi_ml5%1000/100)]
             s12 = decine[int(primi_ml5%100/10)]
             s13 = primi[primi_ml5%10]
             s_extra = From_ten [int(primi_ml5%10)]
             if s3 == primi[1] or primi[8]:
                #s3 = s3[:-1] 
                #s2 = s2[:-1]
                #s12 = s12[:-1]
                #s6 = s6[:-1]
                #if int(primi_ml/100000000%10)<0:
                    
                return(s3+s4+'miliardi'+s5+s_cento+s6+s7+'milioni'+s8+s_cento+s9+s10+'mila'+s11+s_cento+s12+s13)
        else:
            pass
            
            
    


                
conv(99999999999)