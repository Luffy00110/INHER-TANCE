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

print("""
1 - Yemekhane
2 - Kafeterya
3 - Kafe
4 - Otomat """)

secim = input("Seçim: ")
siparis = []

if secim == "1":
    print("\n--- GÜNÜN MENÜSÜ ---")
    urunler = service.gunun_menusunden_siparis()

    for u in urunler:
        print(f"{u['ad']} - {u['fiyat']} TL")

    siparis.extend(urunler)

if secim == "2":
    menu = service.kafeterya_menu_listele()
    print(menu)

    kategori = input("Kategori: ")
    urun = input("Ürün adı: ")

    siparis.append(service.kafeterya_siparis(kategori, urun))

if secim == "3":
    menu = service.kafe_menu_listele()
    print(menu)

    kategori = input("Kategori: ")
    kahve = input("İçecek: ")
    boyut = input("Boyut (tall/grande/venti): ")
    shot = int(input("Ekstra shot: "))

    fiyat = service.kafe_siparis(kategori, kahve, boyut, shot)
    siparis.append({"ad": kahve, "fiyat": fiyat})

if secim == "4":
    menu = service.otomat_menu_listele()
    print(menu)

    kod = input("Ürün kodu: ")
    siparis.append(service.otomat_siparis(kod))

print("\nToplam Tutar:", sum(siparis), "TL")

try:
    service.odeme_yap(ogrenci, siparis)
    print("\n Ödeme başarılı")
except AuthorizationError as e:
    print("\n Ödeme başarısız:", e)

print("\n İŞLEM GEÇMİŞİ")
for s in transaction_repo.kullaniciya_gore(ogrenci):
    print(f"Tarih: {s.tarih} | Tutar: {s.amount} TL | Tür: {s.payment_type}")
