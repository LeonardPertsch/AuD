"""
Übung 3, Aufgabe 4: Listenanalyse
=================================

Findet das größte Element einer Liste und dessen Index mit einer
einfachen while-Schleife.
"""

a=[3,5,2,1,3,0,7,4]

def listenanalyse(b):
 highest = 0
 i = 0
 while i < len(b):
  if b[i]>highest:
   highest = b[i]
   highestindex = i
  i = i + 1
 return highest, highestindex

print(listenanalyse(a))
