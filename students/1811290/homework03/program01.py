import png

def quadrato(filename,c):
    '''Implementare qui la funzione'''
    img=load(filename)#leggo l'immagine
    quadratoold=0
    color_find=c
    pos_riga=0
    colore_pixel_qua_ipotetico=0
    for riga in img:#leggo la colonna orizzontale
        pos_pixel=0
        for pixel in riga:#leggo i pixel della colonna
            if pixel==color_find:
                y_inizio_quadrato_ipotetico=pos_riga #coordinate x iniziali del quadrato da trovare
                x_inizio_quadrato_ipotetico=pos_pixel #coordinate y iniziali del quadrato da trovare
#mi deve restituire se sia un quadrato o meno
                analisi=analisi_coordinate(img,color_find,x_inizio_quadrato_ipotetico,y_inizio_quadrato_ipotetico)
                if analisi!=False:
                    quadratonew=(analisi[0],analisi[1])
                    if quadratoold==0:#dire che se il quadrato è una variabile, allora sostituire il quadrato vecchio con quello  nuovo, senno tenere il quadrato vecchio
                        quadratoold=quadratonew
                    if quadratonew[0]>quadratoold[0]:#mi prende sia il piu  in alto al sinistra che il piu grande
                        quadratoold=quadratonew
            pos_pixel+=1
        pos_riga+=1
    #print('ultimo',quadratoold)
    return quadratoold

def analisi_coordinate(img,color_find,x_inizio_quadrato_ipotetico,y_inizio_quadrato_ipotetico):
    #analisi larghezza
    larghezza=analisi_larghezza(img,color_find,x_inizio_quadrato_ipotetico,y_inizio_quadrato_ipotetico)
    #analisi altezza e la possibilita della forma del quadrato
    altezza_e_quadrato=analisi_altezza_e_quadrato(img,color_find,x_inizio_quadrato_ipotetico,y_inizio_quadrato_ipotetico,larghezza)
    altezza=altezza_e_quadrato[1]
    possibilitaquadrato=altezza_e_quadrato[0]
    #analisi interna dei pixel colorati
    pixeltutticoloratisino=pixel_tutti_colorati_sino(img,color_find,x_inizio_quadrato_ipotetico,y_inizio_quadrato_ipotetico,larghezza,altezza)
        
    #quadratosino=quadrato_sino(larghezza,altezza)
    if possibilitaquadrato==True and pixeltutticoloratisino==True:
        oggetto=larghezza,(x_inizio_quadrato_ipotetico,y_inizio_quadrato_ipotetico)
        return oggetto
    else:
        return False



def analisi_larghezza(img,color_find,x_inizio_quadrato_ipotetico,y_inizio_quadrato_ipotetico):
    pos_riga=y_inizio_quadrato_ipotetico
    pos_pixel=x_inizio_quadrato_ipotetico
    larghezza=0
#conto la larghezza
    for k1 in range(pos_pixel,len(img[pos_riga])):
        pixel=img[pos_riga][k1]
        if pixel==color_find:
            larghezza+=1
        elif pixel!=color_find: #stoppa conteggio dei pixel verso destra
            break            
        pos_pixel+=1
    return larghezza

    
def analisi_altezza_e_quadrato(img,color_find,x_inizio_quadrato_ipotetico,y_inizio_quadrato_ipotetico,larghezza):
    pos_riga=y_inizio_quadrato_ipotetico
    pos_pixel=x_inizio_quadrato_ipotetico
    altezza=0
    
    for k in range(pos_riga,len(img)):
        pixel=img[k][pos_pixel]
        if pixel!=color_find: #stoppa conteggio delle colonne verso il basso
            break 
        else:
            altezza+=1
            
    if altezza>=larghezza:
        altezza=larghezza
        oggetto_true=(True,altezza)
        return oggetto_true
    else:
        oggetto_false=(False,altezza)
        return oggetto_false

def pixel_tutti_colorati_sino(img,color_find,x_inizio_quadrato_ipotetico,y_inizio_quadrato_ipotetico,larghezza,altezza):
    larghezza_passata=larghezza
    pos_riga=y_inizio_quadrato_ipotetico
    larghezza=0
    for k in range(pos_riga,(pos_riga+altezza)):
        pos_pixel=x_inizio_quadrato_ipotetico
        nuova_larghezza=0
        if img[k][pos_pixel]!=color_find: #stoppa conteggio delle colonne verso il basso
            break 
        for k1 in range(pos_pixel,(pos_pixel+larghezza_passata)):
            pixel=img[k][k1]
            if pixel==color_find:
                nuova_larghezza+=1
            elif pixel!=color_find: #stoppa conteggio dei pixel verso destra
                break
        if larghezza==0:
            larghezza=nuova_larghezza
        elif larghezza!=nuova_larghezza:
            return False
    return True

def load(filename):
    """ Carica la immagine PNG dal file fname.
        Torna una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori.
        Ciascun colore è un intero tra 0 e 255 compresi.
    """
    with open(filename, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = []
        for line in png_img:
            l = []
            for i in range(0, len(line), 3):
                l+=[(line[i], line[i+1], line[i+2])]
            img+=[l]
        return img

#quadrato('Ist4.png',(0,0,255))
