from base import PaymentMethod

#Kampüs kartı bazlı ödeme yöntemlerini temsil eder.
class CampusCardPayment(PaymentMethod):

    def __init__(self, owner, currency, bakiye=0):
        super().__init__(owner, currency)
        self.__bakiye = bakiye
        self._kart_tipi = "Kampüs Kartı"

    #Kart bakiyesini yüklemeyi sağlar.
    def yukle(self, amount):
        if amount <= 0:
           return False
        if self.bakiye + amount > self.maksimum_bakiye():
           raise ValueError("Maksimum bakiye aşıldı")
        self.bakiye += amount
        return True

    #Ödeme yapılabilir mi kontrol etmeyi sağlar.
    def kontrol(self, amount):
        return self.bakiye >= amount

    #Ödeme işlemini gerçekleştirir.
    def odeme(self, amount):
        if self.kontrol(amount):
            self.bakiye -= amount
            return True
        return False
    
    #Kart bilgilerini açıklama olarak gösterir.
    def aciklama_bilgisi(self):
        return f"CampusCard(owner={self.owner}, bakiye={self.bakiye} {self.currency})"
    
    # Kart bakiyesini güvenli şekilde döndürür.
    @property
    def bakiye(self):
        return self.__bakiye

    # Kart bakiyesini kontrollü şekilde ayarlar.
    @bakiye.setter
    def bakiye(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Bakiye sayısal olmalıdır!")
        if not isinstance(value, (int, float)):
            raise TypeError("Bakiye sayısal olmalıdır!")
        if value < 0:
            raise ValueError("Bakiye negatif olamaz!")
        self.__bakiye = value

    # Kampüs kartları için maksimum bakiye sınırını döndürür.
    @staticmethod
    def maksimum_bakiye():
        return 5000

    # Kart sınıfının tip bilgisini döndürür.
    @classmethod
    def kart_tipi_bilgisi(cls):
        return cls.__name__
    
    @property
    def kart_tipi(self):
        return self._kart_tipi
    
    #Para birimi bilgisini gösterir.  
    def para_birimi_bilgisi(self):
        return f"Kampüs kartı para birimi: {self.currency}"   
    
#Otobüs kartı ödeme yöntemini temsil eder.
class OtobusCardPayment(CampusCardPayment):
    def __init__(self, owner, currency, bakiye=0):
        super().__init__(owner, currency, bakiye)
        self._kart_tipi = "Otobüs Kartı"

#Bisiklet kartı ödeme yöntemini temsil eder.
class BisikletCardPayment(CampusCardPayment):
    def __init__(self, owner, currency, bakiye=0):
        super().__init__(owner, currency, bakiye)
        self._kart_tipi = "Bisiklet Kartı"

#Scooter kartı ödeme yöntemini temsil eder.
class ScooterCardPayment(CampusCardPayment):
    def __init__(self, owner, currency, bakiye=0):
        super().__init__(owner, currency, bakiye)
        self._kart_tipi = "Scooter Kartı"