from datetime import date


class AuthorizationError(Exception):
    pass

class PaymentMethod:
    def __init__(self, owner, currency):
        self.owner = owner
        self.currency = currency

    def kontrol(self, amount):
        raise NotImplementedError

    def odeme(self, amount):
        raise NotImplementedError

class CreditCardPayment(PaymentMethod):
    def __init__(self, owner, limit, currency):
        super().__init__(owner, currency)
        self.limit = limit

    def kontrol(self, amount):
        return self.limit >= amount

    def odeme(self, amount):
        if not self.kontrol(amount):
            raise AuthorizationError("Kredi kartı limiti yetersiz.")
        self.limit -= amount
        return True


class OnlineWalletPayment(PaymentMethod):
    def __init__(self, owner, balance, currency):
        super().__init__(owner, currency)
        self.balance = balance

    def kontrol(self, amount):
        return self.balance >= amount

    def odeme(self, amount):
        if not self.kontrol(amount):
            raise AuthorizationError("Cüzdan bakiyesi yetersiz.")
        self.balance -= amount
        return True

class PaymentMethodRepository:
    def __init__(self):
        self.methods = []

    def ekle(self, method):
        self.methods.append(method)

    def kullanici_secimi(self, owner):
        return [m for m in self.methods if m.owner == owner]


class TransactionRepository:
    def __init__(self):
        self.transactions = []

    def ekle(self, t):
        self.transactions.append(t)

    def kullaniciya_gore(self, owner):
        return [s for s in self.transactions if s.owner == owner]

class Transaction:
    def __init__(self, owner, amount, payment_type):
        self.owner = owner
        self.amount = amount
        self.payment_type = payment_type
        self.tarih = date.today()


class PaymentService:
    def __init__(self, payment_repo, transaction_repo):
        self.payment_repo = payment_repo
        self.transaction_repo = transaction_repo

    def toplam_tutar_hesapla(self, siparis):
        return sum(siparis)

    def uygun_odeme_yontemi_sec(self, owner, tutar):
        for method in self.payment_repo.kullanici_secimi(owner):
            if method.kontrol(tutar):
                return method
        return None

    def odeme_yap(self, owner, siparis):
        toplam = self.toplam_tutar_hesapla(siparis)
        method = self.uygun_odeme_yontemi_sec(owner, toplam)

        if method is None:
            raise AuthorizationError("Uygun ödeme yöntemi bulunamadı.")

        method.odeme(toplam)
        self.transaction_repo.ekle(
            Transaction(owner, toplam, type(method).__name__)
        )

payment_repo = PaymentMethodRepository()
transaction_repo = TransactionRepository()
service = PaymentService(payment_repo, transaction_repo)

print("// ÖDEME SİSTEMİ DEMO //")

ogrenci = input("Öğrenci adı: ")

kart_limit = int(input("Kredi kartı limiti (TL): "))
cuzdan_bakiye = int(input("Online cüzdan bakiyesi (TL): "))

kart = CreditCardPayment(ogrenci, kart_limit, "TRY")
cuzdan = OnlineWalletPayment(ogrenci, cuzdan_bakiye, "TRY")

payment_repo.ekle(kart)
payment_repo.ekle(cuzdan)

print("\n--- Sipariş Oluşturma ---")
adet = int(input("Kaç ürün aldınız?: "))

siparis = []
for i in range(adet):
    fiyat = int(input(f"{i+1}. ürün fiyatı (TL): "))
    siparis.append(fiyat)

print("\nToplam Tutar:", sum(siparis), "TL")

try:
    service.odeme_yap(ogrenci, siparis)
    print("\n Ödeme başarılı")
except AuthorizationError as e:
    print("\n Ödeme başarısız:", e)

print("\n İŞLEM GEÇMİŞİ")
for s in transaction_repo.kullaniciya_gore(ogrenci):
    print(f"Tarih: {s.tarih} | Tutar: {s.amount} TL | Tür: {s.payment_type}")
