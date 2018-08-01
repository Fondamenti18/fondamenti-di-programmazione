# -*- coding: utf-8 -*-
from  my_html import HTMLNode, fparse

def conta_nodi(fileIn, selettore):

    root = fparse(fileIn)
    list = get_nodes(selettore,root)
    return count(len(list))
    
#the other ones are fine,please let me have this
    
def count(index):
    
    if index == 0:
        return 0
    x = count(index - 1) + 1
    return x
    
def elimina_nodi(fileIn, selettore, fileOut):
    
    root = fparse(fileIn)
    list = get_nodes(selettore,root)
    
    frontier = [root]
        
    while len(frontier) > 0:
        
        current = frontier.pop()
        
        for child in current.content:     
            
            if type(child) == HTMLNode:
                if child in list:
                    current.content.remove(child)
                else:
                    frontier.append(child)                  
    
    with open(fileOut,'w') as f:        
        f.write(root.to_string())
    
def cambia_attributo(fileIn, selettore, chiave, valore, fileOut):
    
    root = fparse(fileIn)
    list = get_nodes(selettore,root)
    
    for node in list:        
        try:
            node.attr[chiave] = valore
        except KeyError:
            pass
    
    with open(fileOut,'w') as f:        
        f.write(root.to_string())
        

def get_nodes(selector,root):
    
    if " " in selector or ">" in selector:
        return list_complex(selector,root)
    else:
        list = [];
        list_simple(selector,root,list)
        return list
    
def list_complex(selector,root):
        
    format = []    
    
    for i in range(len(selector)):       
        if selector[i] == ">":
            format.append(i)
    
    selector = list(selector)
    
    while len(format) > 0:
        
        i = format.pop()        
        selector[i-1] = ""
        selector[i+1] = ""        
    
    selector = "".join(selector)
    
    indices = []
    
    for i in range(len(selector)):       
        if selector[i] == ">" or selector[i] == " ":
            indices.append(i)
    
    #indices.append(len(selector)-1)
    
    returnlist = []
           
    if len(indices) == 1:
        return list_rel(selector,root)
    else:
        i = 0
        
        start = 0
        end = indices[1]
        newSelector = selector[start:end]
        returnlist = list_rel(newSelector,root)
        
        #print(newSelector,"start")
        
        while i + 2 != len(indices):
            
            start = indices[i] + 1
            end = indices[i + 2]
            
            newSelector = selector[start:end]
            newlist = []
            
            #print(newSelector,"middle")
            
            for node in returnlist:
                newlist += list_rel(newSelector,node)
                
            returnlist = newlist[:]
            
            i += 1
               
        start = indices[-2] + 1
        end = len(selector)
        newSelector = selector[start:end]
        newList = []
        
        #print(newSelector,"end")
        
        for node in returnlist:
            newList += list_rel(newSelector,node)
            
        returnlist = newList[:]
    
    return returnlist
    
def list_simple(selector,root,list,oneLevel = -1):
    
    char = selector[0]
    #list = []
    
   # print("looking for " + char)  
    
    if oneLevel > 0:
        oneLevel -= 1
    
    if oneLevel == 0:
        return
    
    if char.isalpha():
            
        if root.tag == selector:
            list.append(root)
            
        for child in root.content:
            if type(child) == HTMLNode:
                list_simple(selector,child,list)                
    else:
        
        key = ""
        value = selector[1:]
        
        if char == ".":
            key = "class"
        elif char == "#":
            key = "id"
        elif char == "@":
            mid = selector.find("=")
        
            key = selector[2:mid]
            value = selector[(mid+2):selector.find("]")-1]
        
        try:
            if key != "class":
                if root.attr[key] == value:
                    list.append(root)
            else:
                if root.attr[key].find(value) != -1:
                    list.append(root)
                
        except KeyError:
            pass
                    
        for node in root.content:
            if type(node) == HTMLNode:
                #frontier.append(node)
                list_simple(selector,node,list,oneLevel);
    
def list_rel(selector,root):
    
    list = []
    
    if ">" in selector:
        mid = selector.find(">")
    
        parentKey = selector[:mid]
        childKey = selector[mid+1:]
        
        parentList = []
        
        list_simple(parentKey,root,parentList)
        #print(len (parentList),"parents")
        
        for parent in parentList:           
            
            childlist = []
            
            for child in parent.content:          
                list_simple(childKey,child,childlist,2)
                        
            list += childlist
            #for c in childlist:
                #print(c.attr)
            
    elif " " in selector:
    
        mid = selector.find(" ")
        
        grandparentKey = selector[:mid]
        grandchildKey = selector[mid+1:]
        
        grandparentList = [] 
        list_simple(grandparentKey,root,grandparentList)
        
        for grandparent in grandparentList:                              
            l = []
            list_simple(grandchildKey,grandparent,l)
            list += l

    return list
    