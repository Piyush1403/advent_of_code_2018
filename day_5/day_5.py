#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 23:18:43 2018

@author: piyush
"""
#part-1

with open('input.txt') as file:
    for line in file:
        text = str(line.strip())

ugh = list(text)
opp_present = True
              
while(opp_present):
    opp_present = False
    for l in range(0, len(ugh)):
        if(l+1<len(ugh)):
            if (abs(ord(ugh[l])-ord(ugh[l+1]))==32):
                del ugh[l]
                del ugh[l]
                opp_present = True

print(len(ugh))


#part-2

ugh2 = list(text)

import string
alpha = list(string.ascii_lowercase)

final_count = []

for i in alpha:
    short_ugh = []
    for j in ugh2:
        
        if j.upper() != i.upper():
            
            short_ugh.append(j)

    opp_present = True
              
    while(opp_present):
        opp_present = False
        for l in range(0, len(short_ugh)):
            if(l+1<len(short_ugh)):
                if (abs(ord(short_ugh[l])-ord(short_ugh[l+1]))==32):
                    del short_ugh[l]
                    del short_ugh[l]
                    opp_present = True
    
    final_count.append(len(short_ugh))
    
   

print(min(final_count))













