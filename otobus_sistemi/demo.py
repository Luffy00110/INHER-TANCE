from base import Shuttle, Bus, Scooter, Bicyle, Metro, Tramvay, Havaray

print("Main.py dosyasının testi") #Değişme ihtimali mevcut denemek için böyle yaptım.

print("Shuttle")
shuttle1 = Shuttle(15,20,"Müsaıt", 15) #id, kapasite, durum, batarya_yuzdesi
shuttle1.motoru_calistir()
shuttle1.motoru_kapat()
#print(f"{s1.km_basina_maaliyet}") #burda error verdi tanımlamayı unutmuşum şimdilik yorum satırına aldım

print("Otobüs")
otobus1 = Bus(16,"Durakta","Koruklu")
otobus1.motoru_calistir()
#otobus1.motoru_kapat() sıkıntı var
#otobus1.mevcut_lokasyon() hata verdi
print(f"Otobüs Tipi: {otobus1.otobus_tipi}")
print(f"Kapasite: {otobus1.kapasite}") 
otobus1.motoru_kapat()
otobus1.bilgi_ver

print("Metro")
metro1 = Metro(34, 1000, "Aktif", "Otogar")
metro1.motoru_calistir()
metro1.anons

print("Havaray")
havaray1 = Havaray(60, 80, "Ringde", "Vadistanbul AVM")
havaray1.motoru_calistir()
# çalışmadı havaray1.anons()
print(f"Havaray Maliyet: {havaray1.km_basina_maaliyet()} TL")

print("SCOOTER")
Scooter1 = Scooter(99, "Sokakta", 100)
Scooter1.motoru_calistir()
print(f"Scooter Maliyeti: {Scooter1.km_basina_maaliyet()} TL")
Scooter1.motoru_kapat()

print("Genel Bilgiler Alanı")
otobus1.bilgi_ver()
print("-------------------------------------------------------------------")
havaray1.bilgi_ver()
print("-------------------------------------------------------------------")
metro1.bilgi_ver()
print("-------------------------------------------------------------------")
shuttle1.bilgi_ver()
