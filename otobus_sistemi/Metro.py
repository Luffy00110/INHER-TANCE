from base import TransportVehicle

class Metro(TransportVehicle):
    def __init__(self, id, kapasite, durum, mevcut_lokasyon="Ana Kampüs",hat_ismi="M1"):
        super().__init__(id, kapasite, durum, mevcut_lokasyon)
        self.hat_ismi = hat_ismi

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