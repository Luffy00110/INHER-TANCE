from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, owner, currency,limit=0):
        self.owner = owner
        self.currency = currency
        self.limit = limit

    @abstractmethod
    def kontrol(self, amount):
        pass

    @abstractmethod
    def odeme(self, amount):
        pass

    @abstractmethod
    def para_birimi_bilgisi(self):
        pass

    def aciklama_bilgisi(self):
        return f"{self.owner} - {self.currency}"