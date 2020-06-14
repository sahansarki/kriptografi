# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 20:18:58 2020

@author: Enes Nurullah Kendirci 170401067
"""

import random
from datetime import datetime

def final(dosya):   #istenilen final fonksiyonu
    with open(dosya, 'rb') as d:
        data = ((d.read()).decode()).zfill(32)
    girdi = data
    girdi = '10000000010110000011000010010010' + girdi
    kayik = bin(int(girdi,2) << 16) #sayiyinin özetlenme islemleri // sayiyi kaydirip ikiye bölüp üzerlerinde xor işlemleri özetliyorum
    kayikilk = kayik[:32]
    kayikson = kayik[32:]
    xor = (bin(int(kayikilk[2:]) ^ int(kayikson[2:]))[2:]).zfill(256)
    parcalanmisxor = (int(xor[0:31],2) ^ int(xor[31:63],2)) ^ int(xor[63:95],2) ^ int(xor[95:127],2) ^ int(xor[127:159],2)  ^ int(xor[159:191],2) ^ int(xor[191:223],2) ^ int(xor[223:255],2)
    ozet = bin(parcalanmisxor)[2:]
    
    return ozet
 
sure = datetime.now().minute #islemin 10dakikayi gecmesini istemiyoruz
for i in range(1,101):
    sureKontrol = datetime.now().minute - sure
    
    if(sureKontrol < 10):   #satir25
        if(i < 10): #dosyanin hazirlanmasi
            dosyaAdi = '00' + str(i) + '.txt'
        elif(i<100):
            dosyaAdi = '0' + str(i) + '.txt'
        ozet = str(final(dosyaAdi))
        
        while(1):   #odevde istenilen kosul saglanana kadar denemeyi saglamak icin while dongusu
            
            rasgaleSayi =  random.getrandbits(32)
            
            toplam = (bin(int(ozet,2) + rasgaleSayi))[2:].zfill(32) #istenilen kosul
            
            if(len(toplam) > 32):   #overflow
                toplam = toplam[-32:]
                
            if(i < 9):  #ozetin yazilacagi dosyayi hazirlama
                dosyaAdi = '00' + str(i + 1) + '.txt'
                dosya = open(dosyaAdi, 'w')
            elif(i<99):
                dosyaAdi = '0' + str(i + 1) + '.txt'
                dosya = open(dosyaAdi, 'w')
            else:
                dosyaAdi = '100.txt'
                dosya = open(dosyaAdi, 'w')
                
            dosya.write(toplam) #ozetin yazilmasi
            
            kontrol = (str(final(dosyaAdi)).zfill(32)) #istenilen ilk 8 bitin 0 olma kosulu
            if(kontrol[:8] == '00000000'):  3
                hashsum = open('HASHSUM.txt', 'a')
                hashsum.write((bin(rasgaleSayi))[2:].zfill(32) + ' - ' + kontrol + '\n')
                hashsum.close()
                break
                
    else: #surenin bitme durumu
        print("Hocam bitti' -Yılmaz Vural")




    
