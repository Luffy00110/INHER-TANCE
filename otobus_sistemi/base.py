from abc import ABC, abstractmethod

class transportVehicle():
    def __init__(self,id,kapasite,durum,mevcut_lokasyon="Ana Kampüs"):
        self.id = id
        self.kapasite = kapasite
        self.durum = durum
        self.mevcut_lokasyon = mevcut_lokasyon

    @abstractmethod
    def motoru_calistir(self):
            pass
    @abstractmethod
    def motoru_kapat(self):
        pass
    @abstractmethod
    def km_basina_maaliyet(self):



