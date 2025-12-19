from base import PaymentMethod

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
    
    def para_birimi_bilgisi(self):
        return f"Nakit ödemelerde kullanılan para birimi: {self.currency}"

    def aciklama_bilgisi(self):
        return f"Cash(owner={self.owner}, cash={self.odeme_amount} {self.currency})"
