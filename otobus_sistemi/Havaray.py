from base import TransportVehicle

class Havaray(TransportVehicle):
    def __init__(self, id, kapasite, durum, mevcut_lokasyon="Kuzey Kampüs"):
        super().__init__(id, kapasite, durum, mevcut_lokasyon)

        self.duraklar = [
            "Vadistanbul AVM",
            "Seyrantepe Metro Aktarma",
            "Kuzey Kampüs",
            "Kuzey Yurtlar Bölgesi",
            "Teknopark"
        ]
    
    def motoru_calistir(self):
        if self.durum == "Arızalı":
            print(f"❌ TEHLİKE: Havaray ({self.id}) sensör hatası! Güvenlik nedeniyle hareket edemez.")
            return
    
    def km_basina_maaliyet(self):
        return 15.5 #Henüz fiyatlandırma hakkında karar vermedim deney örneği.
    
    def motoru_kapat(self):
        return super().motoru_kapat()