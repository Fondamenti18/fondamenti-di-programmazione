'''
Un robottino deve muoversi su di una scacchiera di 15 x 15 celle  con celle bianche e nere  ciascuna di lato 40. 
Per rendere il percorso accidentato alcune delle celle della scacchiera contengono ostacoli (queste celle sono  colorate di rosso).

Un  esempio di scacchiera con ostacoli e' dato  dall'immagine 'I1.png'

Per caricare e salvare immagini PNG usate le funzioni load e save che abbiamo preparato nel modulo immagini.py .

Al'inizio il robottino e' posizionato sulla prima cella in altro a sinistra della scacchiera ed e' rivolto verso destra (x crescente). 
Ad ogni step tenta di ragiungere una delle celle adiacenti in orizzontale o verticale. 
Le regole di movimento del robottino sono le seguenti: 
- al generico step, si sposta sulla cella che ha di fronte se questa e' libera da ostacoli e non ci e' gia transitato in passato. 
- se invece la cella risulta occupata o e' una cella su cui ha gia transitato, ruota di 90 gradi in senso orario ed aspetta lo step successivo. 
- dopo aver ruotato  di 360 gradi senza essere riuscito a spostarsi si ferma. 

Progettare la funzione  percorso(fname, fname1) che presi in input:
- il percorso di un file (fname) contenente l'immagine in formato .png di una scacchiera con ostacoli
- il percorso di un file di tipo .png (fname1) da creare
legge l'immagine della scacchiera in fname, colora di verde le celle della scacchiera percorse dal robottino prima di fermarsi, 
colora di blu la cella in cui il robottino si ferma e registra l'immagine ricolorata nel file fname1. 
Inoltre restituisce una stringa dove in sequanza sono codificati i passi effettuati dal robottino prima di fermarsi. 
La codifica e' a seguente: 
    '0' per un passo verso destra (x crescenti)
    '1' per un passo verso il basso (y crescenti)
    '2' per un passo verso sinistra (x decrescenti)
    '3' per un passo verso l'alto (y decrescenti)

Si puo' assumere che la cella in alto a sinistra sia priva di ostacoli. 

Per esempi di scacchiere con ostacoli e relativi cammini  vedere il file grade02.txt 

NOTA: il timeout per la esecuzione del grader e' fissato a 10*N secondi (per N test eseguiti dal grader)
'''

from immagini import load
from immagini import save
import immagini
from IPython.display import Image

def cammino(fname,  fname1):
    f=immagini.load(fname)
    out=f
    rosso=(255,0,0)
    verde=(0,255,0)
    blu=(0,0,255)
    bianco=(255,255,255)
    nero=(0,0,0)
    draw_rect(out,0,0,40,40,(0,255,0))
    l=len(f[0])
    h=len(f)
    xL=0
    yL=40
    back=''
    direct = '0'
    end='0'
    controllo=' '
    
    while True:
        
        
                
        if direct == '0':
            
            out, xL, yL, direct, end = check0(out,xL,yL,rosso,verde,blu,end,l,h)
            
            pass
            
        if direct == '1':
            
            out, xL, yL, direct, end = check1(out,xL,yL,rosso,verde,blu,end,l,h)
            
            pass
        
        if direct == '2':
            
            out, xL, yL, direct, end = check2(out,xL,yL,rosso,verde,blu,end,l,h)
            
            pass
        
        if direct == '3':
            
            out, xL, yL, direct, end = check3(out,xL,yL,rosso,verde,blu,end,l,h)
            
            pass
            
            
            
         
        if direct == '':
            immagini.save(out,fname1)
            return end
        
    
        
        
def check0(out,xL,yL,rosso,verde,blu,end,l,h):
    draw_rect(out,yL,xL,40,40,verde)
    if yL + 40 >= l:
        if (xL + 40 >= 0) and out[xL+40][yL] != (rosso or verde):
            direct = '1'
            xL = xL + 40
            end += direct
            return out,xL,yL,direct,end
        else:
            if(xL-40 > 0) and out[xL-40][yL] != (rosso or verde):
                direct = '3'
                xl = xL -40
                
                return out,xL,yL,direct,end
            else:
                direct=''
                draw_rect(out,yL,xL,40,40,blu)
                end += direct
                return out,xL,yL,direct,end
            
    else:
        if (out[xL][yL+40] == rosso) or (out[xL][yL+40] == verde):
            if (xL+40 >= h) or (out[xL+40][yL] == rosso) or (out[xL+40][yL] == verde):
                if (xL-40 < 0) or (out[xL-40][yL] == rosso) or (out[xL-40][yL] == verde):
                    draw_rect(out,yL,xL,40,40,blu)
                    direct=''
                    end += direct
                    return out,xL,yL,direct,end
                else:
                    direct = '3'
                    xL=xL-40
                    end += direct
                    return out,xL,yL,direct,end
            else:
                direct = '1'
                xL=xL+40
                end += direct
                return out,xL,yL,direct,end
        else:
            direct='0'
            yL=yL+40
            end += direct
            return out,xL,yL,direct,end
                                
def check1(out,xL,yL,rosso,verde,blu,end,l,h):
    draw_rect(out,yL,xL,40,40,verde)
    if xL + 40 >= h:
        if ( yL-40 > 0) and out[xL][yL-40] != (rosso or verde):
            direct = '2'
            yL = yL -40
            end += direct
            return out,xL,yL,direct,end
        else:
            if (yL+40 > 0) and out[xL][yL] != (rosso or verde):
                direct = '0'
                yL = yL+40
                end += direct
                return out,xL,yL,direct,end
            else:
                direct=''
                draw_rect(out,yL,xL,40,40,blu)
                end += direct
                return out,xL,yL,direct,end
            
    else:
        if (out[xL+40][yL] == rosso) or (out[xL+40][yL] == verde):
            if (yL-40 < 0) or (out[xL][yL-40] == rosso) or (out[xL][yL-40] == verde):
                if (yL+40 < 0) or (out[xL][yL+40] == rosso) or (out[xL][yL+40] == verde):
                    direct=''
                    draw_rect(out,yL,xL,40,40,blu)
                    end += direct
                    return out,xL,yL,direct,end
                else:
                    yL=yL+40
                    direct = '0'
                    end += direct
                    return out,xL,yL,direct,end
            else:
                yL = yL-40
                direct = '2'
                end += direct
                return out,xL,yL,direct,end
        else:
            xL= xL+40
            direct = '1'
            end += direct
            return out,xL,yL,direct,end
        
def check2(out,xL,yL,rosso,verde,blu,end,l,h):
    draw_rect(out,yL,xL,40,40,verde)
    if yL - 40 < 0 :
        if (xL-40 > 0) and out[xL-40][yL] != (rosso or verde):
            direct = '3'
            xL = xL -40
            end += direct
            return out,xL,yL,direct,end
        else:
            if (xL+40 > 0) and out[xL+40][yL] != (rosso or verde):
                xL=xL+40
                direct = '1'
                end += direct
                return out,xL,yL,direct,end
            else:
                direct = ''
                end += direct
                draw_rect(out,yL,xL,40,40,blu)
                return out,xL,yL,direct,end
    
    else:
        if (out[xL][yL-40] == rosso) or (out[xL][yL-40] == verde):
            if (xL-40 < 0) or (out[xL-40][yL] == rosso) or (out[xL-40][yL] == verde):
                if (xL+40 < 0) or (out[xL+40][yL] == rosso) or (out[xL+40][yL] == verde):
                        direct=''
                        draw_rect(out,yL,xL,40,40,blu)
                        end += direct
                        return out,xL,yL,direct,end
                else:
                    xL = xL+40
                    direct = '1'
                    end += direct
                    return out,xL,yL,direct, end
            else:
                xL = xL-40
                direct = '3'
                end += direct
                return out,xL,yL,direct, end
        else:
            
            yL= yL-40
            direct = '2'
            end += direct
            return out,xL,yL,direct, end

def check3(out,xL,yL,rosso,verde,blu,end,l,h):
    
    draw_rect(out,yL,xL,40,40,verde)
    
    if xL - 40 < 0:
        
        if (yL+40 < l) and out[xL][yL+4] != (rosso or verde):
            direct = '0'
            yL = yL + 40
            end += direct
            return out,xL,yL,direct, end 
        else:
            
            if (yL-40 > 0) and out[xL][yL-40] != (rosso or verde):
                
                yL = yL -40
                
                direct ='2'
                end += direct
                
                return out,xL,yL,direct, end
            else:
                
                direct =''
                draw_rect(out,yL,xL,40,40,blu)
                end += direct
                return out,xL,yL,direct, end
            
    else:
        if (out[xL-40][yL] == rosso) or (out[xL-40][yL] == verde):
            if (yL+40 >= l) or (out[xL][yL+40] == rosso) or (out[xL][yL+40] == verde) :
                if (yL-40 < 0) or (out[xL][yL-40] == rosso) or (out[xL][yL-40] == verde):
                    direct=''
                    draw_rect(out,yL,xL,40,40,blu)
                    end += direct
                    return out,xL,yL,direct,end
                else:
                    
                    yL = yL-40
                    direct = '2'
                    end += direct
                    return out,xL,yL,direct, end
            else:
                yL = yL +40
                direct = '0'
                end += direct
                return out,xL,yL,direct, end
        else:
            
            xL = xL-40
            direct = '3'
            end += direct
            
            return out,xL,yL,direct, end
    
    
def draw_rect(img, x, y, w, h, color):
    for px in range(x, x+w):
        for py in range(y, y+h):
            try:
                img[py][px] = color
            except IndexError:
                pass

'''def check0(out,l,h,xL,yL,rosso,verde,blu):
    try:
        
        if out[xL][yL] == (verde):
            
            if out[xL][yL+40] == (rosso or verde):
                if out[xL+40][yL] == (rosso or verde):
                    if out[xL][yL-40] == (rosso or verde):
                        if out[xL-40][yL] == (rosso or verde):
                            draw_rect(out,xL,yL,40,40,blu)
                            return out,xL,yL
                        else:
                            xL=xL-40
                            draw_rect(out,xL,yL,40,40,verde)
                            
                            return out, xL,yL
                    else:
                        yL=yL-40
                        draw_rect(out,xL,yL,40,40,verde)
                    
                        return out,xL, yL
                else:
                    xL=xL+40
                    draw_rect(out,xL,yL,40,40,verde)
                
                    return out , xL,yL
            else:
                yL=yL+40
                draw_rect(out,yL,xL,40,40,verde)
                
                return out ,xL, yL
        else:
          yL += 40 
          return out ,xL,yL
                        
    except IndexError:
        pass'''