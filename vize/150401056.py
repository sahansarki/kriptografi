#okul numaram 150401056
#Damgard Jurik

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import random
from functools import reduce

def isprime(a):
    """bir sayının asal olup olmadığını kontrol eden fonksiyon"""
    i=3
    if(a<2):
        return(0)
    if a!=2 and a%2==0:
        return(0)
    while i<=a**(1/2):
        if a%i==0:
            return(0)
        i += 2
    return(1)

def allprimes(n):
    """bir sayıdan küçük bütün asal sayıları dizi olarak döndüren fonksiyon"""
    primes=[]
    for i in range(2,n+1):
        primes.append(i)
    for x in range(0,int(n/2)+1):
        if(primes[x]!=0):
            for i in range(x+primes[x],n-1,primes[x]):
                primes[i]=0
    primes.sort()
    return(primes[primes.count(0):])


def lcm(x, y):
  #en büyük ortak katı bulan fonksyon

   
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           ekok = greater
           break
       greater += 1

   return ekok



def oklid(a, b): 
    if a == 0: 
        return (b, 0, 1) 
    else: 
        g, y, x = oklid(b % a, a) 
        return (g, x - (b // a) * y, y) 
  

def modinv(a, m): 
    g, x, y = oklid(a, m) 
    return x % m 
  

def crt(m, x): 
  #chinese remainder theorem fonksyonu 
  
  
    while True: 
          
    
        temp1 = (modinv(m[1],m[0]) * x[0] * m[1]) +  modinv(m[0],m[1]) * x[1] * m[0] 
  
                
      
        temp2 = m[0] * m[1] 
  
       
        x.remove(x[0]) 
        x.remove(x[0]) 
        x = [temp1 % temp2] + x  
  
       
        m.remove(m[0]) 
        m.remove(m[0]) 
        m = [temp2] + m 
  
     
        if len(x) == 1: 
            break
  
   
    return x[0] 
  






while (True):
  #rastgele asal q sayısını üretmek için
  q=random.randint(0,50)
  x=isprime(q)
  if x==1:
    break


while (True):
  #rastgele asal p sayısını üretmek için
  p=random.randint(0,50)
  y=isprime(p)
  if y==1:
    break


k=lcm(q-1,p-1)

j=random.randint(0,50)
x=random.randint(0,50)
s=random.randint(0,10)
r=random.randint(0,50)
g1=random.randint(0,50)#bu değer Pailler için Pailler de şifre çözme kısmında kullanılmak için 


def keygen():
  n=p*q
  g=(((1+n)**j)*x)%(n)**(s+1)
  publiclist = []
  publiclist.append(n)
  publiclist.append(g)
  w=n**s
  kalanlar=[]
  kalanlar.append(1)
  kalanlar.append(0)
  mod=[]
  mod.append(w)
  mod.append(k)
  d=crt(mod,kalanlar)
  dosya1=open('privitekey.txt','w')
  dosya1.write(str(d))
  dosya1.close()
  dosya2=open('publickey.txt','w')
  dosya2.write(str(publiclist))
  dosya2.close()
  
 
 
keygen()
def olus():
  metin=8
  dosya3=open('plaintext','w')
  dosya3.write(str(metin))
  dosya3.close()
olus()#bunu replit'te dosyaya yazdırma yapmadığım için fonksyon içinde yapmak zorunda kaldım. 

def encrypt():
  dosya2=open('privitekey.txt','r')
  okunan=dosya2.read()
  dosya2.close()
  b=float(okunan)
  dosya3=open('plaintext','r')
  metin=dosya3.read()
  dosya3.close()
  m=int(metin)
  n=p*q
  b=n**s
  c=r**b
  g=(((1+n)**j)*x)%(n)**(s+1)
  e=g**m
  f=c*e%(n**(s+1))
  dosya4=open('chipertext','w')
  dosya4.write(str(f))
  dosya4.close()
  #bu satırdan altı Pailler için şifreli metin üretme
  paillermetni=(g1**m)*(r**n)%(n**2)
  dosya4=open('paiiler','w')
  dosya4.write(str(paillermetni))
  dosya4.close()
  
 

encrypt()

def decrypt():
  dosya1=open('chipertext','r')
  c1=dosya1.read()
  c2=int(c1)
  dosya1.close()
  dosya2=open('privitekey.txt','r')
  key=dosya2.read()
  d=int(key)
  dosya2.close()
  #buradan altında jmd hesaplamak için pailler kullanılıyorum.
  dosya3=open('paiiler','r')
  c4=dosya3.read()
  c4=int(c4)
  dosya3.close()
  n=p*q
  def l(u):
    u=u-1/n
    return u
  u1=(c4**k)%(n**2)
  g=(((1+n)**j)*x)%(n)**(s+1)
  u2=(g**k)%(n**2)
  v=(l(u2)**(-1))%n
  jmd=((l(u1)*v)%n)*j*d
  m=(jmd*((j*d)**(-1)))%(n**s)
  print(m)


decrypt()
