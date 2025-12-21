from abc import ABC, abstractmethod


class TransportVehicle(ABC):
    def __init__(self, id, kapasite, durum, mevcut_lokasyon="Ana Kampüs"):
        self.id = id
        self.kapasite = kapasite
        self.durum = durum
        self.mevcut_lokasyon = mevcut_lokasyon

    @abstractmethod
    def motoru_calistir(self):
        pass

    @abstractmethod
    def motoru_kapat(self):
        pass
    @abstractmethod
    def ucret_hesapla(self, giris, cikis):
        pass

    @staticmethod #ID kontrolu yapma 
    def id_kontrol(arac_id):
        if isinstance(arac_id, int) and arac_id > 0:
            return True
        return False
    
    @classmethod
    def toplam_filo_sayisi(sinif):
        print(f"Sistemdeki Toplam Araç: {sinif.toplam_arac_sayisi}")
    @classmethod
    def filo_durum_kontrolu(sinif):
        # Örnek bir limit koyalım, mesela 5 araçtan fazlaysa uyarı versin
        limit = 5 
        if sinif.toplam_arac_sayisi >= limit:
            print(f"UYARI: Filo çok kalabalık! ({sinif.toplam_arac_sayisi} araç var.)")
        else:
            print(f"Sistem rahat, yeni araç eklenebilir. ({sinif.toplam_arac_sayisi} araç var.)")

    @abstractmethod
    def km_basina_maaliyet(self):
        pass
    def bilgi_ver(self):
        print(f"Araç ID: {self.id}")
        print(f"Durum: {self.durum}")
        print(f"Konum: {self.mevcut_lokasyon}")
        print(f"Kapasite: {self.kapasite}")
        
    def ariza_yap(self):
        self.durum = "Arızalı"
        print(f"ALARM: {self.id} numaralı araç ARIZA YAPTI! Sistem dışı.")

    def tamir_et(self):
        if self.durum == "Arızalı":
            print("Araç servise alındı, tamir ediliyor...")
            self.durum = "Müsait" 
            print(f"{self.id} numaralı araç tamir edildi. Tekrar göreve hazır.")
        else:
            print(f"ℹ{self.id} numaralı araç zaten sağlam, tamire gerek yok!.")


