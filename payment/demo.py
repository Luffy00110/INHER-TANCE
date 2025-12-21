from base import PaymentMethod
from CampusCardPayment import CampusCardPayment, OtobusCardPayment, BisikletCardPayment, ScooterCardPayment
from CashPayment import CashPayment
from CreditCardPayment import VisaCardPayment, MasterCardPayment, TroyCardPayment, ZiraatCardPayment, HalkbankCardPayment, GarantiCardPayment, AkbankCardPayment, VakifbankCardPayment
from OnlineWalletPayment import OnlineWalletPayment
from YemekCardPayment import YemekCardPayment
from repository import PaymentMethodRepository, TransactionRepository
from service import PaymentService, Transaction, AuthorizationError

# --- Repository ve Service oluştur ---
payment_repo = PaymentMethodRepository()
transaction_repo = TransactionRepository()
service = PaymentService(payment_repo, transaction_repo)

class DemoSimulasyon:
    def __init__(self, payment_service):
        self.ps = payment_service

    # Random sipariş oluşturur ve ödemeyi gerçekleştirir
    def random_siparis_olustur(self, kullanici):
        secilen = []
        for kategori, urunler in self.ps._yemekhane_menu.items():
            if urunler:
                secilen.append(urunler[0]["ad"])
        odeme_yontemi = self.ps.uygun_odeme_yontemi_sec(
            kullanici, self.ps.toplam_tutar_hesapla(secilen)
        )
        self.ps.odeme_yap(kullanici, odeme_yontemi, secilen)
        return secilen
    # Ödeme iadesi testi
    def iade_demo(self, transaction_id):
        basarili = self.ps.odeme_iade(transaction_id)
        if basarili:
            print(f"Iade tamam: Transaction ID {transaction_id}")
        else:
            print(f"Iade başarısız: Transaction ID {transaction_id}")

    # Kullanıcı puan takibi
    def puan_demo(self, kullanici, miktar):
        self.ps.puan_hesapla(kullanici, miktar)
        print(f"{kullanici} için puan güncellendi: {self.ps._puanlar.get(kullanici)}")

    # Otomat stok kontrolü demo
    def otomat_stok_demo(self, kod):
        urun = self.ps.otomat_siparis(kod)
        print(f"Otomat siparişi: {urun['ad']} - {urun['fiyat']} TL")

    # Haftalık ve aylık rapor demo
    def rapor_demo(self):
        print("Haftalık rapor:", self.ps.haftalik_rapor())
        print("Aylık rapor:", self.ps.aylik_rapor())

    # Kullanıcı bazlı istatistik demo
    def kullanici_istatistik_demo(self, kullanici):
        istatistik = self.ps.kullanici_istatistik(kullanici)
        print(f"{kullanici} istatistik: Toplam harcama={istatistik['toplam']} TL, Kategoriler={istatistik['kategoriler']}")
        
# --- Ödeme yöntemleri oluştur ve ekle ---
ali_campus = CampusCardPayment("Ali", "TRY", 500)
ali_otobus = OtobusCardPayment("Ali", "TRY", 300)
ali_bisiklet = BisikletCardPayment("Ali", "TRY", 200)
ali_scooter = ScooterCardPayment("Ali", "TRY", 150)

ali_cash = CashPayment("Ali", "TRY", 1000)
ali_yemek = YemekCardPayment("Ali", "TRY", 400)
ali_wallet = OnlineWalletPayment("Ali", "TRY", "W123", 600)

ali_visa = VisaCardPayment("Ali", "TRY", "1234567890123456", "123", "12/26", 1000, 0.01)
ali_master = MasterCardPayment("Ali", "TRY", "2345678901234567", "234", "01/27", 1500, 0.012)
ali_troy = TroyCardPayment("Ali", "TRY", "345678901234567", "345", "06/25", 800, 0.015)
ali_ziraat = ZiraatCardPayment("Ali", "TRY", "4567890123456789", "456", "11/26", 1200)
ali_halkbank = HalkbankCardPayment("Ali", "TRY", "5678901234567890", "567", "07/25", 1100)
ali_garanti = GarantiCardPayment("Ali", "TRY", "6789012345678901", "678", "10/27", 900)
ali_akbank = AkbankCardPayment("Ali", "TRY", "7890123456789012", "789", "09/26", 950)
ali_vakifbank = VakifbankCardPayment("Ali", "TRY", "8901234567890123", "890", "12/25", 1000)

# Ödeme yöntemlerini repo'ya ekle
for method in [ali_campus, ali_otobus, ali_bisiklet, ali_scooter, ali_cash, ali_yemek, ali_wallet,
               ali_visa, ali_master, ali_troy, ali_ziraat, ali_halkbank, ali_garanti, ali_akbank, ali_vakifbank]:
    payment_repo.payment_method_ekle(method)

# Kullanıcı bakiyesi ve yükleme işlemleri
class Wallet:
    def __init__(self, kullanici, bakiye=0):
        self.kullanici = kullanici
        self.bakiye = bakiye

    def bakiye_yukle(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            return True
        return False

    def bakiye_sorgula(self):
        return self.bakiye

# --- Yemekhane menüsünden sipariş ---
gunun_siparis = service.gunun_menusunden_siparis()
print("Günün menüsü siparişi:", gunun_siparis)

toplam_gunun_siparis = service.toplam_tutar_hesapla(gunun_siparis)
odeme_yontemi = service.uygun_odeme_yontemi_sec("Ali", toplam_gunun_siparis)
service.odeme_yap("Ali", odeme_yontemi, gunun_siparis)

# --- Kafeterya siparişleri ---
try:
    tost_siparis = service.kafeterya_siparis("yiyecek", "Salamlı Tost")
    latte_fiyat = service.kafe_siparis("sicak_icecek", "Latte", "grande", shot=1)
    toplam_kafe = tost_siparis["fiyat"] + latte_fiyat
    odeme_yontemi = service.uygun_odeme_yontemi_sec("Ali", toplam_kafe)
    service.odeme_yap("Ali", odeme_yontemi, [tost_siparis, {"ad":"Latte","fiyat":latte_fiyat}])
except Exception as e:
    print("Kafeterya siparişi hatası:", e)

# --- Otomat siparişi ---
try:
    otomat_urun = service.otomat_siparis("2")  # Bisküvi
    odeme_yontemi = service.uygun_odeme_yontemi_sec("Ali", otomat_urun["fiyat"])
    service.odeme_yap("Ali", odeme_yontemi, [otomat_urun])
except Exception as e:
    print("Otomat siparişi hatası:", e)

# --- Yemek kartı ile sipariş ---
ali_yemek.yemek_sec("Kayseri Mantısı", 70)
ali_yemek.yemek_sec("Çoban Salata", 30)
ali_yemek.odeme()
print("Yemek kartı kalan bakiye:", ali_yemek.bakiye)

# --- Online Wallet ödeme testi ---
ali_wallet.odeme(50)
print("Online Wallet bakiye:", ali_wallet.bakiye)

# --- Kredi kartı ödemeleri ---
for kart in [ali_visa, ali_master, ali_troy, ali_ziraat, ali_halkbank, ali_garanti, ali_akbank, ali_vakifbank]:
    try:
        odeme_miktari = 100  # Ödenecek ürün tutarı
        kart.odeme(odeme_miktari)
    except ValueError as e:
        print(f"{kart.kart_turu} ile ödeme başarısız: {e}")

# --- Campus kart ödemeleri ---
for kart in [ali_campus, ali_otobus, ali_bisiklet, ali_scooter]:
    print(f"{kart.owner} {kart.kart_tipi} ile ödeme: ", kart.odeme(50))

# --- Cash ödemesi ---
ali_cash.odeme(200)
print("Cash ödeme sonrası bakiye:", ali_cash.odeme_amount)

# --- İşlem geçmişi raporu ---
print("\nTüm işlem geçmişi:")
for t in service.islem_gecmisi("Ali"):
    print(f"{t.owner} - {t.amount} {t.payment_type} ({t.tarih})")

# --- Tarih aralığı raporu ---
from datetime import date, timedelta
baslangic = date.today() - timedelta(days=7)
bitis = date.today()
rapor = service.tarih_araligi_raporu(baslangic, bitis)
print("\nSon 7 gün işlemleri:")
for t in rapor:
    print(f"{t.owner} - {t.amount} {t.payment_type} ({t.tarih})")

# --- Ayın her haftasından örnek siparişler ---
for hafta, urunler in service._ayin_menusu.items():
    siparis = service.siparis_olustur(urunler)
    toplam = service.toplam_tutar_hesapla(siparis)
    odeme_yontemi = service.uygun_odeme_yontemi_sec("Ali", toplam)
    service.odeme_yap("Ali", odeme_yontemi, siparis)

print("\nAyın tüm haftaları siparişleri tamamlandı!")

# --- Ekstra testler: invalid işlemler ---
try:
    service.kafeterya_siparis("yiyecek", "Pizza")
except Exception as e:
    print("Hata yakalandı:", e)

try:
    service.kafe_siparis("sicak_icecek", "Espresso", "grande", shot=2)
except Exception as e:
    print("Hata yakalandı:", e)

try:
    service.otomat_siparis("10")
except Exception as e:
    print("Hata yakalandı:", e)