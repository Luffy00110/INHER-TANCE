from base import TransportVehicle

class Scooter(TransportVehicle):
    def __init__(self, id, durum, batarya_yuzdesi, mevcut_lokasyon="Ana Kampüs",):
        self.batarya_yuzdesi = batarya_yuzdesi
        super().__init__(id, durum,batarya_yuzdesi, mevcut_lokasyon)
        self.duraklar = ["Erkek Yurdu", "Yemekhane", "Kütüphane", "Kuzey Kampüs", "Spor Salonu", "Ana Kampüs","Kız Yurdu"]      
        self.durak_arasi_km = 1   
        self.km_ucreti = 4.5
        self.acilis_ucreti = 15
        self.batarya = 100        

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

    def ucret_hesapla(self, binilen_durak, inilen_durak):
        #Pil Kontrolü
        if self.batarya < 10:
            print("❌ Hata: Bu scooter'ın şarjı bitmiş, kullanamazsın.")
            return 0, 0

        giris_sirasi = -1 
        durak_no = 0
        for durak in self.duraklar:
            if durak == binilen_durak:
                giris_sirasi = durak_no
                break 
            durak_no = durak_no + 1
            
        cikis_sirasi = -1
        durak_no = 0
        for durak in self.duraklar:
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
        toplam_km = fark * self.durak_arasi_km
        # Açılış Ücreti + (Gidilen Yol * Km başına ücret)
        toplam_ucret = self.acilis_ucreti + (toplam_km * self.km_ucreti)
        
        #Pil uyarı
        harcanan_sarj = fark * 5
        self.batarya = self.batarya - harcanan_sarj
        
        print(f"🔋 Pil %{harcanan_sarj} azaldı. Kalan Pil: %{self.batarya}")

        return toplam_ucret, fark