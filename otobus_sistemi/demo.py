from services import TransportService  
from repository import TransportRepository 
from Shuttle import Shuttle
from Bus import Bus           
from Metro import Metro
from Bicycle import Bicycle    
from Havaray import Havaray
from Scooter import Scooter
from services import servis

print("Shuttle")
shuttle1 = Shuttle(15, 20, "Müsait", 15) #id, kapasite, durum, batarya
shuttle1.motoru_calistir()
shuttle1.motoru_kapat()
#print(f"{s1.km_basina_maaliyet}") #burda error verdi duzelttim

print("Otobüs")
otobus1 = Bus(16, "Durakta", "Koruklu")
#otobus1.mevcut_lokasyon() # hata verdi kapattim
print(f"Otobüs Tipi: {otobus1.otobus_tipi}")
print(f"Kapasite: {otobus1.kapasite}") 

# Ariza denemesi
otobus1.ariza_yap()
otobus1.motoru_calistir()
otobus1.tamir_et()
otobus1.motoru_calistir()

otobus1.motoru_kapat()
otobus1.bilgi_ver()

print("Metro")
metro1 = Metro(34, 1000, "Aktif", "Otogar")
metro1.motoru_calistir()
metro1.anons()

print("Havaray")
havaray1 = Havaray(60, 80, "Ringde", "Vadistanbul AVM")
havaray1.motoru_calistir()
havaray1.anons()
print(f"Havaray Maliyet: {havaray1.km_basina_maaliyet()} TL")

print("SCOOTER")
Scooter1 = Scooter(99, "Sokakta", 100)
Scooter1.motoru_calistir()
print(f"Scooter Maliyeti: {Scooter1.km_basina_maaliyet()} TL")
Scooter1.motoru_kapat()

print("Bicycle")
Bicycle1 = Bicycle(99, "Çalışır", "Ana Kampüs")
Bicycle1.motoru_calistir()

print("Genel Bilgiler Alanı")
print("Otobüs")
otobus1.bilgi_ver()
print("-------------------------------------------------------------------")
print("Havaray")
havaray1.bilgi_ver()
print("-------------------------------------------------------------------")
print("Metro")
metro1.bilgi_ver()
print("-------------------------------------------------------------------")
print("Shuttle")
shuttle1.bilgi_ver()
print("-------------------------------------------------------------------")
print("Bicycle")
Bicycle1.bilgi_ver()
print("Filtreleme Testi")
servis.aktif_seferleri_listele() 
servis.uygun_arac_bul(50) 
print("Test Sonlandı")