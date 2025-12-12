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
#Shuttle Sınıfı
class Shuttle(TransportVehicle):
    def __init__(self, id, kapasite, durum, batarya_yuzdesi):
        super().__init__(id, kapasite, durum)
        self.batarya_yuzdesi = batarya_yuzdesi  # Shuttle'a özel özellik

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
#Belediye otobüsü
class Bus(TransportVehicle):
    def __init__(self, id, durum, otobus_tipi="Standart"):
        # Otobüs tipine göre kapasite ve km başına yaktığı tl cinsinini hesapladık. Yolcu sayısını hesaplarken oturan ve ayakta giden yoluların toplamını aldık.
        if otobus_tipi == "Koruklu":
            kapasite = 163
            yakit_tuketimi = 26.70   
        else:
            kapasite = 102
            yakit_tuketimi = 15.575

        super().__init__(id, kapasite, durum)
        
        self.otobus_tipi = otobus_tipi
        self.yakit_tuketimi_degeri = yakit_tuketimi

    def motoru_calistir(self):
        return super().motoru_calistir()    
    
    def motoru_kapat(self):
        return super().motoru_kapat()
    
    def km_basina_maaliyet(self):
        return self.yakit_tuketimi_degeri
class Scooter(TransportVehicle):
    def __init__(self, id, durum, batarya_yuzdesi, mevcut_lokasyon="Ana Kampüs",):
        self.batarya_yuzdesi = batarya_yuzdesi
        super().__init__(id, durum,batarya_yuzdesi, mevcut_lokasyon)

    def motoru_calistir(self):
        if self.batarya_yuzdesi <= 10:
            print("Batarya yüzdesi çok düşük! Scooter çalıştırılamadı!")
        else:
            print("Scooter çalıştırıldı! Güvenliğiniz için kaskınızı ve ekipmanlarınızı takmayı unutmayın...")
    
    def motoru_kapat(self):
        return super().motoru_kapat()
    
    def km_basina_maaliyet(self):
        return 0.58
    
    def sarj_et(self):
        self.batarya_yuzdesi = 100
        print("Batarya şarj edildi.")
class Bicyle(TransportVehicle): #Bisiklet ksımı şimdilik sadece ücret eklenmiştir bunun dışında kart ödeme kısmı vs de eklenecektir.
    def __init__(self, id,durum, mevcut_lokasyon="Ana Kampüs"):
        super().__init__(id, durum, mevcut_lokasyon)

    def sistemi_calistir(self):
        print("Bisiklet ulaşım sitemini çalıştırdınız.")
    
    def sistemi_durdur(self):
        print("Bisiklet ulaşım sistemini sonlandırdınız.")
    
    def km_basina_maaliyet(self):
        return 0.15

