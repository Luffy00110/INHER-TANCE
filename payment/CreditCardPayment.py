from base import PaymentMethod

#Kredi kartı tabanlı ödeme yöntemlerini açıklamayı sağlar.
class CreditCardPayment(PaymentMethod):

    #Kredi kartı bilgilerini kapsüllenmiş şekilde tutar.
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, kart_turu, komisyon_orani):
        super().__init__(owner, currency,limit)
        self.__kart_numarasi = kart_numarasi
        self.__cvv = cvv
        self.__son_kullanma_tarihi = son_kullanma_tarihi
        self.__kart_turu = kart_turu
        self.komisyon_orani = komisyon_orani

    # Toplam tutar = ürün + komisyon. 
    def kontrol(self, amount):
       toplam = amount + (amount * self.komisyon_orani)
       return self.limit >= toplam
  
    #Ödeme işlemini limitten düşerek gerçekleştirir. Limitten komisyon da düşer.
    def odeme(self, amount):
        toplam = amount + (amount * self.komisyon_orani)
        if not self.kontrol(amount):
            raise ValueError("Yetersiz kredi limiti")
        self.limit -= toplam  
        print(f"{self.kart_turu} ile ödeme: {amount} + komisyon {toplam - amount:.2f} = {toplam:.2f}, kalan limit: {self.limit:.2f}")
        return True
    
    #Ödenecek miktar üzerinden bankanın alacağı komisyonu hesaplar.
    def komisyon_tutari(self, amount):
        return amount * self.komisyon_orani
    
    def vergi_hesapla(self, amount):
        return amount * 0.05
 
    #Kredi kartlarında kullanılan para birimini döndürür.
    def para_birimi_bilgisi(self):
        return f"Kredi kartlarında kullanılan para birimi: {self.currency}"
    
    #Kredi kartı için açıklama bilgisini döndürür.
    def aciklama_bilgisi(self):
        return f"Wallet(owner={self.owner}, bakiye={self.limit} {self.currency})"
    
    #Kart numarasının geçerli uzunlukta olup olmadığını kontrol etmeyi sağlar.
    @staticmethod
    def kart_numarasi_gecerli_mi(no):
        return isinstance(no, str) and len(no) in [15, 16]

    #Kart türünü sınıf adına göre döndürmeyi sağlar.
    @classmethod
    def kart_tipi(cls):
        return cls.__name__
    
    #Kart türünü güvenli şekilde döndürür.
    @property
    def kart_turu(self):
        return self.__kart_turu
    
    @kart_turu.setter
    def kart_turu(self, value):
        if not isinstance(value, str):
            raise TypeError("Kart türü string olmalıdır!")
        self.__kart_turu = value

    # Kart numarasını güvenli şekilde döndürür.
    @property
    def kart_numarasi(self):
        return self.__kart_numarasi

    @kart_numarasi.setter
    def kart_numarasi(self, value):
        if not CreditCardPayment.kart_numarasi_gecerli_mi(value):
            raise ValueError("Kart numarası geçersiz!")
        self.__kart_numarasi = value

#VISA kart ödemelerini gösterir.
class VisaCardPayment(CreditCardPayment):
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, komisyon_orani=0.01):
        super().__init__(owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, "VISA", komisyon_orani)

#MASTERCARD kart ödemelerini gösterir.
class MasterCardPayment(CreditCardPayment):
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, komisyon_orani=0.012):
        super().__init__(owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, "MASTERCARD", komisyon_orani)
       
#TROY kart ödemelerini gösterir.
class TroyCardPayment(CreditCardPayment):
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, komisyon_orani=0.015):
        super().__init__(owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, "TROY", komisyon_orani)

#Banka Kartı Çeşitleri
class ZiraatCardPayment(CreditCardPayment):
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit):
        super().__init__(owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, "Ziraat", 0.0047)

class HalkbankCardPayment(CreditCardPayment):
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit):
        super().__init__(owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, "Halkbank", 0.0052)

class GarantiCardPayment(CreditCardPayment):
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit):
        super().__init__(owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, "Garanti", 0.0060)

class AkbankCardPayment(CreditCardPayment):
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit):
        super().__init__(owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, "Akbank", 0.0055)

class VakifbankCardPayment(CreditCardPayment):
    def __init__(self, owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit):
        super().__init__(owner, currency, kart_numarasi, cvv, son_kullanma_tarihi, limit, "Vakıfbank",  0.0050)