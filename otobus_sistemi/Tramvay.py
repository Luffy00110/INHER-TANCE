from base import TransportVehicle

class Tramvay(TransportVehicle):
    def __init__(self, id, durum, mevcut_yakit, depo_limit, kapasite, mevcut_lokasyon="Ana Kampüs"):
        super().__init__(id, kapasite, durum, depo_limit, mevcut_yakit, mevcut_lokasyon)
        self.__duraklar = [
            "Ana Kampüs",
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
            "Kuzey Kampüs",
            "Aksaray",
            "Yusufpaşa",
            "Haseki",
            "Fındıkzade",
            "Çapa - Şehremini",
            "Kız Yurdu",
            "Pazartekki",
            "Topkapı",
            "Cevizlibağ",
            "Zeytinburnu",
            "Bağcılar",
            "Erkek Yurdu",
        ]
        self.__durak_arasi_km = 1  
        self.__km_ucreti = 2.0
    def motoru_calistir(self):
        # Arıza Kontrol
        if self.get_durum() == "Arızalı":
            print(f" ELEKTRİK HATASI: Tramvay ({self.get_id()}) katener hattından enerji alamıyor! Pantograf inik.")
            return
        super().motoru_calistir()
        print(f"Tramvay ({self.get_id()}) pantografı kaldırıldı. Motor hazır.")
    
    def motoru_kapat(self):
        super().motoru_kapat()
        print(f"Tramvay ({self.get_id()}) pantografı indirildi. Motor kapatıldı.")
        
    def km_basina_maaliyet(self):
        return 9.35
    
    def ucret_hesapla(self, binilen_durak, inilen_durak):
        giris_sirasi = -1
        durak_no = 0

        for durak in self.__duraklar:
            if durak == binilen_durak:
                giris_sirasi = durak_no
                break
            durak_no = durak_no + 1

        cikis_sirasi = -1  
        durak_no = 0       

        for durak in self.__duraklar:
            if durak == inilen_durak:
                cikis_sirasi = durak_no
                break
            durak_no = durak_no + 1
        
        if giris_sirasi == -1 or cikis_sirasi == -1:
            print("Girdiğiniz durak tramvay hattında bulunmuyor.")
            return 0, 0
        
        fark = 0
        if cikis_sirasi > giris_sirasi:
            fark = cikis_sirasi - giris_sirasi
        else:
            fark = giris_sirasi - cikis_sirasi

        toplam_km = fark * self.__durak_arasi_km
        toplam_ucret = toplam_km * self.__km_ucreti
        
        print(f"Tramvay Rota: {binilen_durak} -> {inilen_durak} ({fark} durak)")
        
        return toplam_ucret, fark