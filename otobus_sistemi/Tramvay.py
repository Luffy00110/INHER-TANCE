from base import TransportVehicle

class Tramvay(TransportVehicle):
    def __init__(self, id, kapasite, durum, mevcut_lokasyon="Ana Kampüs"):
        super().__init__(id, kapasite, durum, mevcut_lokasyon)
        self.duraklar = [
            "Ana Kampüs"
            "Kabataş",
            "Fındıklı",
            "Tophane",
            "Karaköy",
            "Eminönü",
            "Sirkeci",
            "Gülhane",
            "Sultanahmet",
            "Çemberlitaş",
            "Beyazıt - Kapalıçarşı",
            "Laleli - İstanbul Üni.",
            "Kuzey Kampüs"
            "Aksaray",
            "Yusufpaşa",
            "Haseki",
            "Fındıkzade",
            "Çapa - Şehremini",
            "Kız Yurdu"
            "Pazartekki",
            "Topkapı",
            "Cevizlibağ",
            "Zeytinburnu",
            "Bağcılar"
            "Erkek Yurdu"
        ]
        self.durak_arasi_km = 1  
        self.km_ucreti = 2.0
    def motoru_calistir(self):
        # Arıza Kontrol
        if self.durum == "Arızalı":
            print(f"❌ ELEKTRİK HATASI: Tramvay ({self.id}) katener hattından enerji alamıyor! Pantograf inik.")
            return
    
    def motoru_kapat(self):
        return super().motoru_kapat()
    
    def km_basina_maaliyet(self):
        return 9.35
    
    def ucret_hesapla(self, binilen_durak,inilen_durak):
        giris_sirasi = -1
        durak_no = 0

        for durak in self.duraklar:
            if durak == binilen_durak:
                giris_sirasi = durak_no
                break
            durak_no = durak_no + 1
        
        cikis_sirasi = durak_no
        durak_no = 0

        for durak in self.duraklar:
            if durak == inilen_durak:
                cikis_sirasi = durak_no
                break
            durak_no = durak_no + 1
        
        if giris_sirasi == -1 or cikis_sirasi == -1:
            print("Hata: Böyle bir durak ismi listede yok.")
            return 0, 0
        
        fark = 0
        if cikis_sirasi > giris_sirasi:
            fark = cikis_sirasi - giris_sirasi
        else:
            fark = giris_sirasi - cikis_sirasi

        toplam_km = fark * self.durak_arasi_km
        toplam_ucret = toplam_km * self.km_ucreti
        
        return toplam_ucret, fark