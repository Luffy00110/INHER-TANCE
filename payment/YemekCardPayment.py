from base import PaymentMethod

class YemekCardPayment(PaymentMethod):

    def __init__(self, owner, currency, bakiye=0):
        super().__init__(owner, currency)
        self.bakiye = bakiye
        self.secilen_yemekler = []   

    def yukle(self, amount):
        if amount > 0:
            self.bakiye += amount
            return True
        return False

    def yemek_sec(self, yemek_adi, fiyat):
        yemek = {
            "yemek": yemek_adi,
            "fiyat": fiyat
        }
        self.secilen_yemekler.append(yemek)
        return True

    def toplam_ucret(self):
        toplam = 0
        for yemek in self.secilen_yemekler:
            toplam += yemek["fiyat"]
        return toplam

    def kontrol(self, amount=None):
        if amount is None:
            amount = self.toplam_ucret()

        return self.bakiye >= amount

    def odeme(self, amount=None):
        if amount is None:
            amount = self.toplam_ucret()

        if self.kontrol(amount):
            self.bakiye -= amount
            self.secilen_yemekler = []
            return True
        return False
    
    def para_birimi_bilgisi(self):
        return f"Yemekhane kartlarında kullanılan para birimi: {self.currency}"

    def aciklama_bilgisi(self):
        return f"YemekCard(owner={self.owner}, bakiye={self.bakiye} {self.currency})"