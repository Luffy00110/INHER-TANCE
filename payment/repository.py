#Tüm ödeme yöntemlerini saklar.
class PaymentMethodRepository:
    def __init__(self):
        self._payment_methods = []      

    #Ödeme yöntemlerini döner 
    @property
    def payment_methods(self):
        return self._payment_methods

    #Yeni ödeme yöntemi ekler.
    def payment_method_ekle(self, method):
        self._payment_methods.append(method)
        return True
    
    #Tüm ödeme yöntemlerini döner.
    def listele(self):
        return self._payment_methods
    
    #Belirli kullanıcıya ait ödeme yöntemlerini bulmak için.
    def kullanici_secimi(self, owner):     
        sonuc = []
        for method in self.payment_methods:
            if method.owner == owner:
                sonuc.append(method)
        return sonuc
    
    #Belirli kart türüne ait yöntemleri döndürür.
    def kart_tercihi(self, kart_turu):     
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
    
    #Ödeme yöntemini siler.
    def payment_method_sil(self, method):
        if method in self.payment_methods:
            self.payment_methods.remove(method)
            return True
        return False
    
    #Repository hakkında bilgi verir.
    @staticmethod
    def repository_bilgisi():
        return "PaymentMethodRepository sınıfı, ödeme yöntemlerini saklar"
    
    #Sınıf adını döner.
    @classmethod
    def sinif_bilgisi(cls):
        return cls.__name__

#Tüm işlemleri saklar.
class TransactionRepository:
    def __init__(self):
        self._transactions = []
    
    def haftalik_rapor(self):
        rapor = {}
        for t in self._transactions:
            hafta = t.tarih.isocalendar()[1]
            rapor.setdefault(hafta, 0)
            rapor[hafta] += t.amount
        return rapor

    # Belirli ay için toplam tutarı döndürür
    def aylik_rapor(self, ay):
        toplam = 0
        for t in self._transactions:
            if t.tarih.month == ay:
                toplam += t.amount
        return toplam

    #Tüm işlemleri döner.
    @property
    def transactions(self):
        return self._transactions
    
    @transactions.setter
    def transactions(self, value):
        if not isinstance(value, list):
            raise ValueError("Transactions listesi olmalı")
        self._transactions = value

    def ekle(self, islem):
        return self.islem_ekle(islem)

    #Yeni işlem ekler.
    def islem_ekle(self, islem):
        self.transactions.append(islem)
        return True
    
    #Tüm işlemleri döndürür.
    def listele(self):
        return self.transactions
    
    #Belirli kullanıcıya ait işlemleri bulmayı sağlar.
    def kullanici_secimi(self, owner):    
        sonuc = []
        for islem in self.transactions:
            if islem.owner == owner:
                sonuc.append(islem)
        return sonuc
    
    #Tüm işlemlerin toplamını döndürür.
    def toplam_tutar(self):
        toplam = 0
        for islem in self.transactions:
            toplam += islem.amount
        return toplam
    
    #ID ile işlemi bulur.
    def id_ile_getir(self, id):
        for islem in self.transactions:
          if islem.id == id:
            return islem
        return None
    
    #Belirli tarih aralığındaki işlemleri döner.
    def tarih_araligi_getir(self, baslangic, bitis):
     sonuc = []
     for islem in self.transactions:
        if baslangic <= islem.tarih <= bitis:
            sonuc.append(islem)
     return sonuc
    
    # Repository hakkında bilgi verir.
    @staticmethod
    def repository_bilgisi():
        return "TransactionRepository, işlemleri saklar"  

    # Sınıf adını döndürür.
    @classmethod
    def sinif_bilgisi(cls):
        return cls.__name__  