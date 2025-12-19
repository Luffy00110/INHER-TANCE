from base import TransportVehicle

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