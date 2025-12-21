from base import TransportVehicle

class Metro(TransportVehicle):
    def __init__(self, id, kapasite, durum,binilen_durak,inilen_durak, mevcut_lokasyon="Ana Kampüs",hat_ismi="M1"):
        super().__init__(id, kapasite, durum, mevcut_lokasyon)
        self.hat_ismi = hat_ismi
        self.binilen_durak = binilen_durak
        self.inilen_durak = inilen_durak

        self.duraklar = [
            "Ana Kampüs"
            "Yenikapı",
            "Aksaray",
            "Emniyet - Fatih",
            "Topkapı - Ulubatlı",
            "Bayrampaşa - Maltepe",
            "Sağmalcılar",
            "Kocatepe",
            "Otogar",
            "Terazidere",
            "Kuzey Kampüs"
            "Davutpaşa - YTÜ",
            "Merter",
            "Zeytinburnu",
            "Kız Yurdu",
            "Bakırköy - İncirli",
            "Bahçelievler",
            "Ataköy - Şirinevler",
            "Yenibosna",
            "Erkek Öğrenci Yurdu"
            "DTM - İstanbul Fuar Merkezi",
            "Atatürk Havalimanı"
    ] #İstanbul M1 metro hattı duraklar ekstra olarak Ana Kampüs Kuzey Kampüs ve Yurtlar eklenmiştir
    def motoru_calistir(self):
        if self.durum == "Arızalı":
            print(f"❌ KRİTİK HATA: {self.hat_ismi} hattında sinyalizasyon arızası! Metro hareket edemez.")
            return
        
    def motoru_kapat(self):
        return super().motoru_kapat()
    
    def km_basina_maaliyet(self):
        return super().km_basina_maaliyet()
    
    def anons(self):
        print(f"Şuan {self.mevcut_lokasyon} konumunda bulunmaktasınız.")
        print(f"Sıradaki durak")
    
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