from base import TransportVehicle

#Shuttle Sınıfı
class Shuttle(TransportVehicle):
    def __init__(self, id, kapasite, durum, batarya_yuzdesi):
        super().__init__(id, kapasite, durum)
        self.batarya_yuzdesi = batarya_yuzdesi  # Shuttle'a özel özellik
        self.duraklar = ["Ana Kampüs", "Kuzey Kampüs"]
        self.km_ucreti = 0

    def motoru_calistir(self):
        if self.batarya_yuzdesi > 10:
            print(f"Shuttle {self.id} çalıştırıldı. Batarya: %{self.batarya_yuzdesi}")
        else:
            print(f"HATA: Shuttle {self.id} çalıştırılamadı! Batarya çok düşük.")

    def motoru_kapat(self):
        print(f"Shuttle {self.id} kontak kapattı!")
    #Türkiye geneline göre elektrikli araçların km başına maaliyetini araştırıp grup üyelerimizle beraber 2.35tlde karar kıldık.
    def km_basina_maaliyet(self):
        return 2.35
    
    def sarj_et(self):
        self.batarya_yuzdesi = 100
        print(f"Shuttle {self.id} şarj edildi. Batarya ful!")

    def ucret_hesapla(self, binilen_durak, inilen_durak):
        durak_var_mi = False
        if binilen_durak in self.duraklar and inilen_durak in self.duraklar:
            durak_var_mi = True
            
        if durak_var_mi == False:
            print("Hata: Shuttle sadece Ana ve Kuzey Kampüs arası gider.")
            return 0, 0
        if binilen_durak == inilen_durak:
            print("Zaten aynı kampüstesiniz.")
            return 0, 0
        
        print("Bilgi: Öğrenci shuttle servisi ücretsizdir.")
        return 0, 1