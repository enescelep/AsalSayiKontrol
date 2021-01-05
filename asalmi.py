import sys as sistem
sayi=int(input("Pozitif bir sayı giriniz: "))

"""
Bu fonksiyonda klavyeden girilen sayının toplam çarpan sayısını bulduk.
Bilirsiniz, matematikte asal sayıların çarpan sayısı 2'dir.
Bu yüzden asal çarpan sayısı 2'den büyük olan veya 1 olan sayılar asal değildir.
("Tamam 2'den fazlayı anladık örnek:6 ama 1 ne alaka?" diyebilirsiniz, haklısınız.
1 sayısı asal olarak kabul edilmez. 1'in kendisinden başka çarpanı yoktur.)
"""
def toplamCarpanSayisi(f):
    carpanSayisi=0
    for x in range(1,f+1):
        if f%x==0:
            carpanSayisi+=1
    if carpanSayisi>2 or carpanSayisi==1:
        print("Sayı asal değildir")
    else: print("Sayı asaldır")

"""
Bu fonksiyonda 2'den başlayarak girdiğimiz sayıya girene kadar olan sayıları bölüyoruz.
Eğer sayı tam bölünüyorsa 'c' sayacını arttırıyoruz.
Bu fonksiyonun amacını şöyle özetleyebilirim:
Gördüğünüz gibi fonksiyona 'g+1' yazmak yerine 'g' yazdık. 
Bu girdiğimiz sayının bir eksiğine kadar gelmesi demektir.
Aynı şekilde 1 yerine 2'den başlattık.
Şu an anlamış olabilirsiniz bu fonksiyonda amacımız:
Sayının kendisi ve 1 hariç olan çarpanlarını bulup 'c' sayacını arttırmak.
"""
def carpanBol(g):
    c=0
    for y in range (2,g):
        if g%y==0:
            c+=1
    if c>0:
        print("Sayı asal değildir")
    else: print("Sayı asaldır")

# Gerekli kontrolleri yapıyoruz:
if sayi <1:
    print("Girdiğiniz sayı pozitif olmalı.")
    sistem.exit(0)
elif sayi==2:
    print("Sayı asaldır")
    sistem.exit(0)
elif sayi%2==0:
    print("Sayı asal değildir")
    sistem.exit(0)
elif sayi==1:
    print("Sayı asal değildir")
    print("Asal sayılar 2'den itibaren başlar.")
    sistem.exit(0)
else:
    toplamCarpanSayisi(sayi)
    carpanBol(sayi)
