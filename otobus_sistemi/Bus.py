from base import TransportVehicle

class Bus(TransportVehicle):
    def __init__(self, id, durum, mevcut_yakit, otobus_tipi="Standart", plaka="", mevcut_lokasyon="Ana Kampüs"):
        # Otobüs tipine göre kapasite ve km başına yaktığı tl cinsinini hesapladık. Yolcu sayısını hesaplarken oturan ve ayakta giden yoluların toplamını aldık.
        if otobus_tipi == "Koruklu":
            kapasite = 163
            yakit_tuketimi = 26.70   
        else:
            kapasite = 102
            yakit_tuketimi = 15.575
        super().__init__(id, kapasite, durum, 315, mevcut_yakit, mevcut_lokasyon)
        
        self.__otobus_tipi = otobus_tipi
        self.__yakit_tuketimi_degeri = yakit_tuketimi
        self.__bilet_ucreti = 17.08 #15.09.2025 tarihinden istanbulda gecerli toplu taşıma ögrenci tarifesi.
        self.__durak_arasi_km = 2.5 
        self.__duraklar = ["Kuzey Kampüs", "Ana Kampüs", "Kız Yurdu", "Erkek Yurdu", "Kadıköy İskelesi"]
        
        if not plaka:
            print(f"UYARI: {id} ID'li Otobüs için plaka girişi ZORUNLUDUR!")
            self.__plaka = input(f"Lütfen {id} nolu araç için plaka giriniz: ")
        else:
            self.__plaka = plaka
    
    @staticmethod
    def hiz_siniri_kontrol(hiz):
        return hiz <= 80  # Otobüs hız sınırı kontrolü

    @classmethod
    def otobüs_bilgisi(cls):
        return "AKILLI KAMPÜS SİSTEMİ'NE BAĞLI BİR OTOBÜSTÜR"
        
    def get_plaka(self):
        return self.__plaka
    def get_otobus_tipi(self): 
        return self.__otobus_tipi
    
    def motoru_calistir(self):
        if self.get_durum() == "Arızalı":
            print(f"Araç ({self.get_id()}) arızalı! Önce tamir etmelisin.")
            return 
        super().motoru_calistir() 
        print(f"Otobüs ({self.__otobus_tipi}) motoru çalıştı.")
       
    def motoru_kapat(self):
        super().motoru_kapat()
        print(f"Otobüs ({self.__otobus_tipi}) motoru kapattı.")
        
    def km_basina_maaliyet(self):
        return self.__yakit_tuketimi_degeri
    def ucret_hesapla(self, binilen_durak, inilen_durak):
        try:
            # Durakların listedeki yerini buluyoruz
            bas_index = self.__duraklar.index(binilen_durak)
            bit_index = self.__duraklar.index(inilen_durak)
            
            fark = abs(bit_index - bas_index)
            mesafe = fark * self.__durak_arasi_km
            
            print(f"ℹBilgi: Otobüs hatlarında sabit öğrenci tarifesi geçerlidir.")
            print(f"Rota: {binilen_durak} ---> {inilen_durak} ({mesafe} KM)")
            
            return self.__bilet_ucreti, fark
            
        except ValueError:
            print("ata: Girdiğiniz durak otobüs hattında bulunmuyor.")
            return 0, 0

    
    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"Plaka: {self.get_plaka()} | Tip: {self.__otobus_tipi}")