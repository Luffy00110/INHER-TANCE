class PaymentMethodRepository:
    def __init__(self):
        self.payment_methods = []

    def payment_method_ekle(self, method):
        self.payment_methods.append(method)
        return True

    def listele(self):
        return self.payment_methods

    def kullanici_secimi(self, owner):       #Kullanıcıya ait ödeme yöntemlerini bulmak için
        result = []
        for method in self.payment_methods:
            if method.owner == owner:
                result.append(method)
        return result

    def kart_tercihi(self, kart_turu):       #Kart Tipi seçimi için
        result = []
        for method in self.payment_methods:
            if hasattr(method, "kart_turu") and method.kart_turu == kart_turu:
                result.append(method)
        return result

    def payment_method_sil(self, method):
        if method in self.payment_methods:
            self.payment_methods.remove(method)
            return True
        return False
    
class TransactionRepository:
    def __init__(self):
        self.transactions = []

    def islem_ekle(self, islem):
        self.transactions.append(islem)
        return True

    def listele(self):
        return self.transactions

    def kullanici_secimi(self, owner):    #Kullanıcıya ait işlemleri bulmak için
        sonuc = []
        for islem in self.transactions:
            if islem.owner == owner:
                sonuc.append(islem)
        return sonuc

    def toplam_tutar(self):
        toplam = 0
        for islem in self.transactions:
            toplam += islem.amount
        return toplam

