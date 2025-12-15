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

print("Metro")
metro1 = Metro(34, 1000, "Aktif", "Otogar")
metro1.motoru_calistir()
metro1.anons