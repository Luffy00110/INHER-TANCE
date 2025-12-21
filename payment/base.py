from abc import ABC, abstractmethod

# Ödeme yöntemleri için soyut temel sınıf.
class PaymentMethod(ABC):
    # Ödeme yönteminin bilgilerini içinde tutar.
    def __init__(self, owner, currency,limit=0):
        self.__owner = owner
        self.__currency = currency
        self.__limit = limit

# Ödeme yapılabilir mi onu kontrol etmeyi sağlar.
    @abstractmethod
    def kontrol(self, amount):
        pass

# Ödeme işlemini gerçekleştirmeyi sağlar.
    @abstractmethod
    def odeme(self, amount):
        pass

# Para birimi bilgisini döndürmeyi sağlar.
    @abstractmethod
    def para_birimi_bilgisi(self):
        pass

# Kullanıcıya ait açıklama bilgisini döndürür.
    def aciklama_bilgisi(self):
        return f"{self.owner} - {self.currency}"
        
# Geçerli para birimlerini kontrol eder.
    @staticmethod
    def gecerli_para_birimi_mi(currency):
        return currency in ["TRY", "USD", "EUR"]
    
 # Ödeme yöntemi sınıf adını döndürüyor.
    @classmethod
    def odeme_tipi(cls):
        return cls.__name__
    
    @property
    def owner(self):
        return self.__owner

    @property
    def currency(self):
        return self.__currency

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, value):
        if value < 0:
            raise ValueError("Limit negatif olamaz")
        self.__limit = value