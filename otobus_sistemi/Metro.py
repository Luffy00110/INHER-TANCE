from base import TransportVehicle

class Metro(TransportVehicle):
    def __init__(self, id, durum, mevcut_yakit, depo_limit, kapasite, durak_arasi_km, km_ucreti, hat_ismi, mevcut_lokasyon="Ana Kampüs"):
        super().__init__(id, kapasite, durum, depo_limit, mevcut_yakit, mevcut_lokasyon)
        self.__hat_ismi = hat_ismi
        self.__durak_arasi_km = durak_arasi_km
        self.__km_ucreti = km_ucreti

        self.duraklar = [
            "Ana Kampüs",
            "Yenikapı",
            "Aksaray",
            "Emniyet - Fatih",
            "Topkapı - Ulubatlı",
            "Bayrampaşa - Maltepe",
            "Sağmalcılar",
            "Kocatepe",
            "Otogar",
            "Terazidere",
            "Kuzey Kampüs",
            "Davutpaşa - YTÜ",
            "Merter",
            "Zeytinburnu",
            "Kız Yurdu",
            "Bakırköy - İncirli",
            "Bahçelievler",
            "Ataköy - Şirinevler",
            "Yenibosna",
            "Erkek Öğrenci Yurdu",
            "DTM - İstanbul Fuar Merkezi",
            "Atatürk Havalimanı"
    ] #İstanbul M1 metro hattı duraklar ekstra olarak Ana Kampüs Kuzey Kampüs ve Yurtlar eklenmiştir
    @classmethod
    def calisma_saatleri_goster(cls):
       
        return "Metro Çalışma Saatleri: 06:00 - 00:00 (Hafta sonu 24 saat)"
    staticmethod
    def tahmini_sure_hesapla(durak_sayisi):
        sure = durak_sayisi * 2.5
        return f"{durak_sayisi} durak için tahmini varış süresi: {sure} dakika."
    
    def motoru_calistir(self):
        if self.get_durum() == "Arızalı":
            print(f"{self.__hat_ismi} hattında sinyalizasyon arızası! Metro hareket edemez.")
            return
        super().motoru_calistir()
        print(f"Metro ({self.get_id()}) sefere başladı.")
        
    def motoru_kapat(self):
        super().motoru_kapat()
        print(f"Metro ({self.get_id()}) motor kapattı.")
    
    def km_basina_maaliyet(self):
        return  25.75
    
    def anons(self):
        print(f"Sayın yolcularımız lütfen araçtan ayrılırken değerli eşyalarınızı yanınıza almayı unutmayınız. İyi yolculuklar dileriz!")
    
    def ucret_hesapla(self, binilen_durak, inilen_durak):
        giris_sirasi = -1
        cikis_sirasi = -1

        durak_no = 0
        for durak in self.duraklar:
            if durak == binilen_durak:
                giris_sirasi = durak_no
            if durak == inilen_durak:
                cikis_sirasi = durak_no
            durak_no += 1

        if giris_sirasi == -1 or cikis_sirasi == -1:
            print("Böyle bir durak ismi listede yok.")
            return 0, 0

        fark = abs(cikis_sirasi - giris_sirasi)
        toplam_km = fark * self.__durak_arasi_km
        toplam_ucret = toplam_km * self.__km_ucreti

        return toplam_ucret, fark