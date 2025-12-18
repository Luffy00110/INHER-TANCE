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
    def km_basina_maaliyet(self):
        pass
    def bilgi_ver(self):
        print(f"Araç ID: {self.id}")
        print(f"Durum: {self.durum}")
        print(f"Konum: {self.mevcut_lokasyon}")
        print(f"Kapasite: {self.kapasite}")
        
    def ariza_yap(self):
        self.durum = "Arızalı"
        print(f"⚠️  ALARM: {self.id} numaralı araç ARIZA YAPTI! Sistem dışı.")

    def tamir_et(self):
        if self.durum == "Arızalı":
            print("🛠️  Araç servise alındı, tamir ediliyor...")
            self.durum = "Müsait" 
            print(f"✅ {self.id} numaralı araç tamir edildi. Tekrar göreve hazır.")
        else:
            print(f"ℹ️  {self.id} numaralı araç zaten sağlam, tamire gerek yok!.")


