from base import Club
from datetime import datetime, timedelta
import random
# Etkinlik verileri:
class ClubEvent:
    #Kulüplerin düzenlediği etkinlikleri temsil eden sınıf.
    
    def __init__(self, title: str, club_name: str, location: str, quota: int, date_time: datetime):
        self.event_id = random.randint(1000, 9999)
        self.title = title
        self.club_name = club_name
        self.location = location
        self.quota = quota
        self.date_time = date_time
        self.attendees = []  # Katılımcı listesi
        self.is_active = True

    def katilimci_ekle(self, ogrenci_adi: str) -> bool:
        if len(self.attendees) >= self.quota:
            print(f"DOLU '{self.title}' için yer yok.")
            return False
        self.attendees.append(ogrenci_adi)
        print(f"KAYIT {ogrenci_adi} -> {self.title} etkinliğine eklendi.")
        return True


# 2. SUBCLASSES: ALT SINIFLAR (Inheritance)


class SportClub(Club):
    def __init__(self, name, description, brans, saha):
        # Base class'a varsayılan değerleri gönderiyoruz (0 üye, şu anki tarih)
        super().__init__(name, 0, description, datetime.now())
        self.brans = brans
        self.antrenman_sahasi = saha

    # Abstract Metot 1 
    def uye_kabul_sartlari(self) -> list:
        return ["Sağlık raporu", "Spor kıyafeti", "Antrenman disiplini"]

    # Abstract Metot 2 
    def etkinlik_tipi_belirle(self) -> str:
        return "Turnuva ve Maç"

    # Ekstra Metot
    def antrenman_planla(self, saat):
        print(f"SPOR {self.name}, {self.antrenman_sahasi} sahasında {saat} antrenmanı yapacak.")


class MusicClub(Club):
    def __init__(self, name, description, muzik_turu):
        super().__init__(name, 0, description, datetime.now())
        self.muzik_turu = muzik_turu

    def uye_kabul_sartlari(self) -> list:
        return ["Müzik kulağı testi", "Enstrüman yeteneği"]

    def etkinlik_tipi_belirle(self) -> str:
        return "Konser ve Dinleti"


class ScienceClub(Club):
    def __init__(self, name, description, lab_var_mi: bool):
        super().__init__(name, 0, description, datetime.now())
        self.lab_var_mi = lab_var_mi

    def uye_kabul_sartlari(self) -> list:
        return ["Not ortalaması 2.50+", "Bilimsel merak"]

    def etkinlik_tipi_belirle(self) -> str:
        return "Hackathon ve Proje Sunumu"



# 3. SERVICE KATMANI (İş Mantığı)

class ClubService:
    def __init__(self, repository):
        self.repo = repository

    def create_club(self, type_str: str, name: str, desc: str, **detaylar):
        
        #Yeni bir kulüp oluşturur ve repository'e kaydeder.
        
        print(f"\n SERVİS Kulüp oluşturuluyor: {name}...")
        
        if not Club.isim_kontrol(name):
            return None

        yeni_kulup = None
        
        if type_str == "Spor":
            yeni_kulup = SportClub(name, desc, detaylar.get("brans"), detaylar.get("saha"))
        elif type_str == "Muzik":
            yeni_kulup = MusicClub(name, desc, detaylar.get("tur"))
        elif type_str == "Bilim":
            yeni_kulup = ScienceClub(name, desc, detaylar.get("lab"))
        
        if yeni_kulup:
            self.repo.save_club(yeni_kulup)
            print(f"BAŞARILI {yeni_kulup.name} oluşturuldu ve kaydedildi.")
            return yeni_kulup
        else:
            print("HATA Geçersiz kulüp türü.")
            return None

    def add_member(self, club_name: str, member_name: str):
        
        #Var olan bir kulübe üye ekler
        #Artık bu fonksiyon daha akıllı: Kontroller yapıyor
        
        print(f"\n İŞLEM '{club_name}' kulübüne '{member_name}' ekleniyor")

        # 1. KONTROL: İsmin boş olup olmadığını kontrol etmek için olan yer
        if not member_name or len(member_name) < 3:
            print(f"HATA Üye ismi çok kısa veya geçersiz: '{member_name}'")
            return

        # 2. KONTROL: Kulüp var mı onu kontrol eder
        kulup = self.repo.find_club_by_name(club_name)
        if not kulup:
            print(f"HATA '{club_name}' isminde bir kulüp sistemde bulunamadı.")
            return

        # 3. KONTROL: Kapasite kontrolü (Simülasyon)
        # Örneğin bir kulüp en fazla 50 kişi olsun diyelim.
        max_kapasite = 50
        if kulup.member_count >= max_kapasite:
            print(f"DOLU {kulup.name} kulübü maksimum kapasiteye ({max_kapasite}) ulaştı.")
            return

        # 4. İŞLEM BAŞARILI
        eski_uye_sayisi = kulup.member_count
        kulup.uye_sayisi_guncelle(eski_uye_sayisi + 1)
        
        # İşlem özeti yazdır
        print(f"BAŞARILI  {member_name} başarıyla eklendi.")
        print(f"-> Kulüp: {kulup.name}")
        print(f"-> Yeni Mevcut: {kulup.member_count} Üye")
            