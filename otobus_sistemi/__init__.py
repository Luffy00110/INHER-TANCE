from abc import ABC, abstractmethod

class transportVehicle():
    def __init__(self,id,kapasite,mevcut_lokasyon,durum):
        self.id = id
        self.kapasite = kapasite
        self.mevcut_lokasyon = mevcut_lokasyon
        self.durum = durum

