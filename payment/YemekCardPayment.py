from base import PaymentMethod

#Kampüs / Yemekhane kartı ile ödeme yapılmasını sağlar.
class YemekCardPayment(PaymentMethod):

    def __init__(self, owner, currency, bakiye=0):
        super().__init__(owner, currency)
        self._bakiye = bakiye
        self._secilen_yemekler = []   

    #Kart yükleme işlemi yapar.
    def yukle(self, amount):
        if amount > 0:
            self.bakiye += amount
            return True
        return False
     
    #Yemek seçimi yapar.
    def yemek_sec(self, yemek_adi, fiyat):
        yemek = {"yemek": yemek_adi,"fiyat": fiyat}
        self._secilen_yemekler.append(yemek)
        return True
    
    #Seçilen yemeklerin toplam ücretini döndürür.
    def toplam_ucret(self):
        toplam = 0
        for yemek in self._secilen_yemekler:
            toplam += yemek["fiyat"]
        return toplam
    
    #Bakiye kontrolü yapar.
    def kontrol(self, amount=None):
        if amount is None:
            amount = self.toplam_ucret()
        return self.bakiye >= amount
    
    #Ödeme işlemi gerçekleştirir.
    def odeme(self, amount=None):
        if amount is None:
            amount = self.toplam_ucret()
        if self.kontrol(amount):
            self._bakiye -= amount
            self._secilen_yemekler = []
            return True
        return False
    
    #Bakiye bilgisi!
    @property
    def bakiye(self):
        return self._bakiye
    
    @bakiye.setter
    def bakiye(self, value):
        if value < 0:
            raise ValueError("Bakiye negatif olamaz")
        self._bakiye = value

    #Para birimi bilgisi döner.
    def para_birimi_bilgisi(self):
        return f"Yemekhane kartlarında kullanılan para birimi: {self.currency}"
    
    #Kart açıklaması bilgisi döner.
    def aciklama_bilgisi(self):
        return f"YemekCard(owner={self.owner}, bakiye={self.bakiye} {self.currency})"
    
    #Ödeme türü bilgisi döner.
    @staticmethod
    def odeme_turu():
        return "YemekCard ile ödeme"

    #Sınıf adı bilgisi döner.
    @classmethod
    def sinif_bilgisi(cls):
        return cls.__name__