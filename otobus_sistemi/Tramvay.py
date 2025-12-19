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
    def motoru_calistir(self):
        # 1. ARIZA KONTROLÜ
        if self.durum == "Arızalı":
            print(f"❌ ELEKTRİK HATASI: Tramvay ({self.id}) katener hattından enerji alamıyor! Pantograf inik.")
            return
    
    def motoru_kapat(self):
        return super().motoru_kapat()
    
    def km_basina_maaliyet(self):
        return 9.35