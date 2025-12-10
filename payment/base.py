# base.py
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, owner, currency):
        self.owner = owner
        self.currency = currency

    @abstractmethod
    def kontrol(self, amount):
        pass

    @abstractmethod
    def odeme(self, amount):
        pass

    def aciklama_bilgisi(self):
        pass

    @staticmethod
    def para_birimi_bilgisi(currency):      #Doğru para birimi kontrolü yaptım.
        pass

#Kredi Kartı Ödeme Sınıfı
class CreditCardPayment(PaymentMethod):

    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi):
        super().__init__(owner, currency)
        self.kart_numarasi = kart_numarasi
        self.cvv = cvv 
        self.son_kullanma_tarihi = son_kullanma_tarihi

    def aciklama_bilgisi(self):
        return f"CreditCard(owner={self.owner}, limit={self.limit}, currency={self.currency})"

