from base import TransportVehicle

class Teleferik(TransportVehicle):
    def __init__(self, id, durum, kabin_sayisi, halat_uzunlugu, bilet_ucreti, mevcut_lokasyon="Tepe İstasyon"):
        toplam_kapasite = kabin_sayisi * 8
        super().__init__(id, toplam_kapasite, durum, 0, 100, mevcut_lokasyon)
        

        self.__kabin_sayisi = kabin_sayisi
        self.__halat_uzunlugu = halat_uzunlugu 
        self.__bilet_ucreti = float(bilet_ucreti) 
        
    @classmethod
    def guvenlik_kurali(cls):
        return "Rüzgar hızı 40 km/s üzerindeyse sistem otomatik durur."

    @staticmethod
    def kuyruk_suresi_hesapla(sira_bekleyen_kisi):
        dakika_kapasitesi = 16
        tahmini_sure = sira_bekleyen_kisi / dakika_kapasitesi
        
        if tahmini_sure < 1:
            return "Sıra yok, hemen binebilirsiniz."
        
        return f"{sira_bekleyen_kisi} kişi var. Tahmini bekleme süreniz: {int(tahmini_sure)} dakika."

    def get_kabin_sayisi(self):
        return self.__kabin_sayisi
    
    def get_bilet_ucreti(self):
        return self.__bilet_ucreti

    def set_bilet_ucreti(self, yeni_ucret):
        self.__bilet_ucreti = yeni_ucret
        print(f"Bilet ücreti güncellendi: {self.__bilet_ucreti} TL")

    def motoru_calistir(self):
        if self.get_durum() == "Arızalı":
            print(f"Teleferik ({self.get_id()}) teknik arıza nedeniyle durduruldu.")
            return
        super().motoru_calistir()
        print(f"Teleferik ({self.get_id()}) {self.__kabin_sayisi} kabin ile çalışmaya başladı.")

    def motoru_kapat(self):
        super().motoru_kapat()
        print(f"Teleferik ({self.get_id()}) durduruldu.")

    def ucret_hesapla(self, giris, cikis):
        print(f"Manzara Rotası: {giris} -> {cikis}")
        print(f"Hat Uzunluğu: {self.__halat_uzunlugu} metre")
        return self.__bilet_ucreti, 1 

    def km_basina_maaliyet(self):
        return 45.5 
    
    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"Sistem: {self.__kabin_sayisi} Kabin | Hat: {self.__halat_uzunlugu}m | Bilet: {self.__bilet_ucreti} TL")