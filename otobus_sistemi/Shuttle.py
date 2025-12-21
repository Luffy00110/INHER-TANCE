from base import TransportVehicle

#Shuttle Sınıfı
class Shuttle(TransportVehicle):
    def __init__(self, id, kapasite, durum, batarya_yuzdesi, mevcut_lokasyon="Ana Kampüs"):
        super().__init__(id, kapasite, durum, 100, batarya_yuzdesi, mevcut_lokasyon) 
        self.__batarya_yuzdesi = batarya_yuzdesi
        self.__duraklar = ["Ana Kampüs", "Kuzey Kampüs"]
        self.__km_ucreti = 0
        
    @staticmethod
    def servis_saati_mi(saat):
        return 8 <= saat <= 24

    @classmethod
    def servis_tipi(cls):
        return "Ücretsiz Kampüs İçi Personel/Öğrenci Servisi"
    
    #Türkiye geneline göre elektrikli araçların km başına maaliyetini araştırıp grup üyelerimizle beraber 2.35tlde karar kıldık.
    def km_basina_maaliyet(self):
        return 2.35
    
    def get_batarya_yuzdesi(self):
        return self.__batarya_yuzdesi

    def set_batarya_yuzdesi(self, yeni_yuzde):
        if 0 <= yeni_yuzde <= 100:
            self.__batarya_yuzdesi = yeni_yuzde
            self.set_mevcut_yakit(yeni_yuzde)
        else:
            print("Batarya yüzdesi 0 ile 100 arasında olmalıdır!")
    
    def sarj_et(self):
        self.set_batarya_yuzdesi(100)
        print(f"Shuttle {self.get_id()} şarj edildi. Batarya ful!")
    
    def motoru_calistir(self):
        if self.get_batarya_yuzdesi() > 10:
            super().motoru_calistir()
            print(f"Shuttle {self.get_id()} çalıştırıldı. Batarya: %{self.get_batarya_yuzdesi()}")
        else:
            print(f"HATA: Shuttle {self.get_id()} çalıştırılamadı! Batarya çok düşük.")

    def motoru_kapat(self):
        super().motoru_kapat()
        print(f"Shuttle {self.get_id()} kontak kapattı!")

    def ucret_hesapla(self, binilen_durak, inilen_durak):
        durak_var_mi = False
        if binilen_durak in self.__duraklar and inilen_durak in self.__duraklar:
            durak_var_mi = True
            
        if durak_var_mi == False:
            print("Hata: Shuttle sadece Ana ve Kuzey Kampüs arası gider.")
            return 0, 0
        if binilen_durak == inilen_durak:
            print("Zaten aynı kampüstesiniz.")
            return 0, 0
        
        print("Bilgi: Öğrenci shuttle servisi ücretsizdir.")
        return 0, 1
    
    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"Batarya Durumu: %{self.get_batarya_yuzdesi()}")