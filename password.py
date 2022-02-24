# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:05:19 2022

@author: ASUS
"""

import random 
import string
s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)
CN=input(" enter how many caracters: ")
while True :
  CN=int(CN)
  try:
    if CN < 6:
      print("at least 6 caracters")
      CN=input("more than six characters please ")
    else:
      break
  except:
    print("enter numbers only")
    CN=input("how many characters: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
p1=round(CN*(30/100))
p2=round(CN*(20/100))
password=[]
for i in range(p1):
 password.append(s1[i])
 password.append(s2[i])
  
for j in range(p2):
 password.append(s3[j])
 password.append(s4[j])

password="".join(password[0:])
print(password)










