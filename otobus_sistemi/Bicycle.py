from base import TransportVehicle

class Bicycle(TransportVehicle): #Bisiklet ksımı şimdilik sadece ücret eklenmiştir bunun dışında kart ödeme kısmı vs de eklenecektir.
    def __init__(self, id,durum, mevcut_lokasyon="Ana Kampüs"):
        super().__init__(id, 1, durum, mevcut_lokasyon)

    # şiimdilk iptal def sistemi_calistir(self):
        #print("Bisiklet ulaşım sitemini çalıştırdınız.")
    
    # şiimdilk iptal  def sistemi_durdur(self):
        #print("Bisiklet ulaşım sistemini sonlandırdınız.")
    
    # şiimdilk iptal def km_basina_maaliyet(self):
        #return 0.15
    
    def km_basina_maaliyet(self):

        return 0.15 

    def motoru_calistir(self):
        if self.durum == "Arızalı":
            print(f"❌ HATA: Bisiklet ({self.id}) sistem dışı! Kilit açılamaz.")
            return       
        print("✅ Bisiklet kilidi açıldı. Keyifli sürüşler!")

    def motoru_kapat(self):

        print(f"Bisiklet {self.id} kilitlendi.")    

    def bilgi_ver(self):

        super().bilgi_ver()