from base import TransportVehicle

class Havaray(TransportVehicle):
    def __init__(self, id, kapasite, durum, mevcut_yakit, depo_limit, durak_arasi_km, km_ucreti, mevcut_lokasyon="Kuzey Kampüs"):
        super().__init__(id, kapasite, durum, depo_limit, mevcut_yakit, mevcut_lokasyon)

        self.__duraklar = [
            "Kuzey Kampüs",
            "Vadistanbul AVM",
            "Seyrantepe Metro Aktarma",
            "Yemekhane",
            "Kuzey Yurtlar Bölgesi",
            "Teknopark",
            "Ana Kampüs"
        ]
        self.__durak_arasi_km = durak_arasi_km
        self.__km_ucreti = km_ucreti
    @classmethod
    def guvenlik_proseduru_goster(cls):
        return "Rüzgar hızı 50 km/s üzerindeyse sistem otomatik kilitlenir."
    
    @staticmethod
    def enerji_maliyeti_hesapla(mesafe_km):
        tuketim = mesafe_metre = mesafe_km * 9
        return f"{mesafe_km} KM yolculuk için tahmini {tuketim} kWh elektrik harcanır."
    
    def get_km_ucreti(self):
        return self.__km_ucreti
    
    def set_km_ucreti(self, yeni_ucret): 
        self.__km_ucreti = yeni_ucret

    def get_durak_arasi_km(self): 
        return self.__durak_arasi_km
    def set_durak_arasi_km(self, yeni_km): 
        self.__durak_arasi_km = yeni_km
    
    def motoru_calistir(self):
        if self.get_durum() == "Arızalı":
            print(f"Havaray ({self.get_id()}) sensör hatası! Güvenlik nedeniyle hareket edemez.")
            return
        print(f"Havaray ({self.get_id()}) raylar üzerinde askıya alındı. Sefer başlıyor.")
    
    def km_basina_maaliyet(self):
        return 15.5 #Henüz fiyatlandırma hakkında karar vermedim.
    
    def motoru_kapat(self):
        print(f"Havaray ({self.get_id()}) motoru kapattı.")
    
    def ucret_hesapla(self, binilen_durak, inilen_durak):
        try:
            giris_sirasi = self.__duraklar.index(binilen_durak)
            cikis_sirasi = self.__duraklar.index(inilen_durak)            
            fark = abs(cikis_sirasi - giris_sirasi)
            toplam_km = fark * self.get_durak_arasi_km()
            toplam_ucret = toplam_km * self.get_km_ucreti()
            
            return toplam_ucret, fark
            
        except ValueError:
            print("Havaray hattında böyle bir durak bulunamadı.")
            return 0, 0

    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"Sistem: Havaray F3 Hattı Formatı | Durak Sayısı: {len(self.__duraklar)}")