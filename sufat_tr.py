# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 19:21:37 2024

Emir Can Ertekin 44-252
Mohamed babker Ahmed 19-39 ,251-461
"""
from datetime import datetime
import pandas as pd
import numpy as np
import csv 
import matplotlib.pyplot as plt
import os
import time
from tabulate import tabulate
import sys
#dikorlama için
def dico():
    print("\n#***************************************************#")
    return

#başka abona var mı sorunun cevabı
while True:
    try:
        abone_sayisi = int(input("\nKaç tane aboneniz var? (Ör: 3): "))
        if abone_sayisi <= 0:
            print("\nLütfen girdiğiniz değerin sıfırdan büyük doğal bir sayı olduğundan emin olun.")
        else:
            break
    except ValueError:
        print("\nLütfen girdiğiniz değerin sıfırdan büyük doğal bir sayı olduğundan emin olun.")

for i in range(1, abone_sayisi + 1):
    print(f"\n#***************************************************#\n{i}.aboneniz:")
    if abone_sayisi == 1 or abone_sayisi==i:
        baska_abone = "hayır"
    else:
        if abone_sayisi>=i:
            baska_abone = "evet"
            
            
        
    Abone_tipi = {1:"Konut", 2:"İş Yeri", 3:"Kamu Kuruluşu", 4:"Turistik Tesis"}  #Sözcük ataması yapılacağı için dictionary kullanılmalıdır.

    print(" \nMevcut Abone Tiplerimiz = (1 -> Konut , 2 -> İş Yeri , 3 -> Kamu Kuruluşu , 4 -> Turistik Tesis)")


    while True:
        try:
            abone = int(input(" \nAbone Tipi Kodunuzu Giriniz:  "))
            if abone >= 5 or abone <= 0:
                print(" \nHatalı Giriş Yaptınız Tekrar Deneyin.")
                print(" \nMevcut Abone Tiplerimiz = (1 -> Konut , 2 -> İş Yeri , 3 -> Kamu Kuruluşu , 4 -> Turistik Tesis)")
            else:
                break
        except ValueError:  # Geçersiz girişleri önlemek için kullanılır (örneğin girilirse)
            print("\nHatalı Giriş Yaptınız Tekrar Deneyin.")

    print("\nKullandığınız Abonelik Tipi: ", Abone_tipi[abone])

    while True:   
        try:
            onceki_sayac_deger = int(input("\nÖnceki Sayaç Değerini Giriniz: "))
            if onceki_sayac_deger < 0 :
                print("\nSayaç Değeriniz Sıfırdan Küçük Olamaz ")
            else:
                break
        except ValueError:  
            print("\nHatalı Giriş Yaptınız Tekrar Deneyin.")
    while True:
        try:
            simdiki_sayac_deger = int(input("\nŞimdiki Sayaç Değerini Giriniz: "))
            if simdiki_sayac_deger <0 :
                print("\nSayaç Değeriniz Sıfırdan Küçük Olamaz ")
            elif simdiki_sayac_deger<onceki_sayac_deger:
                print("\nşimdiki sayac dğeri önceki sayaç degerden küçük olmaz")
            else:
                break
        except ValueError:  
            print("\nHatalı Giriş Yaptınız Tekrar Deneyin.")
    while True:
        try:
            su_kullanım = simdiki_sayac_deger - onceki_sayac_deger
            if su_kullanım <0:
                print("\nŞimdiki sayaç değeriniz önceki sayaç değerinden küçük olamaz. Tekrar deneyin.")
            else:
                break
        except ValueError:  
            print("\nHatalı Giriş Yaptınız Tekrar Deneyin.")
        
                        
    print("\nToplam Su Kullanımınız: ",su_kullanım) 


    while True:        
        while True:
            try:
                onceki_tarih_1 = input("\nÖnceki Sayaç Değerinin Okunma Tarihini YIL-AY-GÜN (Örn: 2024-11-25) Şeklinde Giriniz: ")
                onceki_tarih = datetime.strptime(onceki_tarih_1, "%Y-%m-%d")
                break
            except ValueError:  
                print("\nHatalı Giriş Yaptınız Tekrar Deneyin.")
        while True:        
            try:
                simdiki_tarih_1 = input("\nŞimdiki Sayaç Değerinin Okunma Tarihini YIL-AY-GÜN (Örn: 2024-12-25) Şeklinde Giriniz: ")
                simdiki_tarih = datetime.strptime(simdiki_tarih_1 , "%Y-%m-%d")
                break
            except ValueError:  
                print("\nHatalı Giriş Yaptınız Tekrar Deneyin.")
            
            
        try:
            if simdiki_tarih < onceki_tarih:
                print("\nŞimdiki tarih önceki tarihten geçmişte olamaz.Tekrar Deneyiniz.")
            else:    
                gecen_süre = (simdiki_tarih - onceki_tarih).days
                if gecen_süre == 0:
                    print("\nGeçen gün sayısı 0 olamaz. Tekrar Deneyiniz.")
                else:
                    break
        except ValueError:  
            print("\nHatalı Giriş Yaptınız Tekrar Deneyin.")
    dico()
    print("\nSon Sayaç Okumanın Üzerinden Geçen Gün Sayısı: ", gecen_süre) 
    aylık_su_tüketimi = (su_kullanım / gecen_süre) *30
    if aylık_su_tüketimi > su_kullanım:
        print("\nSu Kullanım Süreniz Bir Ayı Doldurmamıştır")
        print("\nŞimdiye Kadarki Su Kullanımınız: ", f"{su_kullanım:.2f}", "Tondur")
    else:    
        print("\nAylık Su Tüketiminiz: ", f"{aylık_su_tüketimi:.2f}", " Tondur")
    if gecen_süre < 30 :
        if abone == 1:
            if su_kullanım >= 0 and su_kullanım <= 13:
                ucret = su_kullanım *2.24
                aylık_su_tüketim_ucret = ucret
                print("\n",gecen_süre ,"Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
            elif su_kullanım > 13 and su_kullanım <= 20:
                ucret = su_kullanım *5.78
                aylık_su_tüketim_ucret = ucret
                print("\n",gecen_süre ,"Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
            elif su_kullanım > 20:
                ucret = su_kullanım *9.33
                aylık_su_tüketim_ucret = ucret
                print("\n",gecen_süre ,"Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
        elif abone == 2:
            if su_kullanım > 0 and su_kullanım <= 10:
                ucret = su_kullanım *7.71
                aylık_su_tüketim_ucret = ucret
                print("\n",gecen_süre ,"Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
            elif su_kullanım > 10:
                ucret = su_kullanım *8.88
                aylık_su_tüketim_ucret = ucret
                print("\n",gecen_süre ,"Günlükk Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
        elif abone == 3:
            ucret = su_kullanım *6.64
            aylık_su_tüketim_ucret = ucret
            print("\n",gecen_süre ,"Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
        elif abone == 4:
            ucret = su_kullanım *5.78
            aylık_su_tüketim_ucret = ucret
            print("\n",gecen_süre ,"Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
        if abone == 1:
            aylık_atık_su_ucreti = su_kullanım *1.91
            print("\n",gecen_süre ,"Günlük Atık Su Ücretini: ", f"{aylık_atık_su_ucreti:.2f}","TL'dir." )
        if abone == 2:
            aylık_atık_su_ucreti = su_kullanım *3.79
            print("\n",gecen_süre ,"Günlük Atık Su Ücretini: ", f"{aylık_atık_su_ucreti:.2f}","TL'dir." )
        if abone == 3:
            aylık_atık_su_ucreti = su_kullanım *2.56
            print("\n",gecen_süre ,"Günlük Atık Su Ücretini: ", f"{aylık_atık_su_ucreti:.2f}","TL'dir." )
        if abone == 4:
            aylık_atık_su_ucreti = su_kullanım *1.91
            print("\n", gecen_süre ,"Günlük Atık Su Ücretini: ", f"{aylık_atık_su_ucreti:.2f}","TL'dir." )
        kdv_tutar = (aylık_atık_su_ucreti + aylık_su_tüketim_ucret) *0.08
        print("\nToplam KDV Tutarınız: ", f"{kdv_tutar:.2f}", "TL'dir")
        fatura_tutar = (aylık_atık_su_ucreti + aylık_su_tüketim_ucret + kdv_tutar)
        print("\n", gecen_süre,"Günlük Toplam Fatura Tutarınız: ", f"{fatura_tutar:.2f}", "TL'dir.")
    else:  
        if abone == 1:
            if aylık_su_tüketimi >= 0 and aylık_su_tüketimi <= 13:
                ucret = aylık_su_tüketimi *2.24
                toplam_su_ucreti = su_kullanım *2.24
                print("\n30 Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
                if toplam_su_ucreti != ucret:
                    print("\n",gecen_süre ,"Günlük Ödemeniz Gereken Toplam Su Tüketim Ücretiniz: ", f"{toplam_su_ucreti:.2f}", "TL'dir." )
            elif aylık_su_tüketimi > 13 and aylık_su_tüketimi <= 20:
                ucret = aylık_su_tüketimi *5.78
                toplam_su_ucreti = su_kullanım *5.78
                print("\n30 Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
                if toplam_su_ucreti != ucret:
                    print("\n",gecen_süre ,"Günlük Ödemeniz Gereken Toplam Su Tüketim Ücretiniz: ", f"{toplam_su_ucreti:.2f}", "TL'dir." )
            elif aylık_su_tüketimi > 20:
                ucret = aylık_su_tüketimi *9.33
                toplam_su_ucreti = su_kullanım *9.33
                print("\n30 Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
                if toplam_su_ucreti != ucret:
                    print("\n",gecen_süre ,"Günlük Ödemeniz Gereken Toplam Su Tüketim Ücretiniz: ", f"{toplam_su_ucreti:.2f}", "TL'dir." )
        elif abone == 2:
            if aylık_su_tüketimi > 0 and aylık_su_tüketimi <= 10:
                ucret = aylık_su_tüketimi *7.71
                toplam_su_ucreti = su_kullanım *7.71
                print("\n30 Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
                if toplam_su_ucreti != ucret:
                    print("\n",gecen_süre ,"Günlük Ödemeniz Gereken Toplam Su Tüketim Ücretiniz: ", f"{toplam_su_ucreti:.2f}", "TL'dir." )
            elif aylık_su_tüketimi > 10:
                ucret = aylık_su_tüketimi *8.88
                toplam_su_ucreti = su_kullanım *8.88
                print("\n30 Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
                if toplam_su_ucreti != ucret:
                    print("\n",gecen_süre ,"Günlük Ödemeniz Gereken Toplam Su Tüketim Ücretiniz: ", f"{toplam_su_ucreti:.2f}", "TL'dir." )
        elif abone == 3:
            ucret = aylık_su_tüketimi *6.64
            toplam_su_ucreti = su_kullanım *6.64
            print("\n30 Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
            if toplam_su_ucreti != ucret:
                print("\n",gecen_süre ,"Günlük Ödemeniz Gereken Toplam Su Tüketim Ücretiniz: ", f"{toplam_su_ucreti:.2f}", "TL'dir." )
        elif abone == 4:
            ucret = aylık_su_tüketimi *5.78
            toplam_su_ucreti = su_kullanım *5.78
            print("\n30 Günlük Su Tüketim Ücretiniz: ", f"{ucret:.2f}","TL'dir." )
            if toplam_su_ucreti != ucret:
                print("\n",gecen_süre ,"Günlük Ödemeniz Toplam Su Tüketim Ücretiniz: ", f"{toplam_su_ucreti:.2f}", "TL'dir." )
        if abone == 1:
            aylık_atık_su_ucreti = aylık_su_tüketimi *1.91
            toplam_atık_su_ucreti = su_kullanım *1.91
            print("\n30 Günlük Atık Su Ücretini: ", f"{aylık_atık_su_ucreti:.2f}","TL'dir." )
            if toplam_atık_su_ucreti != aylık_atık_su_ucreti:
                print("\n",gecen_süre ,"Günlük Ödemeniz Gereken Toplam Atık Su Tüketim Ücretiniz: ", f"{toplam_atık_su_ucreti:.2f}", "TL'dir." )
        if abone == 2:
            aylık_atık_su_ucreti = aylık_su_tüketimi *3.79
            toplam_atık_su_ucreti = su_kullanım *3.79
            print("\n30 Günlük Atık Su Ücretini: ", f"{aylık_atık_su_ucreti:.2f}","TL'dir." )
            if toplam_atık_su_ucreti != aylık_atık_su_ucreti:
                print("\n",gecen_süre ,"Günlük Ödemeniz Gereken Toplam Atık Su Tüketim Ücretiniz: ", f"{toplam_atık_su_ucreti:.2f}", "TL'dir." )
        if abone == 3:
            aylık_atık_su_ucreti = aylık_su_tüketimi *2.56
            toplam_atık_su_ucreti = su_kullanım *2.56
            print("\n30 Günlük Atık Su Ücretini: ", f"{aylık_atık_su_ucreti:.2f}","TL'dir." )
            if toplam_atık_su_ucreti != aylık_atık_su_ucreti:
                print("\n",gecen_süre ,"Günlük Ödemeniz Toplam Atık Su Tüketim Ücretiniz: ", f"{toplam_atık_su_ucreti:.2f}", "TL'dir." )
        if abone == 4:
            aylık_atık_su_ucreti = aylık_su_tüketimi *1.91
            toplam_atık_su_ucreti = su_kullanım *1.91
            print("\n30 Günlük Atık Su Ücretini: ", f"{aylık_atık_su_ucreti:.2f}","TL'dir." )
            if toplam_atık_su_ucreti != aylık_atık_su_ucreti:
                print("\n",gecen_süre ,"Günlük Ödemeniz Gereken Toplam Atık Su Tüketim Ücretiniz: ", f"{toplam_atık_su_ucreti:.2f}", "TL'dir." )
        kdv_tutar = (toplam_atık_su_ucreti + toplam_su_ucreti) *0.08
        print("\nToplam KDV Tutarınız: ", f"{kdv_tutar:.2f}", "TL'dir")
        fatura_tutar = (toplam_atık_su_ucreti + toplam_su_ucreti + kdv_tutar)
        print("\n", gecen_süre, "Günlük Toplam Fatura Tutarınız: ", f"{fatura_tutar:.2f}", "TL'dir.")
            
            

# amaç yukardaki değerler toplayıp bir csv dosyada yazmaktır   

    file_exists = os.path.isfile("data.csv")


    with open("data.csv", mode="a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(["Abone Tipi", "Önceki Sayaç Değeri", "Şimdiki Sayaç Değeri", "Gün Sayısı", "Başka Abone Var Mı?",\
                            "Su Tüketim Miktarı", "Su Tüketim Ücreti", "Atık Su Ücreti", "KDV Tutarı", "Fatura Tutarı"])
        
        writer.writerow([Abone_tipi[abone], onceki_sayac_deger, simdiki_sayac_deger, gecen_süre, baska_abone, aylık_su_tüketimi, ucret,\
                        aylık_atık_su_ucreti, kdv_tutar, fatura_tutar])
dico()
print("\nAbone bilgileri CSV dosyasına başarıyla eklenildi.")
dico()


df=pd.read_csv("data.csv")
 
#başlığın tasarımı girilmiş başlık adına göre
def başlık(başlık_adı):
    ba = başlık_adı.upper()
    frame_length = 50
    padding = (frame_length - len(ba)) // 2
    title_line = f"{' ' * padding}{ba}{' ' * padding}"
    if len(title_line) < frame_length:
        title_line += ' ' * (frame_length - len(title_line))

    top_bottom_border = f"+{'-' * frame_length}+"
    empty_line = f"|{' ' * frame_length}|"
    title_with_border = f"|{title_line}|"

    print("\n" + top_bottom_border)
    print(empty_line)
    print(title_with_border)
    print(empty_line)
    print(top_bottom_border)

#kullancıdan ayrıntıları görmek amacıyla izin alma işlemi
while True:
    try:
        detaylar=input("\nAyrıntıları ve tabloları görmek ister misiniz?(evet/hayır)").strip().lower()

        if detaylar == "hayır":
            print("\nSize teşekkür ediyoruz")
            time.sleep(1)
            print("\niyi günler :)")
            sys.exit()
        elif detaylar != "evet" and detaylar!="hayır":
            print("\nLütfen Hayır veya Evet arasından seçim yapın.")
        elif detaylar=="evet":
            break
    except ValueError:
        print("\nLütfen Hayır veya Evet arasından seçim yapın.")
    dico()

#burada vergülden sonra 2 basmaklı olabilmesi için round kullanılır
df["Su Tüketim Miktarı"] = df["Su Tüketim Miktarı"].round(2)
df["Su Tüketim Ücreti"] = df["Su Tüketim Ücreti"].round(2)
df["Atık Su Ücreti"] = df["Atık Su Ücreti"].round(2)
df["KDV Tutarı"] = df["KDV Tutarı"].round(2)
df["Fatura Tutarı"] = df["Fatura Tutarı"].round(2)

başlık("girdiler")
print(tabulate(df.iloc[:, :5], headers='keys', tablefmt='grid'))

başlık("Çıktılar")
print(tabulate(df.iloc[:, 5:], headers='keys', tablefmt='grid'))
dico()

#buradaki fonksiyonun görevi n sütundeki m abone tipi olanların toplama almasıdır.başka bir söz ile dosayda her abone tipin sayısı bulmaktır.
def count(n,m):
    cnt=df[n].str.count(m).sum()
    
    return cnt

#buradaki fonksiyonun görevi kullancıya hedeflenen bilgiler veya tabloları sunmadan izin almasıdır.     
def sor(cumle):
    while True:
        try:
            detaylar=input(f"\n{cumle} görmek için 'enter' basınız)").strip().lower()
            
            if detaylar!="":
                print(f"\nLütfen {cumle} görmek için 'enter' basınız.")
            if detaylar=="":
                break
        except ValueError:
            print(f"\nLütfen {cumle} görmek için 'enter' basınız.")


konut=count("Abone Tipi","Konut")
turistik=count("Abone Tipi","Turistik Tesis")       
iş_yeri=count("Abone Tipi","İş Yeri")    
kuruş=count("Abone Tipi","Kamu Kuruluşu")  

abone_t=["Konut","Turistik Tesis","İş Yeri","Kamu Kuruluşu"]
abone_s=[konut,turistik,iş_yeri,kuruş] 

#bunun kulanma amacı görselde sadece var olan abone tipinin yüzdesi gözüksün.
filtered_abone_t = [abone for abone, sayı in zip(abone_t, abone_s) if sayı > 0]
filtered_abone_s = [sayı for sayı in abone_s if sayı > 0]

df['Günlük Ort Tük'] = df['Su Tüketim Miktarı'] / df['Gün Sayısı']
df['Günlük Ort Tük']=df['Günlük Ort Tük'].round(2)

grouped = df.groupby('Abone Tipi').agg(
    Abone_Sayısı=('Abone Tipi', 'count'),
    Toplam_Gün_Sayısı=('Gün Sayısı', 'sum'),
    Toplam_Su_Tüketimi=('Su Tüketim Miktarı', 'sum')
).reset_index()

grouped['Günlük Ort Tük'] = (grouped['Toplam_Su_Tüketimi'] / grouped['Toplam_Gün_Sayısı']).round(2)

total_abone = grouped['Abone_Sayısı'].sum()
grouped['Yüzde'] = (grouped['Abone_Sayısı'] / total_abone) * 100
grouped['Yüzde'] = grouped['Yüzde'].round(2)


sor("Abone Tipi ile İLgili Bilgiler")
print(tabulate(grouped, headers='keys', tablefmt='grid'))

plt.figure(figsize=(10, 6))
wedges, texts, autotexts = plt.pie(filtered_abone_s, labels=filtered_abone_t, autopct='%1.1f%%', startangle=140,\
                                     colors=["darkslateblue", "royalblue", "lightblue", "skyblue"], wedgeprops=dict(alpha=0.7))

plt.title("Abone Tipi ile İLgili Bilgiler")
for text in autotexts:
    text.set_color('white')
sor("tablo")
plt.show() 

#amaç: "Aylık su tüketim miktarı, 1. kademeyi aşmayan konut abonelerinin:sayısı ve yüzdesi" sorunun cevablamak.
konut_df = df[df['Abone Tipi'] == "Konut"]
subset_konut = konut_df[konut_df['Su Tüketim Miktarı'] <= 13]
num_subset_konut = len(subset_konut)
percentage_subset_konut = (num_subset_konut / konut) * 100 if konut > 0 else 0

if num_subset_konut > 0:
     print(f"\nAylık su tüketim miktarı, 1. kademeyi aşmayan konut abonelerinin:\
           \nsayısı:{num_subset_konut}, yüzdesi: {percentage_subset_konut:.2f}%")
else:
    print(f"\nAylık su tüketim miktarı, 1. kademeyi aşmayan konut aboneleri bulunmamaktadır.") 

#amaç:"Günlük ortalama su miktarı en yüksek olan konut tipi abonenin günlük ortalama su tüketim miktarı"bulmak.
en_yuksek_gunluk_ort_tuk = konut_df['Günlük Ort Tük'].max()
print(f"\nGünlük ortalama su tüketim miktarı en yüksek olan konut tipi abonenin günlük\
    ortalama su tüketim miktarı:{en_yuksek_gunluk_ort_tuk:.2f} ton")

#amaç: "Aylık su tüketim miktarı, 1. kademeyi aşan işyeri  abonelerinin:sayısı ve yüzdesi" sorunun cevablamak.
is_yeri_df = df[df['Abone Tipi'] == "İş Yeri"] 
subset_is_yeri = is_yeri_df[is_yeri_df['Su Tüketim Miktarı'] > 10]
num_subset_is_yeri = len(subset_is_yeri)
percentage_subset_is_yeri = (num_subset_is_yeri / iş_yeri) * 100 if iş_yeri > 0 else 0

if num_subset_is_yeri > 0:
     print(f"\nAylık su tüketim miktarı, 1. kademeyi aşan işyeri abonelerinin:\nsayısı: {num_subset_is_yeri}, yüzdesi: {percentage_subset_is_yeri:.2f}%")
else:
    print(f"\nAylık su tüketim miktarı, 1. kademeyi aşan işyeri aboneleri bulunmamaktadır.")

"""
fonksiyonun amacı:
Aylık su tüketim (ücreti,ya da miktarı) en yüksek olan abonenin:
(abone tipi ,su tüketim miktarı,ödediği aylık [su tüketim,atkı su] ücreti) bulmak.
ona göre bir görsel oluşturmak
"""
def max(column,cumle):
    max_index = df[column].idxmax()
    max_abone = df.loc[max_index] 
    max_height = df[column].max()
    dico()
    sor(f"\nAylık {cumle} Ücreti En Yüksek Olan Abone")

    print(f"\nAylık {cumle} ücreti en yüksek olan abonenin bilgileri:\
            \nAbone Tipi: {max_abone['Abone Tipi']}\
            \nAylık Su Tüketim Miktarı: {max_abone['Su Tüketim Miktarı']} ton\
            \nÖdediği Aylık {cumle} Ücreti: {max_abone[column]} TL")
    sor("tablo")

    plt.figure(figsize=(10, 6))
    bars = plt.bar(df['Abone Tipi'], df[column], color="darkslateblue", alpha=0.7)
    plt.xlabel("Abone Tipi")
    plt.ylabel(f"{cumle} Ücreti (TL)")
    plt.title(f"Aylık {cumle} Ücreti En Yüksek Olan Abone")
    plt.axhline(y=max_abone[column], color='r', linestyle='--')
    plt.text(0, max_abone[column], f"En Yüksek: {max_abone[column]}\
            TL", color='r', ha='left', va='bottom')
    plt.show()

max("Su Tüketim Ücreti","Su Tüketim")

max("Atık Su Ücreti","Atık Su")
#fonksiyonun amacı:her abone tipi için [Toplam Su Tük Miktarı] bulup görsel oluşturmak.
def toplam(column,cumle,birim):
    toplam_su_tuk= df.groupby('Abone Tipi')[column].sum().reset_index()
    plt.figure(figsize=(10, 6))
    bars = plt.bar(toplam_su_tuk['Abone Tipi'], toplam_su_tuk[column], color="darkslateblue", alpha=0.7)
    plt.xlabel("Abone Tipi")
    plt.ylabel(f"Toplam Su Tüketim {cumle} (ton)")
    plt.title(f"Abone Tipine Göre Toplam Su Tüketim {cumle}")

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height, f"{height:.2f} {birim}", ha="center", va="bottom", color="black")
    dico()
    sor(f"Toplam Su Tüketim {cumle}ın tablosu")
    plt.show()

toplam("Su Tüketim Miktarı","miktarı"," ton")

toplam("Su Tüketim Ücreti","ücreti"," TL")

#amaç: Tüm abonelerden elde edilen [aylık toplam atık su ücreti,aylık toplam KDV tutarı] hesaplamaktır.

def tum(column,cumle):
    tasu=df[column].sum().round(2)
    dico()
    sor(cumle)
    print(f"\n{cumle}: {tasu} TL")
    return

tum("Atık Su Ücreti","Tüm abonelerden elde edilen aylık toplam atık su ücreti: ")

tum("KDV Tutarı","Devlete ödenen aylık toplam KDV tutarı: ")

