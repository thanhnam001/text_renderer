#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,re
import fileinput

from collections import defaultdict

firstnames = dict()
surnames = dict()

def fill_hashtables(names):
    
    try:
        firstnames[names[0]] += 1
    except:
        firstnames[names[0]] = 1

    for i in range(2,len(names)):
        if len(names[i])==0:
            continue

        try:
            surnames[names[i]] += 1
        except:
            surnames[names[i]] = 1


def main(f):
    for line in fileinput.input(f):

        # remove de,do,da,dos,e
        name = re.sub("\sD[AEO]S?\s|\sE\s"," ", line)

        #  para os casos especiais, como:
        #        "D' ASSUNÇÃO"
        #        "PÊRO - REAL"
        #  ficarem segmentados como um único token
        
        if re.search("' | - ",name):
            tmp_name = re.sub("([^'])\s", "\\1!", name)
            names = re.split("!", tmp_name)
        
        elif re.search(" - ",name):
            tmp_name = re.sub("([^-])\s([^-])", "\\1!\\2", name)
            names = re.split("!", tmp_name)
                       
        else:
            names = re.split("\s+", name)
            
        fill_hashtables(names)
    
    f_firstnames = open("nomes_proprios.txt","w")
    f_surnames = open("apelidos.txt","w")
    
    
    d = defaultdict(list)
    for w in firstnames: 
        d[firstnames[w]].append(w)
        
    for w in sorted(d, reverse=True):
        for n in sorted(d[w]):
            f_firstnames.write(n+"\t"+str(w)+"\n")


    d = defaultdict(list)
    for w in surnames: 
        d[surnames[w]].append(w)
        
    for w in sorted(d, reverse=True):
        for n in sorted(d[w]):
            f_surnames.write(n+"\t"+str(w)+"\n")

    f_firstnames.close()
    f_surnames.close()

if __name__ == "__main__":
    main(sys.argv[1])
