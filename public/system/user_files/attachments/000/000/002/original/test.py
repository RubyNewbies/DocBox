# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 20:56:12 2014

@author: seventeen
"""

#Pig Latin
import re
y=str(raw_input())
y=y.lower()
m= re.findall(r"\w+",y)

vowel='aeiou'
for n in range(0,len(m)):
   x=m[n] 
   if x[0] in vowel :
            x +='hay'
   elif x[0] in 'q'and x[1] in 'u' :
            x=x[2:]
            x +='quay'
   else:
       if x[0] in 'y':
           x=x[1:] 
           x +='y'
           for i in range(0,len(x)):
             if x[i] not in'aeiouy':
                   x +=x[i]
             else:
                   x=x[i:]+'ay'
                   break
       else:
          for i in range(0,len(x)+1):
            if x[i] not in'aeiouy':
                  x +=x[i]
                      
            else:
              x=x[i:]+'ay'
              break  
   print x,
