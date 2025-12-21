from base import PaymentMethod

#Online cüzdan ile ödeme yapılmasını sağlar.
class OnlineWalletPayment(PaymentMethod):

    def __init__(self, owner, currency, cuzdan_id, bakiye):
        super().__init__(owner, currency)
        self._cuzdan_id = cuzdan_id
        self._bakiye = bakiye

    #Cüzdan İd'si döndürür.
    @property
    def cuzdan_id(self):
        return self._cuzdan_id
    
    #Mevcut bakiye döndürür.
    @property
    def bakiye(self):
        return self._bakiye
    
    @bakiye.setter
    def bakiye(self, value):
        self._bakiye = value
    
    #Ödeme yapılabilir mi diye kontrol eder.
    def kontrol(self, amount):
        return self._bakiye >= amount
    
    #Ödemeyi gerçekleştirir, bakiye yeterliyse düşer.
    def odeme(self, amount):
        if self.kontrol(amount):
            self._bakiye -= amount
            return True
        return False
    
    #Cüzdanda kullanılan para birimini döner.
    @staticmethod
    def para_birimi_bilgisi(currency):
        return f"Online cüzdanlarda kullanılan para birimi: {currency}"
    
    #Sınıf adını döndürür.
    @classmethod
    def sinif_bilgisi(cls):
        return cls.__name__
    
    #Cüzdan sahibi ve bakiyeyi gösterir.
    def aciklama_bilgisi(self):
        return f"Wallet(owner={self.owner}, bakiye={self.bakiye} {self.currency})"
    
    #Kullanıcı dostu string çıktısı
    def __str__(self):
        return f"OnlineWalletPayment(owner={self.owner}, bakiye={self._bakiye} {self.currency})"
    
    #Detaylı debug string çıktısı
    def __repr__(self):
        return f"OnlineWalletPayment(cuzdan_id={self._cuzdan_id}, owner={self.owner}, bakiye={self._bakiye} {self.currency})"