from base import TransportVehicle

class Metrobus(TransportVehicle):
    def __init__(self, id, durum, plaka, kapasite, depo_limit, mevcut_yakit, mevcut_lokasyon):
        super().__init__(id, kapasite, durum, depo_limit, mevcut_yakit, mevcut_lokasyon)
        self.__plaka = plaka
        self.__acilis_ucreti = 10.00
        self.__durak_basi_ucret = 2.50
        self.__duraklar = [
            "Kız Yurdu", 
            "Ana Kampüs", 
            "Erkek Yurdu", 
            "Kadıköy İskelesi", 
            "Kuzey Kampüs"
        ]
        if mevcut_lokasyon not in self.__duraklar:
            print(f"{mevcut_lokasyon} durağı Metrobüs hattında yok! (Varsayılan duraklar: {self.__duraklar})")
    
    @classmethod
    def hat_ozelligi_goster(cls):
        return "Metrobüs trafiğe kapalı özel şeritlerde 7/24 hizmet verir."
    
    @staticmethod
    def yogunluk_tahmini(saat):
        if (7 <= saat <= 9) or (17 <= saat <= 19):
            return "Tahmini Doluluk: %100 "
        elif (10 <= saat <= 16):
            return "Tahmini Doluluk: %60 "
        else:
            return "Tahmini Doluluk: %20 "

    def get_plaka(self):
        return self.__plaka
    
    def set_plaka(self, yeni_plaka):
        self.__plaka = yeni_plaka
        print(f"Plaka güncellendi  {self.__plaka}")

    def get_durak_listesi(self):
        return self.__duraklar

    def get_ucret_tarifesi(self):
        return f"Açılış: {self.__acilis_ucreti} TL + Durak Başı: {self.__durak_basi_ucret} TL"


    def motoru_calistir(self):
        if self.get_durum() == "Arızalı":
            print(f" {self.get_id()} nolu Metrobüs arızalı!")
            return
        
        super().motoru_calistir()
        print(f" ({self.__plaka}) motoru çalıştı. İstikamet: {self.get_mevcut_lokasyon()}")

    def motoru_kapat(self):
        super().motoru_kapat()
        print(f"Metrobüs ({self.__plaka}) motoru kapattı.")

    def km_basina_maaliyet(self):
        return 12.5 
    
    def ucret_hesapla(self, binilen_durak, inilen_durak):
        if binilen_durak not in self.__duraklar or inilen_durak not in self.__duraklar:
            print("Bu durak Metrobüs hattında mevcut değil!")
            return 0, 0
        
        giris_index = self.__duraklar.index(binilen_durak)
        cikis_index = self.__duraklar.index(inilen_durak)
        
        durak_sayisi = abs(cikis_index - giris_index)
        
        if durak_sayisi == 0:
            print("Aynı durakta indiniz, ücret yansımadı.")
            return 0, 0
            
        toplam_ucret = self.__acilis_ucreti + (durak_sayisi * self.__durak_basi_ucret)
        
        print(f"Rota: {binilen_durak} -> {inilen_durak} ({durak_sayisi} Durak)")
        return toplam_ucret, durak_sayisi

    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"Plaka: {self.__plaka}")
        print(f"Hat: {self.__duraklar[0]} <---> {self.__duraklar[-1]}")