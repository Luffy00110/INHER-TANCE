from base import PaymentMethod

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
    
    def para_birimi_bilgisi(self):
        return f"Online cüzdanlarda kullanılan para birimi: {self.currency}"

    def aciklama_bilgisi(self):
        return f"Wallet(owner={self.owner}, bakiye={self.bakiye} {self.currency})"