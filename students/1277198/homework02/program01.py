#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:43:54 2017

@author: fabio
"""

import re

def post(fposts,insieme):
     '''implementare qui la funzione'''  
     lst=make_lst(fposts)
     pst_match=[]
     i=0
     for i in range(1,len(lst),2):
         pst_match+=[lst[i-1] for w in insieme if re.search('[^a-zA-Z]'+w.lower()+'[^a-zA-Z]',lst[i].lower(),)]
     return set(pst_match)    
    
def make_lst(ftxt):
    with open(ftxt,mode='r') as f:
        rd=f.read()
        content=re.split('<POST>\s*(\d*)',rd)
        del(content[0])
        return content
if __name__=='__main__':
    print(post('file01.txt', {'return'}))