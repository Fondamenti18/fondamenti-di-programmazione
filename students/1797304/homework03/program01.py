# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:54:01 2017

@author: User
"""

from immagini import *

def quadrato(filename,c):
    immagine= load(filename)
    lato_maggiore=0
    x_img=[]
    y_img=[]
    
    for y in range(len(immagine)):
        for x in range(len(immagine[0])):
            x2=x
            y2=y
            try:
               if immagine[y][x]==c and immagine[y2+lato_maggiore][x]==c and immagine[y][x2+lato_maggiore]==c and immagine[y2+lato_maggiore][x2+lato_maggiore]==c :
                      lato=0
                      while immagine[y2][x]==c and immagine[y][x2]==c and immagine[y2][x2]==c :
                          lato+=1
                          x2=x2+1
                          y2=y2+1
                      if lato>lato_maggiore:
                          contatore=0
                          for py in range(y,y+lato):
                             for px in range(x,x+lato):
                                if immagine[py][px]==c:
                                   next
                                else:
                                   contatore+=1
                          if contatore==0:
                              lato_maggiore=lato
                              x_img=[x]
                              y_img=[y]        
                      elif lato==lato_maggiore:
                           contatore=0
                           for py in range(y,y+(lato)):
                              for px in range(x,x+(lato)):
                                if immagine[py][px]==c:
                                   next
                                else:
                                   contatore+=1
                           if contatore==0 and y_img[0]>y:
                              x_img=[x]
                              y_img=[y]
                           elif contatore==0 and y_img[0]==y:
                              if x<x_img[0]:
                                   x_img=[x]
                                   y_img=[y]

               else:
                   next
            except IndexError:
                pass
    return(lato_maggiore,(x_img[0],y_img[0]))
    

                            
                        
                       
                    
    
                    
                    
    
                    
                    
                    
                    
                    
                    
                    
                    

            
            
                
                
                
                
                

                    
                
                
    
    
    
    
    
                
        
        
            
        
                