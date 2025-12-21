from TransportService import TransportService
from Bus import Bus
from Shuttle import Shuttle
from Metro import Metro
from Havaray import Havaray
from Scooter import Scooter
from Bicycle import Bicycle
from Tramvay import Tramvay
from Metrobus import Metrobus
from Vapur import Vapur
from Teleferik import Teleferik
from DenizTaksi import DenizTaksi
from base import TransportVehicle

# Servis yonetim nesnesini baslat
servis = TransportService()

print("-" * 60)
print("OTOBUS FILOSU TANIMLAMA VE TEST")
print("-" * 60)
# id, durum, mevcut_yakit, otobus_tipi, plaka, lokasyon
otobus1 = Bus(101, "Müsait", 150, "Koruklu", "34 IBB 101", "Tuzla")
otobus2 = Bus(102, "Müsait", 80, "Standart", "34 IBB 102", "Kadikoy")
otobus3 = Bus(103, "Arızalı", 20, "Standart", "34 IBB 103", "Mecidiyekoy")

servis.arac_kayit(otobus1)
servis.arac_kayit(otobus2)
servis.arac_kayit(otobus3)

otobus1.motoru_calistir()
otobus3.motoru_calistir() # Arızalı oldugu icin hata verecek
otobus3.tamir_et()        # Tamir ediliyor
otobus3.benzin_al(100)    # Yakit ikmali
otobus3.motoru_calistir() # Artik çalışabilir

print("\n" + "-" * 60)
print("SHUTTLE (TESTI")
print("-" * 60)
# id, kapasite, durum, batarya_yuzdesi, lokasyon
shuttle1 = Shuttle(201, 20, "Müsait", 90, "Ana Kampus")
shuttle2 = Shuttle(202, 20, "Müsait", 15, "Kuzey Kampus")
shuttle3 = Shuttle(203, 15, "Şarjda", 5, "Guney Kampus")

servis.arac_kayit(shuttle1)
servis.arac_kayit(shuttle2)
servis.arac_kayit(shuttle3)

shuttle1.motoru_calistir()
shuttle2.motoru_calistir()
shuttle3.sarj_et()

print("\n" + "-" * 60)
print("METRO SISTEMI TESTI")
print("-" * 60)
# id, durum, yakit, depo, kapasite, durak_km, km_ucreti, hat, lokasyon
metro1 = Metro(301, "Aktif", 100, 500, 1200, 1.2, 5.5, "M1 Yenikapi", "Otogar")
metro2 = Metro(302, "Aktif", 100, 500, 1500, 1.5, 6.0, "M2 Haciosman", "Taksim")
metro3 = Metro(303, "Bakımda", 50, 500, 1000, 1.0, 5.0, "M4 Kadikoy", "Kartal")

servis.arac_kayit(metro1)
servis.arac_kayit(metro2)
servis.arac_kayit(metro3)

metro1.anons()
metro2.motoru_calistir()

print("\n" + "-" * 60)
print("HAVARAY SISTEMI TESTI")
print("-" * 60)
# id, kapasite, durum, yakit, depo, durak_km, km_ucreti, lokasyon
havaray1 = Havaray(401, 80, "Müsait", 100, 100, 0.7, 3.5, "Vadistanbul AVM")
havaray2 = Havaray(402, 60, "Müsait", 100, 100, 0.5, 3.5, "Seyrantepe")
havaray3 = Havaray(403, 80, "Arızalı", 100, 100, 0.7, 3.5, "Cendere")

servis.arac_kayit(havaray1)
servis.arac_kayit(havaray2)
servis.arac_kayit(havaray3)

havaray1.motoru_calistir()

print("\n" + "-" * 60)
print("SCOOTER PAYLASIM SISTEMI TESTI")
print("-" * 60)
# id, durum, batarya, durak_km, km_ucreti, acilis, lokasyon
scooter1 = Scooter(501, "Müsait", 100, 0.5, 3.5, 10, "Besiktas")
scooter2 = Scooter(502, "Müsait", 45, 0.5, 3.5, 10, "Ortakoy")
scooter3 = Scooter(503, "Müsait", 8, 0.5, 3.5, 10, "Bebek")

servis.arac_kayit(scooter1)
servis.arac_kayit(scooter2)
servis.arac_kayit(scooter3)

scooter1.motoru_calistir()
scooter3.motoru_calistir() # Batarya yetersiz uyarisi verecek

print("\n" + "-" * 60)
print(" AKILLI BISIKLET SISTEMI TESTI")
print("-" * 60)
# id, durum, acilis_ucreti, dakika_ucreti, lokasyon
bisiklet1 = Bicycle(601, "Müsait", 5.0, 2.5, "Kutuphane")
bisiklet2 = Bicycle(602, "Müsait", 5.0, 2.5, "Sahil Yolu")
bisiklet3 = Bicycle(603, "Arızalı", 5.0, 2.5, "Yemekhane")

servis.arac_kayit(bisiklet1)
servis.arac_kayit(bisiklet2)
servis.arac_kayit(bisiklet3)

bisiklet1.motoru_calistir()

print("\n" + "-" * 60)
print("TRAMVAY HATTI TESTI")
print("-" * 60)
# id, durum, yakit, depo, kapasite, lokasyon
tramvay1 = Tramvay(701, "Müsait", 100, 100, 300, "Sultanahmet")
tramvay2 = Tramvay(702, "Müsait", 100, 100, 300, "Eminonu")
tramvay3 = Tramvay(703, "Arızalı", 100, 100, 300, "Topkapi")

servis.arac_kayit(tramvay1)
servis.arac_kayit(tramvay2)
servis.arac_kayit(tramvay3)

tramvay1.motoru_calistir()

print("\n" + "-" * 60)
print("METROBUS HATTI TESTI")
print("-" * 60)
# id, durum, plaka, kapasite, depo, yakit, lokasyon
metrobus1 = Metrobus(801, "Müsait", "34 BRT 01", 200, 300, 150, "Zincirlikuyu")
metrobus2 = Metrobus(802, "Seferde", "34 BRT 02", 200, 300, 200, "Avcilar")
metrobus3 = Metrobus(803, "Müsait", "34 BRT 03", 200, 300, 50, "Sogutlucesme")

servis.arac_kayit(metrobus1)
servis.arac_kayit(metrobus2)
servis.arac_kayit(metrobus3)

metrobus1.motoru_calistir()
# Static method testi
print(Metrobus.hat_ozelligi_goster())

print("\n" + "-" * 60)
print("VAPUR ISLETMESİ TESTI")
print("-" * 60)
# id, durum, yakit, depo, kapasite, gemi_ismi
vapur1 = Vapur(901, "Müsait", 600, 1000, 800, "Pasabahce")
vapur2 = Vapur(902, "Müsait", 750, 1000, 600, "Ada")
vapur3 = Vapur(903, "Müsait", 400, 1000, 500, "Sariyer")

servis.arac_kayit(vapur1)
servis.arac_kayit(vapur2)
servis.arac_kayit(vapur3)

vapur1.motoru_calistir()
vapur1.anons()

print("\n" + "-" * 60)
print("TELEFERIK SISTEMI TESTI")
print("-" * 60)
# id, durum, kabin, halat, fiyat, lokasyon
teleferik1 = Teleferik(1001, "Müsait", 20, 1500, 50.0, "Macka")
teleferik2 = Teleferik(1002, "Müsait", 30, 2000, 75.0, "Pierre Loti")
teleferik3 = Teleferik(1003, "Arızalı", 10, 800, 40.0, "Tepe")

servis.arac_kayit(teleferik1)
servis.arac_kayit(teleferik2)
servis.arac_kayit(teleferik3)

teleferik1.motoru_calistir()

print("\n" + "-" * 60)
print("DENIZ TAKSI TESTI")
print("-" * 60)
# id, durum, kapasite, acilis, km_ucret, yakit, lokasyon
deniztaksi1 = DenizTaksi(1101, "Müsait", 10, 200.0, 50.0, 120, "Bebek Iskele")
deniztaksi2 = DenizTaksi(1102, "Müsait", 8, 250.0, 60.0, 100, "Moda Iskele")
deniztaksi3 = DenizTaksi(1103, "Müsait", 10, 200.0, 50.0, 30, "Kanlica Iskele")

servis.arac_kayit(deniztaksi1)
servis.arac_kayit(deniztaksi2)
servis.arac_kayit(deniztaksi3)

deniztaksi1.motoru_calistir()

print("\n" + "-" * 60)
print("TURNIKE VE ODEME ALTYAPISI")
print("-" * 60)

# Farkli araclarda ornek bilet satislari
servis.turnike_odeme_yap(101, "Tuzla", "Pendik", "Yolcu 1")
servis.turnike_odeme_yap(301, "Otogar", "Yenikapi", "Yolcu 2")
servis.turnike_odeme_yap(201, "Ana Kampus", "Kuzey Kampus", "Ogrenci 1")
servis.turnike_odeme_yap(501, "Besiktas", "Ortakoy", "Turist 1")
servis.turnike_odeme_yap(901, "Kadikoy", "Besiktas", "Yolcu 3")
servis.turnike_odeme_yap(1101, "Bebek Iskele", "Adalar(MYO)", "Yolcu 4")

print("\n" + "-" * 60)
print("SEFER YONETIMI VE FILTRELEME")
print("-" * 60)

servis.sefer_baslat(102, "Kadikoy")
servis.sefer_baslat(302, "Taksim")
servis.sefer_baslat(902, "Adalar")

print("\n--- Aktif Seferler ---")
servis.aktif_seferleri_listele()

print("\nKapasite Sorgulama")
servis.uygun_arac_bul(50)

print("\nKapasite Sorgulama")
servis.uygun_arac_bul(1200)

print("\n" + "-" * 60)
print("TEST TAMAMLANDI")
print("-" * 60)

TransportVehicle.toplam_filo_sayisi()
TransportVehicle.filo_durum_kontrolu()

# Gun sonu raporu txt olarak cikti alinir
servis.gun_sonu_raporu_olustur()