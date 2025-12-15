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
        pass


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
    
# KART TÜRÜNE GÖRE KREDİ KARTLARI
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

 # KAMPÜS KARTLARI (Ulaşım İçin)      
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