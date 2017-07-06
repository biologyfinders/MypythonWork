#!/usr/bin/python3
import re
file=open("your filename.txt","r")
dna_seq=file
find_motiff=re.findall(dna_seq,pattern)
file.close()


