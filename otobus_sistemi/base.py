from abc import ABC, abstractmethod

class TransportVehicle(ABC):
    __toplam_arac_sayisi = 0

    def __init__(self, id, kapasite, durum, depo_kapasitesi, mevcut_yakit, mevcut_lokasyon="Ana Kampüs"):
        self.__id = id
        self.__kapasite = kapasite
        self.__durum = durum
        self.__depo_kapasitesi = depo_kapasitesi
        self.__mevcut_yakit = mevcut_yakit
        self.__mevcut_lokasyon = mevcut_lokasyon
        
        # Her yeni araçta sayac artar
        TransportVehicle.__toplam_arac_sayisi += 1 
        
        # Varsayilan yakit fiyati
        self.__yakit_fiyati = 0.0
        
    #GETTER VE SETTER METORLARI ALTTA
    def get_id(self): 
        return self.__id
    
    def get_kapasite(self): 
        return self.__kapasite
    
    def set_kapasite(self, yeni_kapasite):
        self.__kapasite = yeni_kapasite
    
    def get_durum(self): 
        return self.__durum
    
    def set_durum(self, yeni_durum): 
        self.__durum = yeni_durum
        
    def get_mevcut_yakit(self): 
        return self.__mevcut_yakit
    
    def set_mevcut_yakit(self, miktar): 
        self.__mevcut_yakit = miktar
        
    def get_depo_kapasitesi(self): 
        return self.__depo_kapasitesi
    
    def get_mevcut_lokasyon(self): 
        return self.__mevcut_lokasyon
    
    def set_mevcut_lokasyon(self, yeni_lokasyon):
        self.__mevcut_lokasyon = yeni_lokasyon
        
    def get_yakit_fiyati(self): 
        return self.__yakit_fiyati
    
    def set_yakit_fiyati(self, fiyat): 
        self.__yakit_fiyati = fiyat
        
    @abstractmethod
    def motoru_calistir(self):
        pass
   
    @abstractmethod
    def motoru_kapat(self):
        pass
   
    @abstractmethod
    def ucret_hesapla(self, giris, cikis):
        pass

    @abstractmethod
    def km_basina_maaliyet(self):
        pass

    @staticmethod 
    def id_kontrol(arac_id):
        if isinstance(arac_id, int) and arac_id > 0:
            return True
        return False
    
    @classmethod
    def toplam_filo_sayisi(cls):
        print(f"Sistemdeki Toplam Araç: {cls.__toplam_arac_sayisi}")
        
    @classmethod
    def filo_durum_kontrolu(cls):
        limit = 5 
        if cls.__toplam_arac_sayisi >= limit:
            print(f"Filo çok kalabalık! ({cls.__toplam_arac_sayisi} araç var.)")
        else:
            print(f"Sisteme yeni araç eklenebilir. ({cls.__toplam_arac_sayisi} araç var.)")
   
    def bilgi_ver(self):
        print(f"ID: {self.__id}")
        print(f"Durum: {self.__durum}")
        print(f"Konum: {self.__mevcut_lokasyon}")
        print(f"Kapasite: {self.__kapasite}")
    
    def ariza_yap(self):
        self.__durum = "Arızalı"
        print(f"{self.__id} numaralı araç ARIZA YAPTI! Sistem dışı.")

    def tamir_et(self):
        if self.__durum == "Arızalı":
            print(" Araç servise alındı, tamir ediliyor...")
            self.__durum = "Müsait" 
            print(f"{self.__id} numaralı araç tamir edildi. Tekrar göreve hazır.")
        else:
            print(f"{self.__id} numaralı araç zaten sağlam, tamire gerek yok!.")

    def benzin_al(self, istenen_litre):
        bos_yer = self.__depo_kapasitesi - self.__mevcut_yakit
        konulacak_miktar = 0
        
        if istenen_litre <= bos_yer:
            konulacak_miktar = istenen_litre
            print(f"{istenen_litre} birim yakıt/enerji dolumu yapılıyor...")
        else:
            print(f"Depo kapasitesi aşıldı! Sadece boş yer kadar ({bos_yer}) dolduruluyor.")
            konulacak_miktar = bos_yer 
            
        tutar = konulacak_miktar * self.__yakit_fiyati
        self.__mevcut_yakit += konulacak_miktar
        
        print(f"--- FİŞ DETAYI ---")
        print(f"Eklendi: {konulacak_miktar:.2f} Birim")
        print(f"Birim Fiyatı: {self.__yakit_fiyati} TL")
        print(f"TOPLAM TUTAR: {tutar:.2f} TL")
        print(f"Depo Durumu: ({self.__mevcut_yakit}/{self.__depo_kapasitesi})")

    def __str__(self):
        return f"[{type(self).__name__}] ID: {self.get_id()} | Durum: {self.get_durum()} | Konum: {self.get_mevcut_lokasyon()} | Kapasite: {self.get_kapasite()}"
