from base import TransportVehicle
class Vapur(TransportVehicle):
    def __init__(self, id, durum, mevcut_yakit, depo_limit, yolcu_kapasitesi, gemi_ismi="İsimsiz Gemi"):
        super().__init__(id, yolcu_kapasitesi, durum, depo_limit, mevcut_yakit, mevcut_lokasyon="Kadıköy İskelesi")
        self.__plaka = gemi_ismi
        self.__bilet_ucreti = 57.3
        self.__km_basina_yakit = 300
    
    @classmethod
    def guvenlik_anonsu(cls):
        return "Can yelekleri koltukların altında veya dolapların üzerindedir."
    @staticmethod
    def mil_km_cevir(deniz_mili):
        km = deniz_mili * 1.852
        return f"{deniz_mili} Deniz Mili, yaklaşık {km:.2f} Kilometre eder."
    
    def km_basina_maaliyet(self):
        return self.__km_basina_yakit
    
    def get_plaka(self):
        return self.__plaka
    
    def anons(self):
        print(f"Sayın yolcularımız, gemimiz kalkışa hazırdır. Lütfen iskeleyi boşaltalım.")
    
    def motoru_calistir(self):
        if self.get_durum() == "Arızalı":
            print(f"{self.__plaka} arızalı. Motor çalıştırılamadı...")
        else:
            super().motoru_calistir()
            print(f"{self.__plaka} motoru çalıştırıldı. Vapur iskeleden kalkışa hazırlanıyor.")
            
    def motoru_kapat(self):
        super().motoru_kapat()
        print(f"{self.__plaka} iskeleye yanaştı. Demir atımı tamanlandı. Motor kapandı.")
    
    def ucret_hesapla(self, binilen_durak, inilen_durak):
        print(f"Vapurun rotası : {binilen_durak} iskelesinden {inilen_durak} iskelesine doğru.")
        return self.__bilet_ucreti, 1
    
    def sefere_cik(self, hedef_iskele):
        duraklar  = ["Kadıköy İskelesi","Adalar(MYO) İskelesi"]
        if self.get_durum() != "Müsait" and self.get_durum() !="Seferde":
            print(f"Vapur şuan {self.get_durum()}, yeni bir sefere çıkamıyor.")
            return
        
        if hedef_iskele not in duraklar:
            print(f"{hedef_iskele} rotası geçersiz!")
            print(f"Sadece şuralara gidilebilir: {duraklar}")
            return
        
        if self.get_mevcut_lokasyon() == hedef_iskele:
            print(f"Zaten {hedef_iskele} konumundasınız.")
            return
        print(f"Sefer başlatılıyor... İstikamet : {hedef_iskele}")

        if hedef_iskele == "Adalar(MYO) İskelesi":
            print(f" {self.__plaka} Adalar(MYO) İskelesi'ne götürülüyor...")
            self.set_mevcut_lokasyon("Adalar(MYO) İskelesi")
        else:
            self.set_mevcut_lokasyon(hedef_iskele)       
        self.set_durum("Seferde") 
    
    def bilgi_ver(self):
        super().bilgi_ver()
        print(f"Gemi İsmi: {self.__plaka}")