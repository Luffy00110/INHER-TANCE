from base import PaymentMethod

#Nakit ödeme yöntemini gösterir.
class CashPayment(PaymentMethod):

    #Nakit ödeme bilgilerini başlatır.
    def __init__(self, owner, currency, odeme_amount):
        super().__init__(owner, currency)
        self.__odeme_amount = odeme_amount

    #Ödeme için yeterli nakit olup olmadığını kontrol eder.
    def kontrol(self, amount):
        return self.__odeme_amount >= amount
    
    #Nakit ödeme işlemini gerçekleştirir.
    def odeme(self, amount):
        if self.kontrol(amount):
            self.__odeme_amount -= amount
            return True
        return False
    
    #Nakit ödemede kullanılan para birimi bilgisini döndürmeyi sağlar.
    def para_birimi_bilgisi(self):
        return f"Nakit ödemelerde kullanılan para birimi: {self.currency}"
    
    #Ödeme yöntemi hakkında açıklama bilgisi döndürmeyi sağlar.
    def aciklama_bilgisi(self):
        return f"Cash(owner={self.owner}, cash={self.odeme_amount} {self.currency})"
    
    #Mevcut nakit tutarını döndürmeyi sağlar.
    @property
    def odeme_amount(self):
        return self.__odeme_amount

    #Nakit tutarını günceller.
    @odeme_amount.setter
    def odeme_amount(self, value):
        if value < 0:
            raise ValueError("Nakit tutar negatif olamaz!")
        self.__odeme_amount = value

    #Nakit ödemelerin fiziksel olup olmadığını belirtir.
    @staticmethod
    def fiziksel_odeme_mi():
        return True
    
    #Nakit ödeme için özel tür bilgisini döndürür.
    @classmethod
    def nakit_odeme_tipi(cls):
        return "NAKİT"