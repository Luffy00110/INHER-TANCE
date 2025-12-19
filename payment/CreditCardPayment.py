from base import PaymentMethod

class CreditCardPayment(PaymentMethod):

    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit):
        super().__init__(owner, currency,limit)
        self.kart_numarasi = kart_numarasi
        self.cvv = cvv
        self.son_kullanma_tarihi = son_kullanma_tarihi

    def kontrol(self, amount):
        return self.limit >= amount

    def odeme(self, amount):
        if self.kontrol(amount):
            self.limit -= amount
            return True
        return False
    
    def para_birimi_bilgisi(self):
        return f"Kredi kartlarında kullanılan para birimi: {self.currency}"

    def aciklama_bilgisi(self):
        return f"Wallet(owner={self.owner}, bakiye={self.limit} {self.currency})"

class VisaCardPayment(CreditCardPayment):
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit):
        super().__init__(owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit)
        self.kart_turu = "VISA"

class MasterCardPayment(CreditCardPayment):
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit):
        super().__init__(owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit)
        self.kart_turu = "MASTERCARD"

class TroyCardPayment(CreditCardPayment):
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit):
        super().__init__(owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit)
        self.kart_turu = "TROY"