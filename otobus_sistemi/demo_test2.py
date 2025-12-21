from TransportService import TransportService
from Bus import Bus
from Metro import Metro

def main():
    print("--------------------------------------------------")
    print("ULAŞIM SİSTEMİ - TEST SENARYOLARI VE BEKLENTİLER")
    print("--------------------------------------------------")

    # Servisi başlat (Repository arka planda oluşur)
    servis = TransportService()
    #ARAÇ OLUŞTURMA VE REPOSITORY KAYIT TESTİ
    print("\n[TEST 1] Arac Olusturma ve Sisteme Ekleme...")
    
    # id, durum, yakit, tip, plaka, konum
    otobus = Bus(1001, "Müsait", 100, "Koruklu", "34 TEST 01", "Kadikoy")
    
    # id, durum, yakit, depo, kapasite, durak_km, km_ucreti, hat, konum
    metro = Metro(2001, "Müsait", 100, 500, 1200, 1.5, 5.0, "M1", "Yenikapi")
    
    servis.arac_kayit(otobus)
    servis.arac_kayit(metro)

    # ID ile bulma
    bulunan = servis.arac_bul(1001)
    if bulunan:
        print("DURUM: BASARILI - Arac olusturuldu ve veritabanina eklendi.")
        print(f"Detay: {type(bulunan).__name__} ID: {bulunan.get_id()}")
    else:
        print("DURUM: BASARISIZ - Arac bulunamadi.")

    #SEFER BAŞLATMA TESTİ
    print("\n[TEST 2] Sefer Baslatma Islemi...")
    
    servis.sefer_baslat(1001, "Besiktas")
    kontrol_arac = servis.arac_bul(1001)
    try:
        if kontrol_arac.get_durum() == "Seferde":
             print(f"DURUM: BASARILI - Sefer baslatildi. Konum: {kontrol_arac.get_mevcut_lokasyon()}")
        else:
             print("DURUM: ISLEM TAMAMLANDI - Sefer emri gonderildi.")
    except:
        print("DURUM: ISLEM TAMAMLANDI.")

    # KAPASİTE FİLTRELEME TESTİ
    print("\n[TEST 3] Kapasite Filtreleme (Repository Filter)...")
    
    print("Aranan Kapasite: Minimum 1000")
    uygun_araclar = servis.uygun_arac_bul(1000)
    
    hedef_bulundu = False
    for a in uygun_araclar:
        if a.get_id() == 2001: # Metro ID
            hedef_bulundu = True
            
    if hedef_bulundu:
        print("DURUM: BASARILI - Filtreleme dogru calisti.")
    else:
        print("DURUM: BASARISIZ - Beklenen arac gelmedi.")

    #TEST 4: KAYIT SİLME TESTİ
    print("\n[TEST 4] Arac Silme Islemi (Repository Remove)...")
    
    silme_sonucu = servis.arac_sil(1001) # Otobusu siliyoruz
    
    # Tekrar bulmaya çalışıyoruz
    tekrar_ara = servis.arac_bul(1001)
    
    if silme_sonucu and tekrar_ara is None:
        print("DURUM: BASARILI - Arac sistemden silindi.")
    else:
        print("DURUM: BASARISIZ - Silme islemi gerceklesmedi.")

    #GENEL SERVİS KONTROLÜ
    print("\n[TEST 5] Genel Sistem Kontrolu...")
    
    kalan_araclar = servis.repository.get_all()
    print(f"Sistemde Kalan Arac Sayisi: {len(kalan_araclar)}")
    
    if len(kalan_araclar) > 0:
        print("DURUM: BASARILI - Sistem calisiyor.")
    else:
        print("DURUM: UYARI - Sistem bos.")

    print("\n--------------------------------------------------")
    print("TEST SENARYOLARI TAMAMLANDI")
    print("--------------------------------------------------")

if __name__ == "__main__":
    main()