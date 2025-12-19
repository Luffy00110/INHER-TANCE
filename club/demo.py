from base import Club
from repository import ClubRepository
from implementations import ClubService, ClubEvent, SportClub, MusicClub, ScienceClub
from datetime import datetime


# AKILLI KAMPÜS SİSTEMİ  DEMO


def main():
    print("   KULÜP YÖNETİM SİSTEMİ BAŞLATILIYOR...   ")
    
    # 1. ALTYAPI HAZIRLIĞI
    #  depoyu  ve servisi hazırlıyoruz
    depo = ClubRepository()
    servis = ClubService(depo)

    # Genel Kurallar (Static Method Testi)
    print("\n BİLGİ Okul Kuralları Kontrol Ediliyor...")
    Club.genel_kurallar()
  
    # 2. KULÜPLERİN OLUŞTURULMASI   
    print("\n\n ADIM 1: KULÜPLER KURULUYOR")
    
    # Spor Kulübü Kuruyoruz 
    k1 = servis.create_club("Spor", "Kampus Kartallari", "Futbol Takımı", brans="Futbol", saha="Halı Saha")
    
    # Müzik Kulübü Kuruyoruz
    k2 = servis.create_club("Muzik", "Genc Sesler", "Okul Korosu", tur="Pop Müzik")
    
    # Bilim Kulübü Kuruyoruz
    k3 = servis.create_club("Bilim", "Robotik", "Robot Yapımı", lab=True)

    # Hatalı Giriş Testi 
    print("   -> Hatalı isim testi yapılıyor...")
    servis.create_club("Spor", "A", "Bu oluşmamalı") 
   
    # 3. ÜYE EKLEME İŞLEMLERİ

    print("\n\n ADIM 2: ÖĞRENCİLER KAYDEDİLİYOR")

    # Kampüs Kartallarına üye ekleyelim
    servis.add_member("Kampus Kartallari", "Bekirkan Kılıç")
    servis.add_member("Kampus Kartallari", "Mehmet Özer")
    
    # Genç Seslere üye ekleyelim
    servis.add_member("Genc Sesler", "Ege Ünal ")
    
    # Robotik kulübüne üye ekleyelim
    servis.add_member("Robotik", "Elon Musk")

    # Olmayan kulübe ekleme yapmaya çalışalım (Hata mesajını görmek için)
    servis.add_member("Satranç Kulübü", "Veli")

    # 4. ETKİNLİK OLUŞTURMA (ClubEvent Kullanımı)

    print("\n\n ADIM 3: ETKİNLİKLER PLANLANIYOR")
    
    simdi = datetime.now()
    
    # Manuel etkinlik oluşturuyoruz
    mac_etkinligi = ClubEvent("Bahar Turnuvası", "Kampus Kartallari", "Stadyum", 100, simdi)
    
    # Etkinliği depoya kaydediyoruz
    depo.save_event(mac_etkinligi)
    
    # Etkinliğe öğrenci kaydı yapalım
    mac_etkinligi.katilimci_ekle("Ahmet Yilmaz")
    mac_etkinligi.katilimci_ekle("Mehmet Özer")
    
    print(f"-> '{mac_etkinligi.title}' etkinliği sisteme girildi.")

    # 5. RAPORLAMA VE POLİMORFİZM TESTİ
    # (Her kulüp kendi özelliğine göre bilgi verecek)

    print("\n\n ADIM 4: SİSTEM RAPORU (Polimorfizm)")
    
    tum_kulupler = depo.list_all_clubs()
    
    for kulup in tum_kulupler:
        print(f"\n KULÜP: {kulup.name}")
        print(f" - Açıklama: {kulup.description}")
        print(f" - Üye Sayısı: {kulup.member_count}")
        # Burası Polimorfizm  örneği:
        # Her kulüp tipi aşağıdaki soruyu farklı cevaplar:
        print(f" - Etkinlik Tipi: {kulup.etkinlik_tipi_belirle()}")
        print(f" - Kabul Şartı: {kulup.uye_kabul_sartlari()[0]}")

    print("   DEMO BAŞARIYLA TAMAMLANDI   ")


if __name__ == "__main__":
    main()
