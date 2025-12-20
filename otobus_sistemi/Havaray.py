from base import TransportVehicle

class Havaray(TransportVehicle):
    def __init__(self, id, kapasite, durum, mevcut_lokasyon="Kuzey Kampüs"):
        super().__init__(id, kapasite, durum, mevcut_lokasyon)

        self.duraklar = [
            "Kuzey Kampüs",
            "Vadistanbul AVM",
            "Seyrantepe Metro Aktarma",
            "Yemekhane"
            "Kuzey Yurtlar Bölgesi",
            "Teknopark"
            "Ana Kampüs"
        ]
        self.durak_arasi_km = 0.7   #Girilen veriler istanbul f3 havaray hattına göre alınmıştır.
        self.km_ucreti = 3,46
    
    def motoru_calistir(self):
        if self.durum == "Arızalı":
            print(f"❌ TEHLİKE: Havaray ({self.id}) sensör hatası! Güvenlik nedeniyle hareket edemez.")
            return
    
    def km_basina_maaliyet(self):
        return 15.5 #Henüz fiyatlandırma hakkında karar vermedim deney örneği.
    
    def motoru_kapat(self):
        return super().motoru_kapat()
    
    def ucret_hesapla(self, binilen_durak,inilen_durak):
        giris_sirasi = -1
        durak_no = 0

        for durak in self.duraklar:
            if durak == binilen_durak:
                giris_sirasi = durak_no
                break
            durak_no = durak_no + 1
        
        cikis_sirasi = durak_no
        durak_no = 0

        for durak in self.duraklar:
            if durak == inilen_durak:
                cikis_sirasi = durak_no
                break
            durak_no = durak_no + 1
        
        if giris_sirasi == -1 or cikis_sirasi == -1:
            print("Hata: Böyle bir durak ismi listede yok.")
            return 0, 0
        
        fark = 0
        if cikis_sirasi > giris_sirasi:
            fark = cikis_sirasi - giris_sirasi
        else:
            fark = giris_sirasi - cikis_sirasi

        toplam_km = fark * self.durak_arasi_km
        toplam_ucret = toplam_km * self.km_ucreti
        
        return toplam_ucret, fark