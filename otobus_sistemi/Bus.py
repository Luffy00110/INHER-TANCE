from base import TransportVehicle

class Bus(TransportVehicle):
    def __init__(self, id, durum, otobus_tipi="Standart"):
        # Otobüs tipine göre kapasite ve km başına yaktığı tl cinsinini hesapladık. Yolcu sayısını hesaplarken oturan ve ayakta giden yoluların toplamını aldık.
        if otobus_tipi == "Koruklu":
            kapasite = 163
            yakit_tuketimi = 26.70   
        else:
            kapasite = 102
            yakit_tuketimi = 15.575

        super().__init__(id, kapasite, durum)
        
        self.otobus_tipi = otobus_tipi
        self.yakit_tuketimi_degeri = yakit_tuketimi

    def motoru_calistir(self):
        if self.durum == "Arızalı":
             print(f"❌ HATA: Araç ({self.id}) arızalı! Önce tamir etmelisin.")
             return 

        print(f"✅ Otobüs ({self.otobus_tipi}) motoru çalıştı.")
       
    def motoru_kapat(self):
        return super().motoru_kapat()
    
    def km_basina_maaliyet(self):
        return self.yakit_tuketimi_degeri