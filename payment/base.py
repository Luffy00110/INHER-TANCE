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
    def para_birimi_bilgisi(currency):
        pass


class CreditCardPayment(PaymentMethod):

    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi):
        super().__init__(owner, currency)
        self.kart_numarasi = kart_numarasi
        self.cvv = cvv
        self.son_kullanma_tarihi = son_kullanma_tarihi

    def kontrol(self, amount):
        return True

    def odeme(self, amount):
        return True

    def aciklama_bilgisi(self):
        return (
            f"CreditCard(owner={self.owner}, CardNumber={self.kart_numarasi}, "
            f"CVV={self.cvv}, expiration_date = {self.son_kullanma_tarihi} "
            f"currency={self.currency})"
        )


class CashPayment(PaymentMethod):

    def __init__(self, owner, currency, odeme_amount):
        super().__init__(owner, currency)
        self.odeme_amount = odeme_amount

    def kontrol(self, amount):
        return self.odeme_amount >= amount

    def odeme(self, amount):
        if self.kontrol(amount):
            self.odeme_amount -= amount
            return True
        return False

    def aciklama_bilgisi(self):
        return f"Cash(owner={self.owner}, cash={self.odeme_amount} {self.currency})"


class OnlineWalletPayment(PaymentMethod):

    def __init__(self, owner, currency, cuzdan_id, bakiye):
        super().__init__(owner, currency)
        self.cuzdan_id = cuzdan_id
        self.bakiye = bakiye

    def kontrol(self, amount):
        return self.bakiye >= amount

    def odeme(self, amount):
        if self.kontrol(amount):
            self.bakiye -= amount
            return True
        return False

    def aciklama_bilgisi(self):
        return f"Wallet(owner={self.owner}, bakiye={self.bakiye} {self.currency})"