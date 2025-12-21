from base import TransportVehicle

class DenizTaksi(TransportVehicle):
    def __init__(self, id, durum, kapasite, acilis_ucreti, km_ucreti, mevcut_yakit, mevcut_lokasyon="Bebek İskelesi"):
        super().__init__(id, int(kapasite), durum, 150, mevcut_yakit, mevcut_lokasyon)
        self.__acilis_ucreti = float(acilis_ucreti)
        self.__km_ucreti = float(km_ucreti)
        self.__max_hiz_knot = 35 

    @classmethod
    def seyir_kurali(cls):
        return "Kıyı şeridinde hız sınırı vardır. Dalga yapmaktan kaçınınız."

    @staticmethod
    def knot_kmh_cevir(knot_degeri):
        kmh = knot_degeri * 1.852
        return f"{knot_degeri} Knot = {kmh:.2f} km/saat"

    
    def get_acilis_ucreti(self):
        return self.__acilis_ucreti

    def set_acilis_ucreti(self, yeni_ucret):
        if yeni_ucret >= 0:
            self.__acilis_ucreti = yeni_ucret
            print(f"Açılış ücreti güncellendi: {self.__acilis_ucreti} TL")
        else:
            print("Hata: Ücret negatif olamaz.")

    def get_km_ucreti(self):
        return self.__km_ucreti

    def set_km_ucreti(self, yeni_ucret):
        if yeni_ucret >= 0:
            self.__km_ucreti = yeni_ucret
            print(f"KM ücreti güncellendi: {self.__km_ucreti} TL/km")
        else:
            print("Ücret negatif olamaz.")

    def motoru_calistir(self):
        if self.get_durum() == "Arızalı":
            print(f"Deniz Taksi ({self.get_id()}) motor arızası! Servis bekleniyor.")
            return
        
        print(DenizTaksi.seyir_kurali())
        super().motoru_calistir()
        print(f"Deniz Taksi ({self.get_id()}) motorları çalıştı. Müşteri bekleniyor.")

    def motoru_kapat(self):
        super().motoru_kapat()
        print(f"Deniz Taksi ({self.get_id()}) iskeleye bağlandı.")

    def ucret_hesapla(self, giris, cikis, mesafe_km=5):
        if giris == cikis:
            print("Zaten aynı iskeledesiniz.")
            return 0, 0

        tutar = self.__acilis_ucreti + (mesafe_km * self.__km_ucreti)
        
        print(f"Rota: {giris} -> {cikis}")
        print(f"esafe: {mesafe_km} KM")
        print(f"esap: {self.__acilis_ucreti} (Açılış) + {mesafe_km}x{self.__km_ucreti} (Yol)")
        
        return tutar, mesafe_km

    def km_basina_maaliyet(self):
        return 22.5 # Deniz yakıtı maliyeti 
    
    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"Tarife: Açılış {self.__acilis_ucreti} TL | KM Başı {self.__km_ucreti} TL")
        print(f"Maksimum Hız: {DenizTaksi.knot_kmh_cevir(self.__max_hiz_knot)}")