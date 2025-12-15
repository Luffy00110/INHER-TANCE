class PaymentMethodRepository:
    def __init__(self):
        self.payment_methods = []

    def payment_method_ekle(self, method):
        self.payment_methods.append(method)
        return True

    def listele(self):
        return self.payment_methods

    def kullanici_secimi(self, owner):     #Kullanıcıya ait ödeme yöntemlerini bulmak için
        sonuc = []
        for method in self.payment_methods:
            if method.owner == owner:
                sonuc.append(method)
        return sonuc

    def kart_tercihi(self, kart_turu):     #Kart tipi seçimi için
        sonuc = []

        for method in self.payment_methods:
            sinif_adi = method.__class__.__name__

            if sinif_adi == "VisaCardPayment":
                if kart_turu == "VISA":
                    sonuc.append(method)

            elif sinif_adi == "MasterCardPayment":
                if kart_turu == "MASTERCARD":
                    sonuc.append(method)

            elif sinif_adi == "TroyCardPayment":
                if kart_turu == "TROY":
                    sonuc.append(method)

        return sonuc

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
    
    def id_ile_getir(self, id):
        for islem in self.transactions:
          if islem.id == id:
            return islem
        return None
    
    def tarih_araligi_getir(self, baslangic, bitis):
     sonuc = []
     for islem in self.transactions:
        if baslangic <= islem.tarih <= bitis:
            sonuc.append(islem)
     return sonuc
