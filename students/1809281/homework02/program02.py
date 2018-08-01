import re
import json

def pianifica(fcompiti,insi,fout):
    risultato = {}
    prereq = {}
    
    with open(fcompiti, mode = "r", encoding = "utf-8") as file:   
        prereq = build_prerequisites(file)
        
        for i in insi:
            if i in prereq:
                pointer = i
                risultato[i] = []
                while True:
                    # print(pointer)
                    pointer = prereq[pointer]
                    if len(pointer) == 0:
                        break
                    risultato[i].insert(0, pointer)
    
    
    with open(fout, mode = "w", encoding = "utf-8") as outfile:
        json.dump(risultato, outfile)
    
    # return risultato
    

    
def build_prerequisites(file):
    prereq = {}
    prev_line = ""
    for line in file:  
        match = re.search("(comp|sub) *([0-9]+)", line)
        
        if match and match.group(1) == "comp":
            prereq[match.group(2)] = ""
            
        elif (match and match.group(1) == "sub"):
            prereq[prev_match.group(2)] = match.group(2)
        
        prev_match = match
    return prereq


    
if __name__ == "__main__":
    # print(pianifica("fcompiti.txt", {"7", "1", "5"}, "a.json"))
    
    pianifica("file02_10_2.txt", {"2","4","11","1","6","9","10"},"test1.json")
    # Output: {"7":["9","3"],"1":[]}