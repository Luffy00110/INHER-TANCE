from base import PaymentMethod

class CampusCardPayment(PaymentMethod):

    def __init__(self, owner, currency, bakiye=0):
        super().__init__(owner, currency)
        self.bakiye = bakiye

    def yukle(self, amount):
        if amount > 0:
            self.bakiye += amount
            return True
        return False

    def kontrol(self, amount):
        return self.bakiye >= amount

    def odeme(self, amount):
        if self.kontrol(amount):
            self.bakiye -= amount
            return True
        return False

    def aciklama_bilgisi(self):
        return f"CampusCard(owner={self.owner}, bakiye={self.bakiye} {self.currency})"
    
    def para_birimi_bilgisi(self):
        return f"Kampüs kartı para birimi: {self.currency}"

class OtobusCardPayment(CampusCardPayment):
    def __init__(self, owner, currency, bakiye=0):
        super().__init__(owner, currency, bakiye)
        self.kart_tipi = "Otobüs Kartı"

class BisikletCardPayment(CampusCardPayment):
    def __init__(self, owner, currency, bakiye=0):
        super().__init__(owner, currency, bakiye)
        self.kart_tipi = "Bisiklet Kartı"

class ScooterCardPayment(CampusCardPayment):
    def __init__(self, owner, currency, bakiye=0):
        super().__init__(owner, currency, bakiye)
        self.kart_tipi = "Scooter Kartı"