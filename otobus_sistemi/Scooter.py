from base import TransportVehicle

class Scooter(TransportVehicle):
    def __init__(self, id, durum, batarya_yuzdesi, durak_arasi_km, km_ucreti, acilis_ucreti, mevcut_lokasyon="Ana Kampüs"):
        super().__init__(id, 1, durum, 100, batarya_yuzdesi, mevcut_lokasyon)
        self.__batarya_yuzdesi = batarya_yuzdesi
        self.__durak_arasi_km = durak_arasi_km
        self.__km_ucreti = km_ucreti
        self.__acilis_ucreti = acilis_ucreti
        self.__duraklar = ["Erkek Yurdu", "Yemekhane", "Kütüphane", "Kuzey Kampüs", "Spor Salonu", "Ana Kampüs", "Kız Yurdu"]
    @classmethod
    def kullanim_kurali_goster(cls):   
        return "lektrikli scooter kullanımı için yasal yaş sınırı 15'tir. Kask takılması önerilir."
    
    @staticmethod
    def tahmini_varis_suresi(mesafe_km):
        ortalama_hiz = 20 # şehir içi ortalama hız 20km/s    
        # Süre (Saat) = Yol / Hız
        sure_saat = mesafe_km / ortalama_hiz    
        # Dakikaya çevir
        sure_dakika = int(sure_saat * 60)       
        return f"{mesafe_km} km yol, scooter ile yaklaşık {sure_dakika} dakika sürer."
        
    def get_batarya_yuzdesi(self):
        return self.__batarya_yuzdesi

    def set_batarya_yuzdesi(self, yeni_yuzde):
        if 0 <= yeni_yuzde <= 100:
            self.__batarya_yuzdesi = yeni_yuzde
            self.set_mevcut_yakit(yeni_yuzde)
        else:
            print("Batarya yüzdesi 0-100 arasında olmalıdır!")
    
    def get_km_ucreti(self):
        return self.__km_ucreti

    def set_km_ucreti(self, yeni_fiyat):
        if yeni_fiyat >= 0:
            self.__km_ucreti = yeni_fiyat
        else:
            print("Ücret negatif olamaz!")

    def get_acilis_ucreti(self):
        return self.__acilis_ucreti

    def set_acilis_ucreti(self, yeni_fiyat):
        if yeni_fiyat >= 0:
            self.__acilis_ucreti = yeni_fiyat
        else:
            print("Hata açılış ücreti negatif olamaz! ")
            
    def get_durak_arasi_km(self):
        return self.__durak_arasi_km

    def set_durak_arasi_km(self, yeni_mesafe):
        if yeni_mesafe > 0:
            self.__durak_arasi_km = yeni_mesafe
        else:
            print("Duraklar arası mesafe negatif olamaz!")
    
    def motoru_calistir(self):
        if self.get_batarya_yuzdesi() <= 10:
            print("Batarya yüzdesi çok düşük! Scooter çalıştırılamadı!")
        else:
            print("Scooter çalıştırıldı! Güvenliğiniz için kaskınızı ve ekipmanlarınızı takmayı unutmayın...")
    
    def motoru_kapat(self):
        print("Scooter motoru başarıyla kapatıldı. Lütfen özel eşyaları yanınıza aldığınızdan emin olun...")
        
    def km_basina_maaliyet(self):
        return 0.58
    
    def sarj_et(self):
        self.set_batarya_yuzdesi(100)
        print("Batarya şarj edildi.")

    def ucret_hesapla(self, binilen_durak, inilen_durak):
        #Pil Kontrolü
        if self.get_batarya_yuzdesi() < 10:
            print("Bu scooter'ın şarjı bitmiş, kullanamazsın.")
            return 0, 0

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
            print("Konum bulunamadı.")
            return 0, 0

        # Mesafenin hesaplanması
        fark = 0
        if cikis_sirasi > giris_sirasi:
            fark = cikis_sirasi - giris_sirasi
        else:
            fark = giris_sirasi - cikis_sirasi 

        # Ücretlerin hesapşanması
        toplam_km = fark * self.get_durak_arasi_km()
        # Açılış Ücreti + (Gidilen Yol * Km başına ücret)
        toplam_ucret = self.get_acilis_ucreti() + (toplam_km * self.get_km_ucreti())
        
        #Pil uyarı
        harcanan_sarj = fark * 5
        self.set_batarya_yuzdesi(self.get_batarya_yuzdesi() - harcanan_sarj)
        
        print(f"Pil %{harcanan_sarj} azaldı. Kalan Pil: %{self.get_batarya_yuzdesi()}")

        return toplam_ucret, fark