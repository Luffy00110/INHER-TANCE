from base import TransportVehicle

class Bicycle(TransportVehicle): 
    def __init__(self, id, durum, acilis_ucreti, dakika_ucreti, mevcut_lokasyon="Ana Kampüs"):
        super().__init__(id, 1, durum, 0, 0, mevcut_lokasyon)
        self.__acilis_ucreti = float(acilis_ucreti)
        self.__dakika_ucreti = float(dakika_ucreti)
    
    @classmethod
    def fiyat_kurali_goster(cls):
        return "Açılış ücreti en az 3 TL, dakika ücreti en az 1 TL olmalıdır."
    
    @staticmethod
    def dakika_saat_cevir(dakika):
        return dakika / 60

    def motoru_calistir(self):
        if self.get_durum() == "Arızalı":
            print(f"Bisiklet ({self.get_id()}) sistem dışı! Kilit açılamaz.")
            return       
        print(f"Bisiklet ({self.get_id()}) kilidi açıldı. Keyifli sürüşler!")
    
    def get_dakika_ucreti(self):
        return self.__dakika_ucreti

    def set_dakika_ucreti(self, yeni_ucret):
        if yeni_ucret <= 0:
            print("Dakika ücreti 0'dan büyük olmalı.")
            return
        self.__dakika_ucreti = yeni_ucret
    
    def get_acilis_ucreti(self):
        return self.__acilis_ucreti

    def set_acilis_ucreti(self, yeni_ucret):
        if yeni_ucret < 0:
            print("Açılış ücreti negatif olamaz.")
            return
        self.__acilis_ucreti = yeni_ucret

    def motoru_kapat(self):
        super().motoru_kapat()
        print(f"Bisiklet ({self.get_id()}) kilitlendi.")  

    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"Tarife       : Açılış {self.__acilis_ucreti} TL + {self.__dakika_ucreti} TL/dk")

    def ucret_hesapla(self, giris, cikis, sure_dk=0):
        print(f"Rota: {giris} -> {cikis}")
        toplam_ucret = self.__acilis_ucreti + (sure_dk * self.__dakika_ucreti)
        print(f"Sürüş Süresi: {sure_dk:.2f} dakika")
        return toplam_ucret, 1
    
    def km_basina_maaliyet(self):
        return 0
    
    def benzin_al(self, litre):
        print("Bisiklete benzin koymak mı? İyi deneme ilerde belki olabilir ama şu anda mümkün değil...")
    
